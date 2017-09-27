#### UNSUPERVISED FEATURE LEARNING 
### NODE/EDGE EMBEDDINGS AS FEATURES 

# 1. owl inference and graph closure
# in: graph out: mappingFile (index of entities) outWrapper (triples using indexes)

#groovy ../RDFWrapper.groovy -i bio-knowledge-graph.n3 -o outWrapper.txt -m mappingFile.txt -d onto_dir/ -c true
groovy ../../walking-rdf-and-owl/RDFWrapper.groovy -i ../3-rdf-owl/edges.sif.n3 -o outWrapper.txt -m mappingFile.txt -d ../onto-dir -c true

# 2. random walks on RDF and OWL

#../deepwalk outWrapper.txt walksFile.txt
../../walking-rdf-and-owl/deepwalk outWrapper.txt walksFile.txt

# 3. learning embeddings

#word2vec/bin/word2vec -train walksFile.txt -output embeddingsFile.txt
../../walking-rdf-and-owl/example/word2vec/bin/word2vec -train walksFile.txt -output embeddingsFile.txt

# 4. map indexes to uri in the feature vectors file learnt

#groovy ../UnMap.groovy -i embeddingsFile.txt -m mappingFile.txt -o embeddingsFile_mapped.txt
groovy ../../walking-rdf-and-owl/UnMap.groovy -i embeddingsFile.txt -m mappingFile.txt -o embeddingsFile_mapped.txt
 
#### PREDICTIONS
### TRAINING MACHINE LEARNING MODEL


