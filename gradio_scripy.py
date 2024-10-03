import gradio as gr
import os
from download_paper import download_arxiv_paper  # 导入你的下载函数

def download_papers(urls):
    output_dir = 'G:\\paper'  # 默认使用G盘的paper目录
    urls = urls.split(',')  # 将输入的URL字符串分割成列表
    for url in urls:
        download_arxiv_paper(url.strip(), output_dir)
    return "下载完成！"

# 示例脚本函数
def script_one(input_text):
    # 脚本一的处理逻辑
    return f"脚本一处理结果: {input_text}"

def script_two(input_text):
    # 脚本二的处理逻辑
    return f"脚本二处理结果: {input_text}"

# Gradio 界面定义
with gr.Blocks() as demo:
    gr.Markdown("## 脚本集合器")
    
    with gr.Tab("下载arxiv论文"):
        input_urls = gr.Textbox(lines=2, placeholder="输入多个URL，用逗号分隔")
        output_status = gr.Textbox(lines=2, placeholder="输出结果")
        btn_download = gr.Button("下载arxiv论文")
        btn_download.click(download_papers, inputs=input_urls, outputs=output_status)
    
    with gr.Tab("脚本一"):
        input_text_one = gr.Textbox(lines=2, placeholder="输入文本")
        output_text_one = gr.Textbox(lines=2, placeholder="输出结果")
        btn_one = gr.Button("运行脚本一")
        btn_one.click(script_one, inputs=input_text_one, outputs=output_text_one)
    
    with gr.Tab("脚本二"):
        input_text_two = gr.Textbox(lines=2, placeholder="输入文本")
        output_text_two = gr.Textbox(lines=2, placeholder="输出结果")
        btn_two = gr.Button("运行脚本二")
        btn_two.click(script_two, inputs=input_text_two, outputs=output_text_two)

# 运行 Gradio 界面
demo.launch()