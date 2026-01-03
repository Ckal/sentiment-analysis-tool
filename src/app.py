from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.2 - Testing full CI/CD pipeline
launch_gradio_demo(SentimentAnalysisTool)
