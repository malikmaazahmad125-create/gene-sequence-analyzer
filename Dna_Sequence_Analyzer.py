# ==========================================
# DNA ANALYZER
# Python Project by Maazi
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("=" * 50)
print("DNA ANALYZER")
print("Python Project by Maazi")
print("=" * 50)


# ==========================================
# STEP 1: INPUT DNA SEQUENCE
# ==========================================

dna = input("\nEnter your DNA sequence: ").upper().strip()


# ==========================================
# STEP 2: VALIDATE DNA SEQUENCE
# ==========================================

valid_bases = "ATGC"
valid = True

for base in dna:
    if base not in valid_bases:
        valid = False
        break


if not valid or len(dna) == 0:

    print("\nInvalid DNA sequence!")
    print("Only A, T, G, C are allowed.")

else:

    print("\nDNA sequence is valid!")


    # ==========================================
    # STEP 3: BASIC INFORMATION
    # ==========================================

    length = len(dna)

    A = dna.count("A")
    T = dna.count("T")
    G = dna.count("G")
    C = dna.count("C")

    print("\n" + "=" * 50)
    print("BASIC INFORMATION")
    print("=" * 50)

    print("DNA Sequence:", dna)
    print("Length:", length)

    print("\nA:", A)
    print("T:", T)
    print("G:", G)
    print("C:", C)


    # ==========================================
    # STEP 4: BASE PERCENTAGES
    # ==========================================

    A_percentage = (A / length) * 100
    T_percentage = (T / length) * 100
    G_percentage = (G / length) * 100
    C_percentage = (C / length) * 100

    print("\n" + "=" * 50)
    print("BASE PERCENTAGES")
    print("=" * 50)

    print("A Percentage:", round(A_percentage, 2), "%")
    print("T Percentage:", round(T_percentage, 2), "%")
    print("G Percentage:", round(G_percentage, 2), "%")
    print("C Percentage:", round(C_percentage, 2), "%")


    # ==========================================
    # STEP 5: GC AND AT CONTENT
    # ==========================================

    GC_content = ((G + C) / length) * 100
    AT_content = ((A + T) / length) * 100

    print("\n" + "=" * 50)
    print("DNA CONTENT")
    print("=" * 50)

    print("GC Content:", round(GC_content, 2), "%")
    print("AT Content:", round(AT_content, 2), "%")


    # ==========================================
    # STEP 6: DNA COMPLEMENT
    # ==========================================

    complement = ""

    for base in dna:

        if base == "A":
            complement += "T"

        elif base == "T":
            complement += "A"

        elif base == "G":
            complement += "C"

        elif base == "C":
            complement += "G"


    # ==========================================
    # STEP 7: REVERSE DNA
    # ==========================================

    reverse = dna[::-1]


    # ==========================================
    # STEP 8: REVERSE COMPLEMENT
    # ==========================================

    reverse_complement = complement[::-1]


    print("\n" + "=" * 50)
    print("DNA ANALYSIS")
    print("=" * 50)

    print("Original DNA:", dna)
    print("Complement:", complement)
    print("Reverse DNA:", reverse)
    print("Reverse Complement:", reverse_complement)


    # ==========================================
    # STEP 9: DNA TO RNA
    # ==========================================

    rna = dna.replace("T", "U")

    print("\n" + "=" * 50)
    print("DNA TO RNA CONVERSION")
    print("=" * 50)

    print("RNA:", rna)


    # ==========================================
    # STEP 10: CODON ANALYSIS
    # ==========================================

    codons = []

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        codons.append(codon)

    print("\n" + "=" * 50)
    print("CODON ANALYSIS")
    print("=" * 50)

    print("Codons:", codons)
    print("Number of Codons:", len(codons))


    # ==========================================
    # STEP 11: STORE DATA FOR VISUALIZATION
    # ==========================================

    bases = ["A", "T", "G", "C"]

    counts = [A, T, G, C]

    percentages = [
        A_percentage,
        T_percentage,
        G_percentage,
        C_percentage
    ]


    # ==========================================
    # STEP 12: DATA VISUALIZATION
    # ==========================================

    print("\nCreating Data Visualizations...")


    # ------------------------------------------
    # GRAPH 1: BASE FREQUENCY BAR CHART
    # ------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.bar(bases, counts)

    plt.title("DNA Base Frequency")
    plt.xlabel("DNA Bases")
    plt.ylabel("Count")

    for i, value in enumerate(counts):
        plt.text(i, value + 0.1, str(value), ha="center")

    plt.show()


    # ------------------------------------------
    # GRAPH 2: BASE PERCENTAGE PIE CHART
    # ------------------------------------------

    plt.figure(figsize=(7, 7))

    plt.pie(
        percentages,
        labels=bases,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("DNA Base Percentage")

    plt.show()


    # ------------------------------------------
    # GRAPH 3: GC VS AT CONTENT
    # ------------------------------------------

    content_names = ["GC Content", "AT Content"]

    content_values = [
        GC_content,
        AT_content
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        content_names,
        content_values
    )

    plt.title("GC Content vs AT Content")
    plt.xlabel("DNA Content")
    plt.ylabel("Percentage (%)")

    plt.ylim(0, 100)

    for i, value in enumerate(content_values):

        plt.text(
            i,
            value + 2,
            f"{value:.2f}%",
            ha="center"
        )

    plt.show()


    # ------------------------------------------
    # GRAPH 4: BASE DISTRIBUTION LINE GRAPH
    # ------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.plot(
        bases,
        percentages,
        marker="o",
        linewidth=2,
        markersize=8
    )

    plt.title("DNA Base Percentage Distribution")

    plt.xlabel("DNA Bases")
    plt.ylabel("Percentage (%)")

    plt.ylim(0, 100)

    plt.grid()

    plt.show()


    # ==========================================
    # FINAL REPORT
    # ==========================================

    print("\n" + "=" * 50)
    print("FINAL DNA SEQUENCE REPORT")
    print("=" * 50)

    print("DNA Sequence:", dna)
    print("Length:", length)

    print("\nBase Counts:")

    print("A =", A)
    print("T =", T)
    print("G =", G)
    print("C =", C)

    print("\nGC Content =", round(GC_content, 2), "%")
    print("AT Content =", round(AT_content, 2), "%")

    print("\nNumber of Codons =", len(codons))

    print("\nProject completed successfully!")
