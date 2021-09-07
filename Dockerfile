FROM python:3.9-slim 
WORKDIR /app

COPY app /app
RUN pip3 install -r requirements.txt
WORKDIR /app

EXPOSE 10024

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=10024","--reload"]
