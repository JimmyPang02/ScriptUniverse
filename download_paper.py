import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import os
from tqdm import tqdm

# 设置代理（全局代理）
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'

def download_arxiv_paper(url, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取论文标题
    title = soup.find('h1', class_='title mathjax').text.strip()
    title = title.replace('Title:', '')
    print(title)
    
    # 从URL中获取发表时间
    date = url.split('/')[-1][:4]  # 提取URL中的年月信息
    print(date)

    # 处理文件名中的非法字符 :
    safe_title = re.sub(r':\s*', '-', title)  # 将冒号及其后的空格替换为连字符
    print(safe_title)
    
    # 构建新的文件名
    new_filename = f"{date}_{safe_title}.pdf"
    print(new_filename)
    
    # 获取PDF下载链接
    pdf_url = url.replace('abs', 'pdf')
    print(pdf_url)
    
    # 下载PDF文件
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }
    pdf_response = requests.get(pdf_url, stream=True, proxies=proxies)
    total_size_in_bytes = int(pdf_response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    # 构建完整的文件路径
    full_path = os.path.join(output_dir, new_filename)
    
    with open(full_path, 'wb') as f:
        for data in pdf_response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
    
    print(f"文件已下载并重命名为: {new_filename}")

def main():
    output_dir = 'G:\\paper'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 示例使用
    arxiv_urls = [
        'https://arxiv.org/abs/2307.04738',  # 替换为你要下载的论文URL
        'https://arxiv.org/abs/2307.04739',  # 可以添加更多URL
    ]
    
    for url in arxiv_urls:
        download_arxiv_paper(url, output_dir)

if __name__ == "__main__":
    main()