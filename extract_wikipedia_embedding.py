import xml.etree.ElementTree as ET
import re
import json
import transformers
from sentence_transformers import SentenceTransformer
transformers.BertTokenizer = transformers.BertJapaneseTokenizer
import numpy as np
import time
import os
import torch

def extract_wikipedia_embeddings(xml_file_path, output_json_path):
    """
    Extract Wikipedia articles and generate embeddings, saving incrementally
    
    Args:
    xml_file_path (str): Path to the input XML file
    output_json_path (str): Path to save the output JSON file
    """
    def clean_text(text):
        """
        Clean and normalize extracted text
        
        Args:
        text (str): Raw text to be cleaned
        
        Returns:
        str: Cleaned text
        """
        # Remove XML/HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove references and citation markers
        text = re.sub(r'\[[0-9]+\]', '', text)
        
        # Limit text length to prevent overwhelming the transformer
        # return text[:1000]  # Limit to first 1000 characters
        return text

    # Check and print GPU availability
    print("CUDA available:", torch.cuda.is_available())
    print("Current device:", torch.cuda.current_device() if torch.cuda.is_available() else "CPU")
    
    # Load Sentence Transformer model with explicit device setting
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SentenceTransformer('tohoku-nlp/bert-base-japanese-v3', device=device)

    # Batch processing variables
    batch_size = 1000
    flush_size = 1000
    current_batch = []
    total_processed = 0
    start_time = time.time()
    
    # Prepare output file (create or truncate)
    with open(output_json_path, 'w', encoding='utf-8') as f:
        f.write('[\n')
    
    # Track first item for JSON comma handling
    is_first_item = True
    
    # Iterate through the XML file
    context = ET.iterparse(xml_file_path, events=('end',))
    
    for event, elem in context:
        # Look for page elements
        if elem.tag.endswith('page'):
            try:
                # Extract title and text
                title_elem = elem.find('{*}title')
                text_elem = elem.find('.//{*}text')
                
                if title_elem is not None and text_elem is not None:
                    title = title_elem.text
                    text = text_elem.text
                    
                    if text:
                        # Clean the text
                        cleaned_text = clean_text(text)
                        
                        # Skip very short articles
                        if len(cleaned_text) > 50:
                            current_batch.append({
                                'title': title,
                                'text': cleaned_text
                            })
                
                # Process batch when it reaches batch size
                if len(current_batch) == batch_size:
                    # Extract texts for embedding
                    texts = [item['text'] for item in current_batch]
                    
                    # Generate embeddings for the batch
                    embeddings = model.encode(texts, precision="binary", normalize_embeddings=True)
                    
                    # Append to output file
                    with open(output_json_path, 'a', encoding='utf-8') as f:
                        for i, article in enumerate(current_batch):
                            # Handle JSON comma for proper formatting
                            if not is_first_item:
                                f.write(',\n')
                            
                            # Write article with embedding
                            json.dump({
                                'title': article['title'],
                                'embedding': embeddings[i].tolist()
                            }, f, ensure_ascii=False)
                            
                            is_first_item = False
                    
                    # Update total processed and check progress
                    total_processed += batch_size
                    
                    # Display progress every 1000 articles
                    if total_processed % flush_size == 0:
                        elapsed_time = time.time() - start_time
                        print(f"Processed {total_processed} articles. "
                              f"Elapsed time: {elapsed_time:.2f} seconds")
                    
                    # Reset batch
                    current_batch = []
                
                # Clear the element to save memory
                elem.clear()
            
            except Exception as e:
                print(f"Error processing page: {e}")
    
    # Process any remaining articles in the last batch
    if current_batch:
        texts = [item['text'] for item in current_batch]
        embeddings = model.encode(texts)
        
        # Append remaining articles to output file
        with open(output_json_path, 'a', encoding='utf-8') as f:
            for i, article in enumerate(current_batch):
                # Handle JSON comma for proper formatting
                if not is_first_item:
                    f.write(',\n')
                
                # Write article with embedding
                json.dump({
                    'title': article['title'],
                    'embedding': embeddings[i].tolist()
                }, f, ensure_ascii=False)
                
                is_first_item = False
        
        # Update total processed for final batch
        total_processed += len(current_batch)
    
    # Close the JSON array
    with open(output_json_path, 'a', encoding='utf-8') as f:
        f.write('\n]')
    
    # Final progress report
    elapsed_time = time.time() - start_time
    print(f"\nTotal articles processed: {total_processed}")
    print(f"Total processing time: {elapsed_time:.2f} seconds")

def main():
    # Example usage
    input_xml_path = 'jawiki-20241120-pages-articles-multistream.xml'  # Replace with your XML file path
    output_json_path = 'wikipedia_articles_embeddings.json'
    
    # Extract articles and generate embeddings
    extract_wikipedia_embeddings(input_xml_path, output_json_path)
    
    # Optional: print first few lines to verify
    print("\nFirst few lines of the output:")
    with open(output_json_path, 'r', encoding='utf-8') as f:
        for _ in range(5):
            print(f.readline().strip())

if __name__ == "__main__":
    main()
