# Starting with base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Installing required packages from requirements.txt file
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copying the FastAPI inference script
COPY ./nlp_app/ /nlp_app

# Setting the working directory appropriately
WORKDIR /nlp_app

# Exposing the appropriate port on the container
EXPOSE 8000

# Setting the entrypoint for the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]