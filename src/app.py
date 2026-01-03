from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.1.4 - Testing authenticated HF clone
launch_gradio_demo(SentimentAnalysisTool)
