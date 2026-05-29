FROM python:3.12-slim

WORKDIR /app

RUN apt update && apt install -y \
    ffmpeg \
    git \
    curl

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
