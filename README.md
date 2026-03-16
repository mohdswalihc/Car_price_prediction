🚗 Built a full end-to-end Car Price Prediction app — and you can run it with a single command.

From raw car data to a live prediction API, this project covers the full ML engineering stack:

🔹 Trained a Scikit-learn pipeline to predict car prices
🔹 Served it as a REST API using FastAPI (port 8000)
🔹 Built an interactive Streamlit frontend (port 8501)
🔹 Packaged everything into a Docker image — zero setup for anyone who wants to try it

The architecture is simple but production-minded:
User → Streamlit UI → FastAPI → ML Model → Predicted Price

▶️ Run it yourself in seconds:

docker pull mhdswalih/car_price-prediction:latest
docker run -p 8000:8000 -p 8501:8501 mhdswalih/car_price-prediction

Open http://localhost:8501 and start predicting! 🎯

🐳 Docker Hub → https://hub.docker.com/r/mhdswalih/car_price-prediction
💻 GitHub → https://github.com/mohdswalihc/Car_price_prediction

Feedback and stars are always welcome! 🙌

#MachineLearning #Python #FastAPI #Streamlit #Docker #MLOps #DataScience #OpenSource #AI
