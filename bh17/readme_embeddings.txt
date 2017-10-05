#### UNSUPERVISED FEATURE LEARNING 
### NODE/EDGE EMBEDDINGS AS FEATURES 
# Software downloaded on Sep 11, 2017.

# 1. owl inference and graph closure
# in: graph out: mappingFile (index of entities) outWrapper (triples using indexes)

groovy ../../walking-rdf-and-owl/RDFWrapper.groovy -i ../3-rdf-owl/edges.sif.n3 -o outWrapper.txt -m mappingFile.txt -d ../onto-dir -c true

# 2. random walks on RDF and OWL

../../walking-rdf-and-owl/deepwalk outWrapper.txt walksFile.txt

# 3. learning embeddings

../../walking-rdf-and-owl/example/word2vec/bin/word2vec -train walksFile.txt -output embeddingsFile.txt

# 4. map indexes to uri in the feature vectors file learnt

groovy ../../walking-rdf-and-owl/UnMap.groovy -i embeddingsFile.txt -m mappingFile.txt -o embeddingsFile_mapped.txt
 
#### PREDICTIONS
### TRAINING MACHINE LEARNING MODEL

Weka (java) or Scikit-learn (python) software can be used. We used Weka v3.9.1.

