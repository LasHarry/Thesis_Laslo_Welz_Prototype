from PyPDF2 import PdfReader
import glob
from thefuzz import process

PATH = 'research/'
keyword_list = []
new_item = 'Language Model'

for file in glob.glob('{}*.pdf'.format(PATH)):
    meta = PdfReader(file)

    title_meta = meta.metadata.title
    try:
        keywords_meta = str(list(meta.metadata.items())[7][1])
        kw_meta = keywords_meta.split(';')

    except:
        pass

    keyword_list.extend(x for x in kw_meta if x not in keyword_list)

print(keyword_list)
result = process.extract(new_item, keyword_list, limit=5)
print(result)

input_added = False

for k, s in result:
    if s > 80:
        if not input_added:
            keyword_list.append(new_item)
            input_added = True
            print("new Item added: " + str(new_item))
    else:
        print("Item not relevant")

