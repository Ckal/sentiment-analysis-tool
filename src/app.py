from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.1 - Testing CI deployment
launch_gradio_demo(SentimentAnalysisTool)
