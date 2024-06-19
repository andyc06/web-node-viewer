FROM --platform=linux/amd64 python:3.11 as build

WORKDIR .
ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app --reload"]
