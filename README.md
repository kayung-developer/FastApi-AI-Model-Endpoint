# AI Model Inference with FastAPI

This project demonstrates how to set up a FastAPI endpoint for AI model inference, specifically using a pre-trained sentiment analysis model from the Hugging Face Transformers library.

## Project Structure

- `app/`: Contains the FastAPI application code.
  - `main.py`: Entry point for the FastAPI application.
  - `models/`: Directory for model-related code.
    - `sentiment_model.py`: Contains the sentiment analysis model class.
  - `routers/`: Directory for route definitions.
    - `inference.py`: Contains the route for sentiment analysis inference.
  - `schemas/`: Directory for request/response schemas.
    - `text_data.py`: Contains the schema for text data.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: List of Python dependencies.
- `.dockerignore`: List of files and directories to ignore in the Docker image.
- `README.md`: Project documentation.

## Setup

### Prerequisites

- Docker
- Docker Compose (optional, for more complex setups)

### Running the Application

1. Build the Docker image:

    ```sh
    docker build -t ai-model-inference .
    ```

2. Run the Docker container:

    ```sh
    docker run -d -p 8000:8000 ai-model-inference
    ```

3. Access the API documentation at `http://localhost:8000/docs`.

### Endpoints

- `POST /predict/`: Predict the sentiment of a given text.

### Example Request

```sh
curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d '{"text": "I love FastAPI!"}'
