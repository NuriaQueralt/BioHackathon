# Walking the NGLY1 deficiency RDF and OWL graph

This is the application of the [neuro-symbolic learning algorithm](https://doi.org/10.1093/bioinformatics/btx275), which is an unsupervised feature learning on RDF and OWL, on the NGLY1 deficiency (OMIM:615273, ORPHA:404454)-seeded [hetionet](http://het.io/). We applied this method and used the graph features learnt to the task prediction of drugs repositioned for the extremely rare monogenetic disease _NGLY1 deficiency_. Read more [info](https://docs.google.com/presentation/d/17sduqUMjJxYBKIuTAXGdRRAuclsmP_ZcW9HXSLHCaYk/edit?usp=sharing) to complement this workflow.

##### Prerequisites
The walking-rdf-and-owl software was downloaded on Sep 11, 2017. The software is available at [GitHub](https://github.com/bio-ontology-research-group/walking-rdf-and-owl).
The machine learning was performed by using [Weka](https://www.cs.waikato.ac.nz/ml/weka/) (for Java), but any other software suite like scikit-learn for Python can be used.


Here is the description of the steps to reproduce the study:

### Unsupervised feature learning
In this part, we applied the learning algorithm to obtain node/edge embedding vectors as features. 
Run all the following from the current workdir:

#### 1. Build the NGLY1 deficiency graph
Build the graph running a modified version of the [Jupyter notebook](https://github.com/dhimmel/integrate/blob/master/integrate.ipynb) created by Daniel Himmelstein to build hetionet. Run:

~~~~
jupyter nbconvert --execute 1-graph-building/ngly1_bh_hetionet.ipynb --inplace --ExecutePreprocessor.timeout=-1
~~~~

#### 2. Graph RDFization
Run:

~~~~
python 2-rdf/edges2rdf.py
~~~~

#### 3. Add OWL ontologies (the semantic layer)
Run:

~~~~
python 3-rdf-owl/addOnto.py
~~~~

#### 4. Learn graph embeddings

0. Install the `walk-rdf-and-owl` software. I installed in an upper level to the current directory.

Run all the following from the `4-learn-embeddings/` workdir:

1. OWL inference and graph closure. 
Input: `edges.sif.n3` the RDF/OWL graph
Output: `outWrapper.txt` the classified RDF graph using the OWL ontologies in `onto-dir/` directory
Run:

~~~~
groovy ../../walking-rdf-and-owl/RDFWrapper.groovy -i ../3-rdf-owl/edges.sif.n3 -o outWrapper.txt -m mappingFile.txt -d ../onto-dir -c true
~~~~

2. Random walks on RDF and OWL graph

3. Learn embeddings

4. Map indexes to URIs in the learnt feature vectors file


### Drug repositioning predictions for NGLY1 deficiency
In this part, we explain how to use the feature embedding vectors representing the graph structure to make predictions on new drug-disease edges in the graph. We used the features to train a machine learning logistic regression model.

#### 5. Train the model
#### 6. Make predictions


## Contributors
Robert Hoehndorf, Goto Susumu, Pier Luigi Buttigieg, Kiyoko F. Aoki-Kinoshita, Tiffany Callahan.

## Collaborators
- The Scripps Research Institute
- KAUST
- Database Center for Life Science (DBCLS)

## License

## Acknowledgments
To the DBCLS and [BioHackathon 2017](http://2017.biohackathon.org/) sponsors and organizers to select and allow this project happen. And also to all the BioHackathon participants for all the inspiring discussions and fruitful ideas.
