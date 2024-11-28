FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 6111
CMD ["python", "manage.py", "runserver", "0.0.0.0:6111"]