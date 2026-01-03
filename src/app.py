from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.1.1 - Testing PAT_TOKEN with quoted URL
launch_gradio_demo(SentimentAnalysisTool)
