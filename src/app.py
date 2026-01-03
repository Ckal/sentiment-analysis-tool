from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.8 - Testing with secrets configured
launch_gradio_demo(SentimentAnalysisTool)
