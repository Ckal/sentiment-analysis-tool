from transformers.tools.base import launch_gradio_demo
from sentiment_analysis import SentimentAnalysisTool

# Version: 1.0.3 - Full CI/CD pipeline test
launch_gradio_demo(SentimentAnalysisTool)
