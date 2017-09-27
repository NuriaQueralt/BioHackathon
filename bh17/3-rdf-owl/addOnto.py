header = 1
nodeTypeDict = dict()
for line in open('../1-graph-building/out/nodeTypes2uri.tsv', 'r').readlines():
    if header:
        header = 0
        continue
    kind, uri = line.strip().split('\t')
    nodeTypeDict[kind] = uri

header = 1
predDict = dict()
for line in open('../1-graph-building/out/metaedges2uri.tsv', 'r').readlines():
    if header:
        header = 0
        continue
    edge, abbr, iri = line.strip().split('\t')
    predDict[abbr] = iri

header = 1
nodeDict = dict()
for line in open('../1-graph-building/out/nodes2uri.tsv', 'r').readlines():
    if header:
        header = 0
        continue
    kind, nsid, ns = line.strip().split('\t')
    key = kind
    if  kind == 'Pathway':
        key = nsid
    nodeDict[key] = ns

f = open('edges.sif.n3', 'w')
header = 1
for line in open('../1-graph-building/out/edges.sif', 'r').readlines():
    if header:
        header = 0
        continue
    sub, pred, obj = line.strip().split('\t')
    sub_type = sub.split('::')[0]
    obj_type = obj.split('::')[0]
    sub_id = sub.split('::')[1]
    obj_id = obj.split('::')[1]
    pred = predDict[pred]
    key = obj.split('::')[0]
    if obj.split('::')[0] == 'Pathway':
        key = obj.split('::')[1][:2].lower()
    sub = nodeDict[sub.split('::')[0]]+sub.split('::')[1].replace(':','_')
    obj = nodeDict[key]+obj.split('::')[1].replace(':','_')
    f.write('<{}> <{}> <{}> .\n'.format(sub,pred,obj))
    f.write('<{}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{}> .\n'.format(sub,nodeTypeDict[sub_type]))
    f.write('<{}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{}> .\n'.format(obj,nodeTypeDict[obj_type]))
    if sub_type in ['Disease','Molecular Function','Cellular Component','Biological Process']:
        classIri = 'http://purl.obolibrary.org/obo/'+sub_id.replace(':','_')
        f.write('<{}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{}> .\n'.format(sub,classIri))
    if obj_type in ['Disease','Molecular Function','Cellular Component','Biological Process']:
        classIri = 'http://purl.obolibrary.org/obo/'+obj_id.replace(':','_')
        f.write('<{}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{}> .\n'.format(obj,classIri))
f.close()

