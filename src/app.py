from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.1.0 - Testing git credential store auth
launch_gradio_demo(SentimentAnalysisTool)
