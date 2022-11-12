#!/usr/bin/env python3

import bibtexparser
import pandas as pd

with open("../../Dropbox/Backup/konyvek.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

df = pd.DataFrame(bib_database.entries)
books = df[['author', 'title', 'year', 'isbn', 'url']]
books_sorted = books.sort_values(by=['author', 'title'])
books_sorted.to_excel("../../Dropbox/Backup/konyvek.xls", index=False, engine='xlsxwriter')
