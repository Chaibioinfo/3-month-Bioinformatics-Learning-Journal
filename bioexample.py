from Bio import SeqIO
from Bio.Seq import Seq

list_of_seqs = []
for seq_record in SeqIO.parse("ladyorchid.fasta", "fasta"):
    list_of_seqs.append(seq_record.seq)
    str_seqs = [str(s) for s in list_of_seqs]
    joined_str = ''.join(str_seqs)
    concatenated = Seq(joined_str)
    print(concatenated)
