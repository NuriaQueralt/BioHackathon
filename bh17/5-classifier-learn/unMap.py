mapDict = dict()
for line in open('mappingFile.txt').readlines():
    obs,i = line.strip().split('\t')
    mapDict[i] = obs.replace('::',',')

header = 1
with open('predictions_mapped.csv', 'w') as f:
    for line in open('predictions.csv').readlines():
        if header: 
            header = 0
        else:
            line = line.split(',')
            f.write('{},{}'.format(mapDict[line[0]],','.join(line[1:])))
