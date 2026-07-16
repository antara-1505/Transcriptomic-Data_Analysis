from Bio import AlignIO

# Read an alignment result file (e.g., from ClustalW)
alignment = AlignIO.read("example.aln", "clustal")
print(alignment)


# from Bio.Seq import Seq
# from Bio import SeqIO


# dna_seq = Seq("ATGCTACGTA")

# print("DNA SEQUENCE:", dna_seq)

# print("Complement DNA Sequence:", dna_seq.complement())

# print("Reverse Complement DNA Sequence:", dna_seq.reverse_complement())

# print("RNA Transcription:", dna_seq.transcribe())

# print("Protein Translation:", dna_seq.translate())


# # reading sequence from fasta format
# for record in SeqIO.parse("example.fasta", "fasta"):
#     print("ID", record.id)
#     print("sequence", record.seq)
#     print("sequence length", len(record.seq))

# # writing in fasta sequence
