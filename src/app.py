from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.5 - Testing public repo deployment
launch_gradio_demo(SentimentAnalysisTool)
