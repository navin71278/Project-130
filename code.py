import csv
import pandas as pd

df = pd.read_csv("merged_dataset.csv")

del df["Constellation"]
del df["App."]
del df["Declination"]
del df["Distance"]
del df["Right"]
del df["Spectral"]
del df["Discovery"]
del df["Brown dwarf"]

df.to_csv('main.csv')