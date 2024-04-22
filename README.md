# Master Thesis: Enhancing Large Language Models through external Domain Knowledge
GitHub Repository created by [Laslo Welz](https://github.com/LasHarry/)

## Introduction

The prototype was build in a Linux enivronment using [WSL](https://learn.microsoft.com/de-de/windows/wsl/about).
This is recommended for using the ColBERT library. To run the scripts, it is recommended to train the model on a GPU using the Nvidia CUDA environment.
A list of all required libraries is in this [config file](conda_env.yml).

## Functionality
* [Processing and Knowledge Base Creation](process_documents.ipby): Loads the documents from the [folder](research/) and extracts the text and metadata. The text is cleaned and chunked into smaller segments. All chunks are loaded into one single [file](collection1024token.tsv).



Some additional links:
* [DSPy](https://github.com/stanfordnlp/dspy)
* [ColBERT](https://github.com/stanford-futuredata/ColBERT/blob/main/docs/intro.ipynb)
* [Phi-2](https://huggingface.co/microsoft/phi-2)
