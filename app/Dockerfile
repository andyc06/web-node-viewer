FROM --platform=linux/amd64 python:3.11 as build

COPY . .

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "main.py", "--port", "80"]
