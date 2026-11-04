FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
COPY site_check.py .
COPY sites.txt .
RUN pip install --upgrade pip && pip install --upgrade requests certifi
CMD ["python", "site_check.py"]
