FROM python:3.9-slim-bullseye

WORKDIR /model_gen

COPY gerador_modelo.py .

RUN pip install pandas fpgrowth_py requests

CMD ["python", "gerador_modelo.py"]
