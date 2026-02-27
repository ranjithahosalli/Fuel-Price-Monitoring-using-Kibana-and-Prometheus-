FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir Flask==3.0.0
COPY mock_api.py /app/mock_api.py
EXPOSE 8000
CMD ["python", "mock_api.py"]
