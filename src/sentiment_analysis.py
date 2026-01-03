import requests
import gradio as gr
from transformers import pipeline

class SentimentAnalysisTool:
    name = "sentiment_analysis"
    description = "This tool analyses the sentiment of a given text input."

    inputs = ["text"]
    outputs = ["json"]
    
    model_id_1 = "nlptown/bert-base-multilingual-uncased-sentiment"
    model_id_2 = "microsoft/deberta-xlarge-mnli"
    model_id_3 = "distilbert-base-uncased-finetuned-sst-2-english"
    model_id_4 = "lordtt13/emo-mobilebert"
    model_id_5 = "juliensimon/reviews-sentiment-analysis"
    model_id_6 = "sbcBI/sentiment_analysis_model"
    model_id_7 = "models/oliverguhr/german-sentiment-bert"
    
    def __call__(self, inputs: str): 
        return self.predicto(inputs)
        
    def parse_output(self, output_json):  
        list_pred = []
        for i in range(len(output_json[0])):
            label = output_json[0][i]['label']
            score = output_json[0][i]['score']
            list_pred.append((label, score))
        return list_pred
    
    def get_prediction(self, model_id):
        classifier = pipeline("text-classification", model=model_id, return_all_scores=True)
        return classifier
    
    def predicto(self, review):
        classifier = self.get_prediction(self.model_id_3)
        prediction = classifier(review)
        print(prediction)
        return self.parse_output(prediction)

# Create an instance of the SentimentAnalysisTool class
sentiment_analysis_tool = SentimentAnalysisTool()
