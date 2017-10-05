# Walking the NGLY1 deficiency RDF and OWL graph

This is the application of the [neuro-symbolic learning algorithm](https://doi.org/10.1093/bioinformatics/btx275), which is an unsupervised feature learning on RDF and OWL, on the NGLY1 deficiency (OMIM:615273, ORPHA:404454)-seeded [hetionet](http://het.io/). We applied this method and used the graph features learnt to the task prediction of drugs repositioned for the extremely rare monogenetic disease _NGLY1 deficiency_. More [info](https://docs.google.com/presentation/d/17sduqUMjJxYBKIuTAXGdRRAuclsmP_ZcW9HXSLHCaYk/edit?usp=sharing) to complement this workflow.

##### Prerequisites
The walking-rdf-and-owl software was downloaded on Sep 11, 2017. The software is available at [GitHub](https://github.com/bio-ontology-research-group/walking-rdf-and-owl).
The machine learning was performed by using [Weka](https://www.cs.waikato.ac.nz/ml/weka/) (for Java), but any other software suite like scikit-learn for Python can be used.


Here is the description of the steps to reproduce the study:

### 1. Unsupervised feature learning
In this part, we applied the learning algorithm to obtain node/edge embedding vectors as features.

#### 1. Building the NGLY1 deficiency graph


2. Graph RDFization
3. Adding OWL ontologies (the semantic layer)
4. Learning graph embeddings


### 2. Drug repositioning predictions for NGLY1 deficiency
In this part, we explain how to use the feature embedding vectors representing the graph structure to make predictions on new drug-disease edges in the graph. We used the features to train a machine learning logistic regression model.


## Contributors
Robert Hoehndorf, Goto Susumu, Pier Luigi Buttigieg, Kiyoko F. Aoki-Kinoshita, Tiffany Callahan.

## Collaborators
- The Scripps Research Institute
- KAUST
- Database Center for Life Science (DBCLS)

## License

## Acknowledgments
To the DBCLS and [BioHackathon 2017](http://2017.biohackathon.org/) sponsors and organizers to select and allow this project happen. And also to all the BioHackathon participants for all the inspiring discussions and fruitful ideas.
