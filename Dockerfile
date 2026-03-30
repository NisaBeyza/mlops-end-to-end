# 1. Hafif bir Python sürümü seçiyoruz
FROM python:3.11-slim

# 2. Konteyner içindeki çalışma klasörümüzü belirliyoruz
WORKDIR /app

# 3. Kütüphane listemizi kopyalayıp kurulumları yapıyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projemizdeki tüm kodları ve model dosyamızı konteynere kopyalıyoruz
COPY . .

# 5. FastAPI'nin dış dünyayla iletişim kuracağı portu açıyoruz
EXPOSE 8000

# 6. Konteyner ayağa kalktığında çalıştırılacak nihai komut
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
