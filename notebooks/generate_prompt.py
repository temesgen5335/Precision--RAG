
import os
import openai

import numpy as np
import pandas as pd
from similarity_search import load_embeddings_from_csv, compute_cosine_similarity, similarity_search
from dotenv import load_dotenv
#Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Sample prompts and ground truths for inspiration
EXAMPLE_PROMPTS = [
    {
        "prompt": "What are the core tasks for this week's challenge in the context of {context}?",
        "ground_truth": "The core tasks include understanding specific aspects of {context}, such as {detail1}, {detail2}, and planning for {objective}."
    },
    {
                "prompt": "What is the minimum requirement for the interim submission in the challenge?",
                "ground_truth": "The minimum requirement is to have a well-structured repository with some coding progress made."
            },
            {
                "prompt": "What is the key performance indicator for Tuesday's session on RAG components?",
                "ground_truth": "The key performance indicators include understanding prompt ranking, understanding prompt matching, and ability to reuse previous knowledge."
            },
            {
                "prompt": "What is the instruction for Automatic Prompt Engineering Fundamental Tasks?",
                "ground_truth": "The core tasks include understanding prompt engineering tools and concepts, familiarizing with language models, developing a plan for prompt generation and testing, setting up a development environment, designing a user interface for prompt system, planning integration of LLMs, building and refining prompt generation system, developing automatic evaluation data generation system, implementing prompt testing and evaluation mechanism, and refining and optimizing system based on feedback."
            },
            {
                "prompt": "What is the deadline for the final submission in the challenge?",
                "ground_truth": "The final submission deadline is Saturday 8pm UTC."
            }
    # ... other examples ...
]

def generate_custom_prompts(similar_texts, base_query, model="gpt-3.5-turbo-instruct", max_tokens=100):
    custom_prompts = []
    for example in EXAMPLE_PROMPTS:
        for text in similar_texts:
            # Customize the prompt using the example and context from similarity search results
            prompt = example["prompt"].format(context=text, detail1="precision RAG", detail2="prompt engineering")
            # For simplicity, we're not using the ground_truth here but you could incorporate it in your workflow
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7
            )
            generated_prompt = response.choices[0].text.strip()
            custom_prompts.append({
                "original_prompt": prompt,
                "generated_prompt": generated_prompt
            })
    return custom_prompts

def main(query, base_query, embeddings_file='new_embeddings.csv', top_n=5):
    # Load embeddings and perform similarity search
    embeddings_df = load_embeddings_from_csv(embeddings_file)
    results_df = similarity_search(query, embeddings_df)
    top_results = results_df.head(top_n)['text'].tolist()
    
    # Generate custom prompts based on the similarity search results
    generated_prompts = generate_custom_prompts(top_results, base_query)

    # Print the generated prompts
    for prompt_data in generated_prompts:
        print(f"Original Prompt: {prompt_data['original_prompt']}")
        print(f"Generated Prompt: {prompt_data['generated_prompt']}\n")

if __name__ == "__main__":
    query = "References in Precision RAG systems"
    base_query = "Explain the importance of references in the context of Precision Retrieval-Augmentation Generation systems"
    main(query, base_query)