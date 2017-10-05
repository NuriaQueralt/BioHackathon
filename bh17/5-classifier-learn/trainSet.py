compDict = dict()
disDict = dict()
trueDict = dict()
allCompDisDict = dict()
for line in open('../3-rdf-owl/edges.sif.n3', 'r').readlines():
    sub, pred, obj = line.strip().split(' .')[0].split(' ')
    subIri = sub.lstrip('<').rstrip('>')
    subId = sub.rsplit('/', 1)[1].strip('>')
    objIri = obj.lstrip('<').rstrip('>')
    objId = obj.rsplit('/', 1)[1].strip('>')
    #rel = pred.rsplit('/', 1)[1].strip('>')
    if 'drugbank' in subIri:
        compDict[subId] = subIri
    if 'drugbank' in objIri:
        compDict[objId] = objIri
    if 'DOID' in subIri:
        disDict[subId] = subIri
    if 'DOID' in objIri:
        disDict[objId] = objIri
    if 'CtD' in pred:
        trueDict[subId+'::'+objId] = 1

for drug in compDict.keys():
    for disease in disDict.keys():
        allCompDisDict[drug+'::'+disease] = 1

negDict = dict()
for pair in allCompDisDict:
    if pair not in trueDict.keys():
        negDict[pair] = 1

print('len comp: {}'.format(len(compDict)))
print('len dis: {}'.format(len(disDict)))
print('len all: {}'.format(len(allCompDisDict)))
print('len true: {}'.format(len(trueDict)))
print('len neg: {}'.format(len(negDict)))

featureDict = dict()
for line in open('../4-embeddings-learn/embeddingsFile_mapped.txt', 'r').readlines():
    vecList = line.strip().split('\t')
    iri = vecList[0]
    vec = vecList[1:]
    featureDict[iri] = '\t'.join(vec)
    #featureDict[iri] = line.strip()

print('len features: {}'.format(len(featureDict)))

f = open('trainData.csv', 'w')
negList = list(negDict.keys())
i = int(-1)
for pos in trueDict:
    i += 1
    comp,dis = pos.split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('t\t{}\t{}\n'.format(featureDict[compIri],featureDict[disIri]))
    comp,dis = negList[i].split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('f\t{}\t{}\n'.format(featureDict[compIri],featureDict[disIri]))
f.close()

f = open('trainExtData.csv', 'w')
i = int(-1)
for pos in trueDict:
    i += 1
    comp,dis = pos.split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('t\t{}\t{}\n'.format(featureDict[compIri],featureDict[disIri]))
    comp,dis = negList[i].split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('f\t{}\t{}\n'.format(featureDict[compIri],featureDict[disIri]))
    
print(i)    
while i < len(trueDict)*10:
    comp,dis = negList[i].split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('f\t{}\t{}\n'.format(featureDict[compIri],featureDict[disIri]))
    i += 1
print(i)
f.close()

f = open('unclassified.csv', 'w')
m = open('mappingFile.txt', 'w')
i = 1
for obs in allCompDisDict:
    comp,dis = obs.split('::')
    compIri = compDict[comp]
    disIri = disDict[dis]
    f.write('{}\t{}\t?\n'.format(featureDict[compIri],featureDict[disIri]))
    m.write('{}\t{}\n'.format(obs,i))
    i += 1
f.close()
m.close()

