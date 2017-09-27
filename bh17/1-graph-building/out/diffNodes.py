def line2dict(dictionary, key, value):
    value_dict = dictionary.get(key, {})
    value_dict[value] = 1
    dictionary[key] = value_dict
    return dictionary


type_dict = dict()
header = 1
for line in open('./nodes.tsv', 'r').readlines():
    if header:
        header = 0
        continue
    vec = line.split('\t')[0].split('::')
    line2dict(type_dict, vec[0], vec[1])

for key in type_dict:
    print('{} {}'.format(key, type_dict.get(key).keys()))

for key in type_dict:
    print('{}'.format(key))

        

    
