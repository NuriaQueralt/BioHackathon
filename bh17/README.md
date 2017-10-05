# Walking the NGLY1 deficiency RDF and OWL graph

This is the application of the [neuro-symbolic learning algorithm](https://doi.org/10.1093/bioinformatics/btx275), which is an unsupervised feature learning on RDF and OWL, on the NGLY1 deficiency (OMIM:615273, ORPHA:404454)-seeded [hetionet](http://het.io/). We applied this method and used the graph features learnt to the task prediction of drugs repositioned for the extremely rare monogenetic disease _NGLY1 deficiency_. Read more [info](https://docs.google.com/presentation/d/17sduqUMjJxYBKIuTAXGdRRAuclsmP_ZcW9HXSLHCaYk/edit?usp=sharing) to complement this workflow.

##### Prerequisites
The walking-rdf-and-owl software was downloaded on Sep 11, 2017. The software is available at [GitHub](https://github.com/bio-ontology-research-group/walking-rdf-and-owl).
The machine learning was performed by using [Weka](https://www.cs.waikato.ac.nz/ml/weka/) (for Java), but any other software suite like scikit-learn for Python can be used.
Python3 and Groovy.


Here is the description of the steps to reproduce the study:

### Unsupervised feature learning
In this part, we applied the learning algorithm to obtain node/edge embedding vectors as features. 
Run all the following from the current workdir:

#### 1. Build the NGLY1 deficiency graph
Build the graph running a modified version of the [Jupyter notebook](https://github.com/dhimmel/integrate/blob/master/integrate.ipynb) created by Daniel Himmelstein to build hetionet. 
Input: files in `1-graph-building/in/` and `1-graph-building/compile/` directories. To obtain the input files in `1-graph-building/compile/`, run beforehand the Jupyter notebooks therein.
Output: `edges.sif` tabulated graph 
Run:

~~~~
jupyter nbconvert --execute 1-graph-building/ngly1_bh_hetionet.ipynb --inplace --ExecutePreprocessor.timeout=-1
~~~~

#### 2. Graph RDFization
Note, that you can avoid this step because is also implemented in the next one. We firstly created the RDF graph entities using blank nodes, but some incompatibility occurred with the _walk-rdf-and-owl_ method, so we solved this out using minted URIs solution implemented in the next step.
Input: `edges.sif` tabulated graph
Output: `edges.sif.rdf` RDF graph
Run:

~~~~
python 2-rdf/edges2rdf.py
~~~~

#### 3. Graph RDFization and addition of OWL ontologies (the semantic layer)
Input: `edges.sif` graph, `1-graph-building/out/nodeTypes2uri.tsv`, `1-graph-building/out/metaedges2uri.tsv`, and `1-graph-building/out/nodes2uri.tsv`
Output: `edges.sif.n3` RDF and OWL graph
Run:

~~~~
python 3-rdf-owl/addOnto.py
~~~~

#### 4. Learn graph embeddings

0. Install the `walk-rdf-and-owl` software. I installed in an upper level to the current directory.

Run all the following from the `4-learn-embeddings/` workdir:

1. OWL inference and graph closure. 
Input: `edges.sif.n3` the RDF/OWL graph  
Output: `outWrapper.txt` the classified RDF graph using the OWL ontologies in `../onto-dir/` directory  
Run:

~~~~
groovy ../../walking-rdf-and-owl/RDFWrapper.groovy -i ../3-rdf-owl/edges.sif.n3 -o outWrapper.txt -m mappingFile.txt -d ../onto-dir -c true
~~~~

2. Random walks on RDF and OWL graph
Input: `outWrapper.txt` classified graph
Output: `walksFile.txt` corpus of graph walks
Run:

~~~~
../../walking-rdf-and-owl/deepwalk outWrapper.txt walksFile.txt
~~~~

3. Learn embeddings
Input: `walksFile.txt` corpus of graph walks
Output: `embeddingsFile.txt` feature vectors
Run:

~~~~
../../walking-rdf-and-owl/example/word2vec/bin/word2vec -train walksFile.txt -output embeddingsFile.txt
~~~~

4. Map indexes to URIs in the learnt feature vectors file
Input: `embeddingsFile.txt` feature vectors
Output: `embeddingsFile_mapped.txt` mapped feature vectors
Run:

~~~~
groovy ../../walking-rdf-and-owl/UnMap.groovy -i embeddingsFile.txt -m mappingFile.txt -o embeddingsFile_mapped.txt
~~~~

### Drug repositioning predictions for NGLY1 deficiency
In this part, we explain how to use the feature embedding vectors representing the graph structure to make predictions on new drug-disease edges in the graph. We used the features to train a machine learning logistic regression model. Weka (java) or Scikit-learn (python) software can be used. We used Weka v3.9.1.

#### 5. Train the model

1. Create the training set, the unclassified set, and the mapping file.
Input: `4-embeddings-learn/embeddingsFile_mapped.txt` feature vectors, `3-rdf-owl/edges.sif.n3` RDF/OWL graph, 
Output: `trainData.csv` 1:1 true versus false instances training set, `trainExtData.csv` 1:10 true versus false instances training set, `unclassified.csv` observations set, `mappingFile.txt` indexes to drug-disease ID pairs mapping
Run:

~~~~
python trainSet.py
~~~~

2. Train the machine learning model
Input: `trainExtData.csv` training set
Output: model

Run: We used Weka and trained a logistic regression model using 10-fold crossvalidation. 

#### 6. Make predictions
1. Evaluate the unclassified observations using the model.
Input: model, `unclassified.csv` observations set
Output: `predictions.csv` classified observations

Run: In Weka.

2. Unmap the indexed predictions to the drug-disease hypothesis classified.
Input: `mappingFile.txt`, `predictions.csv`
Output: `predictions_mapped.csv` mapped predictions

Run:

~~~~
python unMap.py
~~~~

## Contributors
Robert Hoehndorf, Goto Susumu, Pier Luigi Buttigieg, Kiyoko F. Aoki-Kinoshita, Tiffany Callahan.

## Collaborators
- The Scripps Research Institute
- KAUST

## License

## Acknowledgments
To the DBCLS and [BioHackathon 2017](http://2017.biohackathon.org/) sponsors and organizers to select and allow this project happen. And also to all the BioHackathon participants for all the inspiring discussions and fruitful ideas.
