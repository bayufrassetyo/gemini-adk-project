# 1. Gunakan image Python resmi yang ringan
FROM python:3.10-slim

# 2. Atur environment variables agar Python tidak membuat file .pyc 
# dan log langsung muncul di Cloud Logs (tidak ter-buffer)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Tentukan direktori kerja di dalam kontainer
WORKDIR /app

# 4. Copy requirements dulu untuk memanfaatkan Docker layer caching
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy seluruh kode aplikasi ke dalam kontainer
COPY . .

# 7. Expose port 8080 (standar Cloud Run)
EXPOSE 8080

# 8. Jalankan aplikasi menggunakan Gunicorn untuk performa produksi
# main:app merujuk pada file main.py dan objek Flask 'app'
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8080"]