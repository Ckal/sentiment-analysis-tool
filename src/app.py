from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.1.3 - Testing lightweight HF deployment
launch_gradio_demo(SentimentAnalysisTool)
