import gradio as gr
from sentiment_analysis import sentiment_analysis_tool

# Version: 1.1.5 - Fixed deprecated transformers.tools import
iface = gr.Interface(
    fn=sentiment_analysis_tool.predicto,
    inputs=gr.Textbox(lines=3, label="Enter text to analyze"),
    outputs=gr.Label(label="Sentiment Analysis Results"),
    title="Sentiment Analysis Tool",
    description="Analyzes the sentiment of text using DistilBERT model"
)

if __name__ == "__main__":
    iface.launch()
