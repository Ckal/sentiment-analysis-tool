from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.4 - Testing deployment pipeline
launch_gradio_demo(SentimentAnalysisTool)
