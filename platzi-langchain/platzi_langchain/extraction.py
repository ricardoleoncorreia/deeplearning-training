import requests
import os
from langchain.document_loaders import PyPDFLoader

def fetch_and_load_papers(urls):
  """
  Fetches machine learning papers from specified URLs, saves them to a local directory,
  and loads the content into a list of documents.
  """
  # Create the external data directory path
  downloaded_data_path = '../data/external'
  ml_papers = []

  for i, url in enumerate(urls):
      response = requests.get(url)
      filename = f'paper{i+1}.pdf'
      # Save files in the external data directory
      filepath = os.path.join(downloaded_data_path, filename)
      
      with open(filepath, 'wb') as f:
          f.write(response.content)
          print(f'Downloading {filename} in {filepath}')

          loader = PyPDFLoader(filepath)
          data = loader.load()
          ml_papers.extend(data)

  return ml_papers
