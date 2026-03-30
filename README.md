# 🚀 End-to-End MLOps Pipeline: House Price Prediction

Bu proje, bir makine öğrenmesi modelinin eğitilmesinden, modern yazılım mimarileriyle (**FastAPI**, **Docker**, **Kubernetes**) servis edilmesine kadar tüm süreçleri kapsayan uçtan uca bir **MLOps** çalışmasıdır.

## 🎯 Projenin Amacı
Ev fiyatlarını tahmin eden bir modelin sadece bir notebook dosyası olarak kalmayıp, ölçeklenebilir bir mikroservis mimarisiyle nasıl canlıya alınabileceğini (deployment) simüle etmektir.

---

## 🏗 Mimari Yapı ve Akış

Proje dört ana sütun üzerine inşa edilmiştir:

1.  **Model Training (`src/`):** Scikit-learn kullanılarak regresyon modeli eğitildi ve performans metrikleri analiz edildi.
2.  **API Layer (`api/`):** Eğitilen model, yüksek performanslı **FastAPI** kullanılarak bir web servisine dönüştürüldü.
3.  **Containerization (`Dockerfile`):** Uygulama tüm bağımlılıklarıyla birlikte **Docker** imajı haline getirildi.
4.  **Orchestration (`k8s/`):** Hazırlanan imaj, **Kubernetes** üzerinde (Deployment ve Service objeleriyle) ayağa kaldırıldı.

---

## 🛠 Kullanılan Teknolojiler

*   **Dil:** Python 3.9+
*   **ML:** Scikit-learn, Pandas, Joblib
*   **API:** FastAPI, Uvicorn
*   **DevOps:** Docker, Kubernetes (K8s)
*   **Model Management:** Git LFS (Large File Storage)

---

## 🚀 Nasıl Çalıştırılır?

### 1. Yerel Ortamda (Local)
```bash
# Bağımlılıkları kurun
pip install -r requirements.txt

# API'yi başlatın
uvicorn api.app:app --reload
API arayüzüne (Swagger UI) erişmek için: http://localhost:8000/docs
```

### 2. Docker İle
```bash
# İmajı oluşturun
docker build -t mlops-house-app .

# Konteynırı çalıştırın
docker run -p 8000:8000 mlops-house-app
```

### 3. Kubernetes Üzerinde
```bash
# K8s konfigürasyonlarını uygulayın
kubectl apply -f k8s/

# Servis durumunu kontrol edin
kubectl get services
📦 Model Yönetimi (Git LFS)
Bu projede kullanılan .pkl model dosyası GitHub limitlerini aştığı için Git LFS (Large File Storage) kullanılarak versiyonlanmıştır. Repoyu klonladığınızda modelin düzgün inmesi için Git LFS'nin sisteminizde kurulu olması gerekir.
```

✒️ Yazar
Nisa Beyza Nar - LinkedIn Profilime Buradan Ulaşabilirsin: https://www.linkedin.com/in/nisabeyzanar/ 