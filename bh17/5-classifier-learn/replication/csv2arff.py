#!/usr/bin/python3

# imports
import sys

# TRAINING dataset
# dataset name
dataset_name = sys.argv[1].split('.')[0]

# open csv file
rows = open(sys.argv[1]).readlines()

# attributes
attributes_l = list()
i = 1
while i < len(rows[0].strip().split('\t')):
    attributes_l.append('@attribute attr_{} numeric'.format(i))
    i += 1
attributes_l.append('@attribute class { t, f }')


# data
data_l = list()
for row in rows:
    row_l = row.strip().split('\t')
    row_l.append(row_l[0])
    row_l.pop(0)
    data_l.append(','.join(row_l))

# open output file
with open('{}.arff'.format(dataset_name), 'w') as f:
    # write preamble
    f.write('% Title: "{}" training dataset for learning\n'.format(dataset_name))
    f.write('%\n')
    f.write('% Number of instances: {}\n'.format(len(data_l)))
    f.write('%\n')
    f.write('% Number of attributes: {} + class attribute\n'.format(len(attributes_l)-1))
    f.write('%\n')

    # write dataset name line
    f.write('\n@relation {}\n'.format(dataset_name))

    # write attributes
    f.write('\n'.join(attributes_l))

    # write data
    f.write('\n@data\n')
    f.write('\n'.join(data_l))
f.close()

## UNCLASSIFIED dataset
# dataset name
dataset_name = sys.argv[2].split('.')[0]

# open csv file
rows = open(sys.argv[2]).readlines()

# attributes
attributes_l = list()
i = 1
while i < len(rows[0].strip().split('\t')):
    attributes_l.append('@attribute attr_{} numeric'.format(i))
    i += 1
attributes_l.append('@attribute class { t, f }')

# data
data_l = list()
for row in rows:
    row_l = row.strip().split('\t')
    data_l.append(','.join(row_l))

# open output file
with open('{}.arff'.format(dataset_name), 'w') as f:
    # write preamble
    f.write('% Title: "{}" dataset for classification\n'.format(dataset_name))
    f.write('%\n')
    f.write('% Number of instances: {}\n'.format(len(data_l)))
    f.write('%\n')
    f.write('% Number of attributes: {} + class attribute\n'.format(len(attributes_l)-1))
    f.write('%\n')

    # write dataset name line
    f.write('\n@relation {}\n'.format(dataset_name))

    # write attributes
    f.write('\n'.join(attributes_l))

    # write data
    f.write('\n@data\n')
    f.write('\n'.join(data_l))
f.close()
