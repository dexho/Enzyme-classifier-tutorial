'''BALANCE THE DATASETS OF POPLAR AND TARDIGRADE PROTEINS SO THERE ARE EQUAL NUMBERS.'''

import random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

pop_fasta = '/Users/desho/Desktop/protein-classifier-tutorial/fasta/poplar.fasta'
tar_fasta = '/Users/desho/Desktop/protein-classifier-tutorial/fasta/tardigrade.fasta'


def balance(pop_fasta, tar_fasta):
    count_pop = 0
    count_tar = 0
    tar_genes = []
    pop_seq_record = SeqIO.parse(pop_fasta, "fasta")
    for i in pop_seq_record:
        tar_genes.append(i)
        count_pop += 1
    
    tar_seq_record = SeqIO.parse(tar_fasta, "fasta")
    for j in tar_seq_record:
        count_tar += 1

    print(count_pop, count_tar)

    with open("balanced_tar.fasta", "a") as handle:
        SeqIO.write(random.sample(tar_genes, count_pop), handle, "fasta")

balance(pop_fasta, tar_fasta)
