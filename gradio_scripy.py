import gradio as gr
import os
from download_paper import download_arxiv_paper  # Import your download function

def download_papers(urls):
    output_dir = 'G:\\paper'  # Default to the paper directory on the G drive
    urls = urls.split(',')  # Split the input URL string into a list
    for url in urls:
        download_arxiv_paper(url.strip(), output_dir)
    return "Download completed!"

# Example script function
def script_one(input_text):
    # Processing logic for script one
    return f"Script one result: {input_text}"

def script_two(input_text):
    # Processing logic for script two
    return f"Script two result: {input_text}"

# Gradio interface definition
with gr.Blocks() as demo:
    gr.Markdown("## ScriptUniverse")
    
    with gr.Tab("Download arXiv Papers"):
        input_urls = gr.Textbox(lines=2, placeholder="Enter multiple URLs separated by commas")
        output_status = gr.Textbox(lines=2, placeholder="Output result")
        btn_download = gr.Button("Download arXiv Papers")
        btn_download.click(download_papers, inputs=input_urls, outputs=output_status)
    
    with gr.Tab("Script One"):
        input_text_one = gr.Textbox(lines=2, placeholder="Enter text")
        output_text_one = gr.Textbox(lines=2, placeholder="Output result")
        btn_one = gr.Button("Run Script One")
        btn_one.click(script_one, inputs=input_text_one, outputs=output_text_one)
    
    with gr.Tab("Script Two"):
        input_text_two = gr.Textbox(lines=2, placeholder="Enter text")
        output_text_two = gr.Textbox(lines=2, placeholder="Output result")
        btn_two = gr.Button("Run Script Two")
        btn_two.click(script_two, inputs=input_text_two, outputs=output_text_two)

# Run Gradio interface
demo.launch(ssl_verify=False)