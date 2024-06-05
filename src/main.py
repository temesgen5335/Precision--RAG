import sys
import os
from langchain_community.document_loaders import DirectoryLoader

# Get the current script directory
current_script_path = os.path.abspath(os.path.dirname(__file__))

# Get the project root directory (assuming 'src' is within the project root)
project_root = os.path.abspath(os.path.join(current_script_path, '..'))

# Add the project root to the system path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set the data path dynamically
DATA_PATH = os.path.join(project_root, 'data', 'books')

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def main():
    try:
        documents = load_documents()
        # print(documents)
        print("Documents loaded successfully.")
        # Process documents
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()