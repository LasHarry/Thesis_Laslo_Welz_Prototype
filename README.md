# Master Thesis: Enhancing Large Language Models through external Domain Knowledge
GitHub Repository created by [Laslo Welz](https://github.com/LasHarry/)

## Introduction

The prototype was build in a Linux enivronment.
This is recommended for using the ColBERT library. To run the scripts, it is recommended to train the model on a GPU using the Nvidia CUDA environment.
A list of all required libraries is in this [config file](conda_env.yml).

## Functionality
* [Processing and Knowledge Base Creation](process_documents.ipynb): Loads the documents from the [folder](research/) and extracts the text and metadata. The text is cleaned and chunked into smaller segments. All chunks are loaded into one single [file](kb/collection1024token.tsv).

* [Knowledge Base Retrieval and Answer Generation](llm_retrieval_agent.ipynb): The retreival model loads the collection and retrieves relevant chunks based the given query. The retreived content is then filled into an instruction prompt. The prompt changes based on the defined interaction. The LLM generates an answer from the prompt.  



Some additional links:
* [DSPy](https://github.com/stanfordnlp/dspy)
* [ColBERT](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)
* [Phi-2](https://huggingface.co/microsoft/phi-2)
