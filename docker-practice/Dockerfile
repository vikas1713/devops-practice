FROM python:3.11-slim
WORKDIR /app
COPY site_check.py .
COPY sites.txt .
RUN pip install requests
CMD ["python", "site_check.py"]
