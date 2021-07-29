import secrets

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from nlp_app.model import SentimentAnalysisPipeline
# from model import SentimentAnalysisPipeline  # if run with container
from nlp_app.oauth2 import get_current_user
# from oauth2 import get_current_user  # if run with container

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'This is a Sentiment Analysis App'}


class SentimentResponse(BaseModel):
    sentiment: str
    probability: float


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    correct_username = secrets.compare_digest(form_data.username, 'tonystark')
    correct_password = secrets.compare_digest(form_data.password, 'ironman')
    if not(correct_username and correct_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.post('/sentiment_analysis/')
async def sentiment_analysis(
        text: str,
        username: str = Depends(get_current_user)
):

    print(f"Auth User {username} Successfull")
    model = SentimentAnalysisPipeline(pipeline_name='sentiment-analysis').get_model()
    prediction = model(text)

    sentiment = prediction[0]['label']
    score = prediction[0]['score']

    print(f'Sentiment is {sentiment} with probability {round(score, 4)}')

    return SentimentResponse(
        sentiment=sentiment, probability=score
    )
