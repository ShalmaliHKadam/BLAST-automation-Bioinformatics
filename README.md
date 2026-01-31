# 🔍 Automated BLASTN Search & Visualization | TP53 Gene

This project demonstrates how to automate an NCBI BLASTN query using **Python** and **Biopython**, then parse, visualize, and export the top results.

I used the human **TP53 (tumor protein p53)** gene as input, sent the sequence to NCBI programmatically, extracted the top 10 alignments from the returned XML, and plotted their significance using `-log10(E-values)`.

---

##  Overview

| Task | Description                                                                                        |
|------|----------------------------------------------------------------------------------------------------|
|  Query | BLASTN query of TP53 sequence using Biopython                                                      |
|  Output | 'blast_result.xml' (raw BLAST), 'blast_summary.csv'(top 10 hits), 'blast_plot.png' (visualization) |
|  Parsing | Extracted accession, hit info, e-value, bit score                                                  |
|  Visualization | Bar chart of top 10 hits                                                                           |
|  Export | Summary table to CSV file                                                                          |

---

##  Tools & Technologies

- Python 3.11
- Biopython
- Matplotlib
- NCBI BLAST API
- File formats: FASTA, XML, CSV

---

##  Files in This Project

| File | Description |
|------|-------------|
| `sequence.fasta` | Input sequence (TP53, Homo sapiens) |
| `blast_script.py` | Main script: BLAST + parse + plot + export |
| `blast_result.xml` | Raw BLAST output from NCBI |
| `blast_plot.png` | Visualization of top 10 alignments |
| `blast_summary.csv` | Table of hits with e-values, accessions, scores |
| `README.md` | Project overview, tools, instructions, and preview |

---

##  How to Run

1. **Install required packages**:
```bash
pip install biopython matplotlib
