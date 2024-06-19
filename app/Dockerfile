FROM --platform=linux/amd64 python:3.11 as build

# ADD node_map /node_map
# ADD node_map/generate_combined_map.py .
# ADD node_map/navigator.py .
# ADD node_map/startup_helpers.py .
# ADD node_map/__init__.py .
# ADD main.py .
# ADD requirements.txt .

COPY . .

RUN pip install -r requirements.txt

# CMD ["fastapi", "run", "main.py", "--port", "80"]
CMD ["fastapi", "run", "main.py"]
