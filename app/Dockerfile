FROM --platform=linux/amd64 python:3.11 as build

ADD folder /node_map
ADD generate_combined_map.py .
ADD navigator.py .
ADD startup_helpers.py .
ADD __init__.py .
ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app --reload"]
