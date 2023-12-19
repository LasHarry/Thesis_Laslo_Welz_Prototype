import fitz
import csv

path = 'docs/HitL_Research_Paper.pdf'
doc = fitz.open(path)

# p = 1
# b = 3

# blocks = doc[p].get_text("dict", flags=11)["blocks"]
# print(blocks[b])

t = ''
title = ""
old_title = ""
chapter = ""
old_chapter = ""
section = ""
old_section = ""
article = ""
old_article = ""
paragraph = ""
break_loop = False
# Loop on pages of the document
for p in doc:
    blocks = p.get_text("dict", flags=11)["blocks"]
    title_y = 0.0
    chapter_y = 0.0
    section_y = 0.0
    article_y = 0.0
    # Loop on blocks of a page
    for b in blocks:  # iterate through the text blocks
        if break_loop == True:
            break
        for l in b["lines"]:  # iterate through the text lines
            if break_loop == True:
                break
            for s in l["spans"]:  # iterate through the text spans
                # Ignore header
                if s["bbox"][3] < 50:
                    break
                # Ignore footer
                if s["bbox"][1] > 500:
                    break
                # Ignore the smallest text (like reference to a footnote)
                if s["size"] < 6.5 and not (s["text"].isnumeric()):
                    break
                # Content page at the end of the document is noise for the search, we remove it
                if s["text"].strip() == "Contents" and s["size"] > 10 and s["flags"] == 20:
                    break_loop = True
                    break
                # Get title
                if s["bbox"][1] == title_y and s["text"] != "":
                    title += " " + s["text"].strip()
                # Get title if on a new line
                elif s["text"][:6] == "Title ":
                    title = s["text"].strip()
                    title_y = s["bbox"][1]
                # Get chapter
                elif s["bbox"][1] == chapter_y and s["text"] != "":
                    chapter += " " + s["text"].strip()
                # Get chapter if on a new line
                elif s["text"][:8] == "Chapter ":
                    chapter = s["text"].strip()
                    chapter_y = s["bbox"][1]
                # Get section
                elif s["bbox"][1] == section_y and s["text"] != "":
                    section += " " + s["text"].strip()
                # Get section if on a new line
                elif s["text"][:8] == "Section " and s["flags"] == 20:
                    section = s["text"].strip()
                    section_y = s["bbox"][1]
                # Get article
                elif s["bbox"][1] == article_y and s["text"] != "":
                    article += " " + s["text"].strip()
                # Get article if on a new line
                elif s["text"][:5] == "Art. " and s["flags"] == 20:
                    article = s["text"].strip()
                    article_y = s["bbox"][1]
                # Get paragraph
                # elif s["size"]<6.5 and s["text"].isnumeric():
                #    paragraph="Paragraph "+s["text"]
                else:
                    # For any new article, creates a new piece of text, including title, chapter, section article in
                    # the header of this piece of text.
                    if old_article != article:
                        t += "\n"
                        t += "|" + title + "|" + chapter + "|" + section + "|" + article + "|"
                    t += s["text"]
                    old_article = article
# print(t[1000:3000])

stext = t.split('\n')
with open('docs/Hitl_Refactored.tsv', 'wt', encoding="utf-8") as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    i = 0
    for tex in stext:
        tsv_writer.writerow([i, tex])
        i += 1
