import csv
import re

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open('docs/HitL_Research_Paper.pdf', 'rb') as file:
    pdf = PdfReader(file)
    text = " ".join(page.extract_text() for page in pdf.pages)

clean_text = text.replace('\n', ' ')
clean_text2 = clean_text.replace('- ', '')
clean_text3 = re.sub(r'\[\d+(?:,\s*\d+)*\]', '', clean_text2)

meta = PdfReader('docs/hitl_hcii.pdf')

title_meta = meta.metadata.title
author_meta = meta.metadata.author.strip()
date_meta = str(meta.metadata.creation_date.date())
subject_meta = meta.metadata.subject.split(',')[0]
doi_meta = meta.metadata.subject.split(',')[1].strip()
source_meta = str(list(meta.metadata.items())[4][1])
keywords_meta = str(list(meta.metadata.items())[7][1])

keys = ['title', 'author', 'publish_date', 'subject', 'doi', 'source', 'keywords']
content = [title_meta, author_meta, date_meta, subject_meta, doi_meta, source_meta, keywords_meta]

dict_metadata = dict(zip(keys, content))
# print(dict_metadata)

custom_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=450,
    chunk_overlap=30,
    length_function=len
)

lib = custom_text_splitter.create_documents([clean_text3])

libs = []
for i in range(len(lib)):
    libs.append(lib[i].page_content)

print(type(lib[1].metadata))
for j in range(len(lib)):
    lib[j].metadata.clear()
    lib[j].metadata.update(dict_metadata)

print(lib[6])
# print(libs[0:2])

"""
with open('docs/hitl_refactor.tsv', 'wt', encoding='utf-8') as out_file:
    i = 0
    for line in lib:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([i, line])
        i += 1
"""