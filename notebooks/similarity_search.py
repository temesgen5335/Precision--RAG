import os
import openai
import numpy as np
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to load embeddings from CSV
def load_embeddings_from_csv(file_path):
    df = pd.read_csv(file_path)
    print("Columns in CSV file:", df.columns)  # Print columns to debug
    if "embedding" not in df.columns:
        raise KeyError("The 'embedding' column is not present in the CSV file.")
    df["embedding"] = df["embedding"].apply(lambda x: np.fromstring(x.strip("[]"), sep=","))
    return df

# Function to compute cosine similarity using NumPy
def compute_cosine_similarity(query_embedding, embeddings):
    query_embedding = np.array(query_embedding)
    embeddings = np.array([np.array(embed) for embed in embeddings])
    similarities = np.dot(embeddings, query_embedding) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding))
    return similarities

# Function to perform similarity search
def similarity_search(query, embeddings_df):
    response = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002"
    )
    query_embedding = response['data'][0]['embedding']
    similarities = compute_cosine_similarity(query_embedding, embeddings_df["embedding"])
    embeddings_df["similarity"] = similarities
    return embeddings_df.sort_values(by="similarity", ascending=False)

# Example usage
if __name__ == "__main__":
    # Load embeddings
    embeddings_df = load_embeddings_from_csv('new_embeddings.csv')

    # Perform similarity search
    query = "References"
    results = similarity_search(query, embeddings_df)
    print(results.head())