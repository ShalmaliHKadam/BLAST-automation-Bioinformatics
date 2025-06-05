

from Bio.Blast import NCBIWWW, NCBIXML
import matplotlib.pyplot as plt
import numpy as np

# Reading the sequence from FASTA file
with open("sequence.fasta") as fasta_file:
    fasta_string = fasta_file.read()

# Submitting BLAST query to NCBI
print("Running BLAST search... this may take a few seconds.")
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

# Saving the BLAST result as XML
with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()
print("BLAST result saved as blast_result.xml")

# Parse BLAST result
with open("blast_result.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)

hit_ids = []
e_values = []

# Extracting top 10 hits
for alignment in blast_record.alignments[:10]:
    for hsp in alignment.hsps:
        hit_ids.append(alignment.hit_def)
        e_values.append(hsp.expect)
        break  # only take the first HSP

# Plotting the E-values (log scale)
log_e_values = [-1 * np.log10(e if e > 1e-180 else 1e-180) for e in e_values]

plt.figure(figsize=(12, 8))
bars = plt.barh(hit_ids, log_e_values, color='skyblue')
plt.xlabel('-log10(E-value)', fontsize=12)
plt.title('Top 10 BLAST Hits', fontsize=14)
plt.gca().invert_yaxis()
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adding E-value labels to each bar
for i, v in enumerate(log_e_values):
    plt.text(v + 1, i, f"{e_values[i]:.1e}", va='center', fontsize=9)

# Save the output
plt.savefig("blast_plot.png", bbox_inches='tight')
plt.show()

# Blast to csv result
import csv

# Step 6: Export summary to CSV
with open("blast_summary.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hit Number", "Accession", "E-value", "Bit Score", "Alignment Length", "Hit Description"])

    for i, alignment in enumerate(blast_record.alignments[:10], start=1):
        for hsp in alignment.hsps[:1]:
            writer.writerow([
                i,
                alignment.accession,
                f"{hsp.expect:.2e}",
                f"{hsp.bits:.2f}",
                alignment.length,
                alignment.hit_def
            ])

print("Summary saved to blast_summary.csv")
