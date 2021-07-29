# Cloud Academy Webinar Series
## FastAPI for Data Science
This repo is a companion for the Cloud Academy Webinar entitled *FastAPI for Data Science*.

### Overview
🤖 The aim of this webinar is to show you how to serve a Data Science app with FastAPI.
At the end of the webinar, the material will be made available here.

👉 Note that no data is required for this webinar: this means you do not need to download anything in advanced. 

:mega: Be sure you have the latest Docker version locally installed, as well as all the backend Python requirements, 
available in the `requirements.txt` file.

### Learning Objectives
 - Learn the fundamentals of FastAPI.
 - Learn standard Security Fundamentals in FastAPI (authentication).
 - Build a NLP FastAPI application to perform sentiment analysis.
 - Deploy it using Docker.
 
### What is FastAPI?

FastAPI is a pretty recent Python framework that leverages all modern python 3.6 or above features, such as:
 - type hints;
 - dataclasses;
 - f-strings;
 - the use of asynchronous code with async and await; 
 - ASGI servers.

If you are familiar with Flask or Django, they use WSGI servers - Web Service Gateway Interface servers - which is
**de facto** the Python standard for compatibility between web servers, frameworks, and applications.  
Those do not work for async and await operations, so you need an ASGI servers - asynchronous survey gateway interface server -
such as `uvicorn`.

To locally install FastAPI, please use the pip manager and run `pip install fastapi` as well as `pip install uvicorn` 
to work as the server.
Please note that you can run `pip install uvicorn[standard]` to install only the standard uvicorn features, or directly
`pip install fastapi[all]` to easily includes `uvicorn` in just one requirements.

### Test our the Sentiment Analysis App
Our app expects a string - the piece of text used to perform for sentiment analysis. 
The response contains the sentiment with the corresponsing probability.

To run the app, you just need to open your terminal and run

```bash
 uvicorn nlp_app.app:app --reload
```

You can then navigate in `http://127.0.0.1:8000/docs` and perform a prediction. Alternatively, with the Python requests library, 
you can run the following snippet:
```python
import requests

query = {
    'text':'i love the pizza made by Gaetano, and I would definitely recommend this restaurant to all my friends!'
}
my_headers = {'Authorization' : 'Bearer tonystark'}
response = requests.post('http://127.0.0.1:8000/sentiment_analysis/', params=query, headers=my_headers)
print(response.json())
```
to get a positive prediction. To get a negative one, try for instance the following text
```bash
I have reserved a table in that restaurant, but i was really disappointed by the food!
```

#### Deploy the app with Docker compose

You can build a container by running
```bash
docker-compose up --build nlp_webapp
```

### Feedbacks
You can reach me out at [:email:](andrea.giussani@cloudacademy.com) or on 
[Linkedin](https://it.linkedin.com/in/andrea-giussani-764816148?trk=public_profile_samename_mini-profile_title), 
and you can follow my [:rocket: blog](https://andreagiussani.github.io/the-long-beard-blog/).
