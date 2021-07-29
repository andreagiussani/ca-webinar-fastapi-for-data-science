from dataclasses import dataclass
from transformers import pipeline


@dataclass
class SentimentAnalysisPipeline:
    pipeline_name: str

    def get_model(self):
        return pipeline(self.pipeline_name)
