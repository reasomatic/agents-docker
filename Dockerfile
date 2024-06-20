FROM ghcr.io/reasomatic/agents-docker:latest

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
