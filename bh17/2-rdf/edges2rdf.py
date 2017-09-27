header = 1
predDict = dict()
for line in open('../out/metaedges2uri.tsv', 'r').readlines():
    if header:
        header = 0
        continue
    edge, abbr, iri = line.strip().split('\t')
    predDict[abbr] = iri
    #print('{} {} {}'.format(edge, abbr, iri))

header = 1
nodeDict = dict()
for line in open('../out/nodes2uri.tsv', 'r').readlines():
    if header:
        header = 0 
        continue
    kind, nsid, ns = line.strip().split('\t')
    key = kind
    if  kind == 'Pathway':
        key = nsid
    #key = kind+'_'+nsid
    #print('{} {} {}'.format(kind, nsid, ns))
    nodeDict[key] = ns

f = open('edges.sif.rdf', 'w')
header = 1
for line in open('../out/edges.sif', 'r').readlines():
    if header:
        header = 0
        continue
    sub, pred, obj = line.strip().split('\t')
    pred = predDict[pred]
    key = obj.split('::')[0]
    if obj.split('::')[0] == 'Pathway':
        #print('{}'.format(sub.split('::')[1]))
        key = obj.split('::')[1][:2].lower()
        #print('{} {}'.format(key, nodeDict[key]))
    #if obj.split('::')[0] == 'Pathway':
    #sub = nodeDict[sub.split('::')[0]]
    #obj = nodeDict[obj]
    sub = nodeDict[sub.split('::')[0]]+sub.split('::')[1]
    obj = nodeDict[key]+obj.split('::')[1]
    #print('{}'.format(line))
    #print('<{}> {} <{}> .'.format(sub,pred,obj))
    f.write('<{}> {} <{}> .\n'.format(sub,pred,obj))
f.close()
