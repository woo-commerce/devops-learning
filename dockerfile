FROM python:3.10-slim
WORKDIR /app
COPY app/ .
RUN pip install --no-cache-dir -r requirment.txt
EXPOSE 8081
CMD ["python", "app.py"]
