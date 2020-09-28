# Protein-classifier-tutorial
A simple SVM machine learning classifier to answer the most urgent of questions: does this membrane protein belong to water bears, or poplar trees? (representatives of brown bears vs. redwood trees, go bears!)

This framework builds a classifer for any type of coding sequence, with any two genbank assmeblies of your choosing. 

##Instructions
Clone this repo, then create a folder named 'genbank' to contain genbank files from NCBI. You can choose any two assemblies, but they must contain the 'CDS' (coding sequence) annotation for you to be able to pull gene sequences out of the genome.

The python scripts explained, in order:
## get-proteins.py
Script for extracting protein sequences out of the genbank file into a fasta file using BioPython. Here, you implement the logic in what kinds of coding sequences you want to extract. In this example, I pulled coding sequences that were annotated with the term "membrane" to find hypothetical membrane-associated proteins.

## balance-sets.py
Balanced sets are important in training models. To ensure the total number of protein sequences is the same across both organisms, use this script.

## build-sets.py
Here, we calculate features of the gene sequences we found previously. The SVM model attempts to draw a hyperplane between the proteins belonging to each organism using the features you specify. In this exmaple, I used the ProtParam package in BioPython to find features such as amino acid composition, secondary structures, molecular weight, etc. 

## train.py
The model is built, trained, and tested here. 
