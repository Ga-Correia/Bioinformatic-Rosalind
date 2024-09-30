from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

fl = "rosalind_clus.txt"
clustalw2_path = "/home/gabriel/Clustalw2/clustalw2"
clustalw_cline = ClustalwCommandline(clustalw2_path, infile=fl)
stdout, stderr = clustalw_cline()
aln = fl.replace(".txt",".aln")
align = AlignIO.read(aln, "clustal")
print(align[len(align)-1].id)
