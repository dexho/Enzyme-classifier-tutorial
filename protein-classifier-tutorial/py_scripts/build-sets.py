'''READS A FASTA FILE AND GENERATES A PANDAS DATAFRAME CONTAINING FEATURES FROM BIOPYTHON PROTPARAM'''

import os
import pandas as pd 
from Bio import SeqUtils
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO

name = "poplar"
fasta_location = "/Users/desho/Desktop/protein-classifier-tutorial/fasta/poplar.fasta"
os.chdir("/Users/desho/Desktop/protein-classifier-tutorial/training_sets")

def make_dataset(fasta):
    # a list of dictionaries containing features for all sequences
    ls_features = []

    # assign whether it's from tardigrades 'tar' or poplars 'pop'
    if 'tar' in fasta:
        target = 0
    elif 'pop' in fasta:
        target = 1

    for record in SeqIO.parse(fasta, "fasta"):
        analysed_seq = ProteinAnalysis(str(record.seq))

        # the dictionary containing features for a single sequence
        dict_features = {}

        # compute length
        dict_features['length'] = len(record.seq)

        # compute molecular weight
        dict_features['mol_weight'] = analysed_seq.molecular_weight()

        # compute aromaticity
        dict_features['aromaticity'] = analysed_seq.molecular_weight()

        # compute stability
        dict_features['stability'] = analysed_seq.instability_index()

        # compute flexibility
        dict_features['flexibility'] = analysed_seq.flexibility()

        # compute isoelectric point
        dict_features['isoelectric'] = analysed_seq.isoelectric_point()

        # compute secondary structure fraction
        frac = analysed_seq.secondary_structure_fraction()
        dict_features['helix'] = frac[0]
        dict_features['turn'] = frac[1]
        dict_features['sheet'] = frac[2]

        # compute AAC composition of entire sequence
        aac = analysed_seq.get_amino_acids_percent()

        # merge all features and dictionaries into dict_features
        dict_features.update(aac)
        ls_features += [dict_features]

    df = pd.DataFrame(ls_features)
    df['target'] = target

    print(df)
    df.to_pickle(name + '_set.pkl')

make_dataset(fasta_location)

