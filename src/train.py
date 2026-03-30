from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import mlflow

mlflow.set_tracking_uri("file:./mlruns")

# dataset yükle
data = fetch_california_housing()

X = data.data
y = data.target

# train-test ayır
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model oluştur
model = RandomForestRegressor(n_estimators=100)

# MLflow ile experiment başlat
with mlflow.start_run():

    # modeli eğit
    model.fit(X_train, y_train)

    # modeli değerlendir
    score = model.score(X_test, y_test)

    # MLflow log
    mlflow.log_param("model", "RandomForest")
    mlflow.log_metric("score", score)

    # modeli kaydet
    joblib.dump(model, "model.pkl")

print("Model trained and saved!")