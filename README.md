# Precision RAG: Prompt Tuning For Building Enterprise Grade RAG Systems
This project focuses on Automatic Prompt Engineering (APE) for Retrieval-Augmented Generation (RAG) systems.

## Business Objective:

The aims is to simplify LLM interaction through prompt engineering solutions. Through services liike:

Automatic Prompt Generation: Creates effective prompts to generate high-quality content.
Automatic Evaluation Data Generation: Generates diverse test cases for prompt evaluation.
Prompt Testing and Ranking: Evaluates prompts and ranks them based on effectiveness.

## Setup

1. Create a virtual environment and install the required packages:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

2. Create a Virtual Environment and Install Dependencies

```bash
python3.10 -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
``` 
3. Create a free Pinecone account and get your API key from [here](https://www.pinecone.io/).

3. Create a `.env` file and add the following variables:

```bash
OPENAI_API_KEY = [ENTER YOUR OPENAI API KEY HERE]
PINECONE_API_KEY = [ENTER YOUR PINECONE API KEY HERE]
```