import os
import csv
import random
import pandas as pd 
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

'''EXTRACT ALL MEMBRANE-ASSOCIATED PROTEINS FROM GENBANK FILE INTO LIST OF ENTIRES IN FASTA DOCUMENT. 
    INCLUDES GENES WITH 'MEMBRANE' IN PRODUCT DESC'''

tar_genbank = '/Users/desho/Desktop/protein-classifier-tutorial/genbank/GCA_005239225.1_ASM523922v1_genomic.gbff'
pop_genbank = '/Users/desho/Desktop/protein-classifier-tutorial/genbank/GCA_002082055.1_nHd_3.1_genomic.gbff'
name = 'poplar'
os.chdir('/Users/desho/Desktop/protein-classifier-tutorial/fasta')
file_name = 'Users/desho/Desktop/protein-classifier-tutorial/fasta/' + name + '.fasta'

all_genes = {}

def collect_genes(gb):
    global all_genes
    seq_record = SeqIO.parse(gb, "genbank")

    # add all sequences to all_genes
    for record in seq_record:
        for feature in record.features:
            if feature.type == 'CDS':
                try:
                    translation = feature.qualifiers['translation']
                except:
                    translation = None
                locus = feature.qualifiers['locus_tag']
                if translation and locus:
                    try:
                        desc = feature.qualifiers['product'][0]
                    except:
                        desc = ''
                    if 'membrane' in desc:
                        # print(desc)
                        new_seqrecord = SeqRecord(
                            Seq(translation[0]),
                            id = locus[0],
                            name = feature.qualifiers['protein_id'][0],
                            description = desc,
                        )
                        all_genes[locus[0]] = new_seqrecord

collect_genes(pop_genbank)
# print(all_genes)

with open(name + ".fasta", "a") as handle:
    SeqIO.write(all_genes.values(), handle, "fasta")
