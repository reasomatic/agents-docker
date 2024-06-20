FROM ghcr.io/reasomatic/agents-docker:latest

RUN useradd -m -u 1000 user
WORKDIR /app 

COPY --chown=user ./requirements.tx[t] requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt || echo 'requirements.txt does not exist'

# RUN huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

COPY --chown=user . /app

USER user

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]