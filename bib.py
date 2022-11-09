import bibtexparser
import pandas as pd

with open("../../Dropbox/Backup/konyvek.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

df = pd.DataFrame(bib_database.entries)
selection = df[['author', 'title', 'year', 'isbn', 'url']]
selection.to_excel("../../Dropbox/Backup/konyvek.xls", index=False)
