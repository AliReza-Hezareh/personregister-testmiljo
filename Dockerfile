FROM python:3.11

WORKDIR /app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create directory for SQLite database
RUN mkdir -p /data

CMD ["python", "app.py"]