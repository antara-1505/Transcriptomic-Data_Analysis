from Bio import pairwise2
from Bio.Seq import Seq

# Sample sequences
seq1 = Seq("TGTGACTA")
seq2 = Seq("CATGGTCA")

# Perform a global alignment
alignments = pairwise2.align.globalxx(seq1, seq2)

# Print results
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))


from Bio import AlignIO

# Read an alignment result file (e.g., from ClustalW)
alignment = AlignIO.read("example.aln", "clustal")
print(alignment)
