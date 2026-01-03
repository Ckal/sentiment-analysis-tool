from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.1.2 - Testing with persist-credentials false
launch_gradio_demo(SentimentAnalysisTool)
