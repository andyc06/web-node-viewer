# web-node-viewer

## Overview

This application implements a viewer for pre-rendered images of nodes in a 3D scene prepared in advance. It consists of a frontend webpage that sends requests to a FastAPI powered backend. The backend loads a directory of rendered images and a YAML file that maps node IDs to X-Y coordinates. For a given starting location and movement type sent by the frontend, the backend returns the new location (node ID) and heading (angle), along with the image name corresponding to the new location and heading.

## Installation

1. Clone this repo
2. cd to ./backend
3. python -m venv venv
4. source venv/bin/activate
5. python -m pip install -r requirements.txt

## Running

1. uvicorn main:app --reload
2. Open ./frontend/game.html

