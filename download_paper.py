import requests
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm


def download_arxiv_paper(url, output_dir):
    if url.endswith('.pdf'):
        pdf_url = url
        new_filename = url.split('/')[-1]  # Use the original filename from the URL
        print(new_filename)
    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get paper title
        title = soup.find('h1', class_='title mathjax').text.strip()
        title = title.replace('Title:', '')
        print(title)
        
        # Get publication date from URL
        date = url.split('/')[-1][:4]  # Extract year and month information from URL
        print(date)

        # Handle illegal characters in filename :
        safe_title = re.sub(r':\s*', '-', title)  # Replace colon and subsequent spaces with hyphen
        print(safe_title)
        
        # Construct new filename
        new_filename = f"{date}_{safe_title}.pdf"
        print(new_filename)
        
        # Get PDF download link
        pdf_url = url.replace('abs', 'pdf')
        print(pdf_url)
    
    # Download PDF file
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }
    pdf_response = requests.get(pdf_url, stream=True)#, proxies=proxies)
    total_size_in_bytes = int(pdf_response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    # Construct full file path
    full_path = os.path.join(output_dir, new_filename)
    
    with open(full_path, 'wb') as f:
        for data in pdf_response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    
    print(f"File has been downloaded and renamed to: {new_filename}")

def main():
    output_dir = 'G:\\paper'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Example usage
    arxiv_urls = [
        'https://robot-ma.github.io/MA_paper.pdf',  # Replace with the URL of the paper you want to download
        'https://arxiv.org/abs/2307.04739',  # You can add more URLs
    ]
    
    for url in arxiv_urls:
        download_arxiv_paper(url, output_dir)

if __name__ == "__main__":
    main()