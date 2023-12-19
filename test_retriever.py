import dspy

colbert_abstracts = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

retrieval_response = colbert_abstracts('When was the first FIFA World Cup held?', k=5)

print(type(colbert_abstracts))
"""
for result in retrieval_response:
    print("Text:", result['text'], "\n")
"""