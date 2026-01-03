from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.6 - Testing complete deployment flow
launch_gradio_demo(SentimentAnalysisTool)
