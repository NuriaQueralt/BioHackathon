# Walking the NGLY1 deficiency RDF and OWL graph
-----

This is the application of the [neuro-symbolic learning algorithm](https://doi.org/10.1093/bioinformatics/btx275), which is an unsupervised feature learning on RDF and OWL, on the NGLY1 deficiency (OMIM:615273, ORPHA:404454)-seeded [hetionet](http://het.io/). We applied this method and used the graph features learnt to the task prediction of drugs repositioned for the extremely rare monogenetic disease _NGLY1 deficiency_. More [info](https://docs.google.com/presentation/d/17sduqUMjJxYBKIuTAXGdRRAuclsmP_ZcW9HXSLHCaYk/edit?usp=sharing).

Here is the description of the steps to reproduce the study:

## 1. Unsupervised feature learning
In this part, we applied the learning algorithm to obtain node/edge embedding vectors as features.
The walking-rdf-and-owl software was downloaded on Sep 11, 2017.

## 2. Drug repositioning predictions for NGLY1 deficiency
In this part, we explain how to use the feature embedding vectors representing the graph structure to make predictions on new drug-disease edges in the graph. We used the features to train a machine learning logistic regression model.
