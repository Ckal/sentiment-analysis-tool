from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.7 - Testing with correct target parsing
launch_gradio_demo(SentimentAnalysisTool)
