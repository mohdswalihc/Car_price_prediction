<div align="center">

# 🚗 Car Price Prediction

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=2E9EF7&center=true&vCenter=true&width=600&lines=End-to-End+ML+Price+Predictor;FastAPI+%2B+Streamlit+%2B+Docker;Pull+and+Run+in+Seconds!" alt="Typing SVG" />

<br/>

[![Docker Pulls](https://img.shields.io/docker/pulls/mhdswalih/car_price-prediction?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)](https://hub.docker.com/r/mhdswalih/car_price-prediction)
[![Docker Image Size](https://img.shields.io/docker/image-size/mhdswalih/car_price-prediction/latest?style=for-the-badge&logo=docker&logoColor=white&color=2496ED)](https://hub.docker.com/r/mhdswalih/car_price-prediction)
[![GitHub Stars](https://img.shields.io/github/stars/mohdswalihc/Car_price_prediction?style=for-the-badge&logo=github&logoColor=white&color=181717)](https://github.com/mohdswalihc/Car_price_prediction/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mohdswalihc/Car_price_prediction?style=for-the-badge&logo=github&logoColor=white&color=181717)](https://github.com/mohdswalihc/Car_price_prediction/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<br/>

**A production-ready ML app that predicts car prices in real time.**
Built with FastAPI · Streamlit · Scikit-learn · Docker

<br/>

[🚀 Quick Start](#-quick-start) · [📖 API Docs](#-api-reference) · [🏗️ Architecture](#%EF%B8%8F-architecture) · [🤝 Contributing](#-contributing)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

🎯 **Real-time Predictions**
Enter car details and get an instant price estimate via a clean Streamlit UI

⚡ **Production-grade API**
FastAPI backend with auto-generated Swagger docs at `/docs`

</td>
<td width="50%">

🐳 **Zero Setup with Docker**
Pull and run — no Python, no installs, no configuration needed

🧠 **Scikit-learn Pipeline**
Trained ML pipeline with full preprocessing and prediction in one step

</td>
</tr>
</table>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     🐳 Docker Container                      │
│                                                              │
│   ┌──────────────┐   POST /predict   ┌──────────────────┐  │
│   │  Streamlit   │ ────────────────► │     FastAPI      │  │
│   │   Frontend   │                   │     Backend      │  │
│   │  :8501  🖥️   │ ◄──────────────── │    :8000  ⚡     │  │
│   └──────────────┘   predicted price └────────┬─────────┘  │
│                                               │              │
│                                               ▼              │
│                                    ┌──────────────────┐     │
│                                    │    ML Pipeline   │     │
│                                    │  car_price.pkl 🧠│     │
│                                    └──────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Technology | File |
|:---|:---|:---|
| 🖥️ Frontend | Streamlit | `frontend.py` |
| ⚡ Backend API | FastAPI + Uvicorn | `app.py` |
| 🧠 ML Pipeline | Scikit-learn | `model/car_price_pipeline.pkl` |
| 📐 Input Schema | Pydantic | `schema/user_input.py` |
| 🔮 Prediction Logic | Python | `predict.py` |

---

## 🚀 Quick Start

### Option 1 — 🐳 Docker (Recommended)

> No setup required. Works on any machine with Docker installed.

```bash
# Pull the image
docker pull mhdswalih/car_price-prediction:latest

# Run the container
docker run -p 8000:8000 -p 8501:8501 mhdswalih/car_price-prediction
```

Then open your browser:

| Interface | URL |
|:---|:---|
| 🖥️ Streamlit UI | http://localhost:8501 |
| ⚡ FastAPI Swagger | http://localhost:8000/docs |

<br/>

<details>
<summary><b>Option 2 — 🐍 Run Locally (click to expand)</b></summary>

<br/>

**Step 1 — Clone the repo**

```bash
git clone https://github.com/mohdswalihc/Car_price_prediction.git
cd Car_price_prediction
```

**Step 2 — Create a virtual environment**

```bash
python -m venv env

# Activate on macOS/Linux
source env/bin/activate

# Activate on Windows
env\Scripts\activate
```

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Run FastAPI backend**

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

**Step 5 — Run Streamlit frontend** *(open a new terminal)*

```bash
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0
```

</details>

---

## 📖 API Reference

### `POST /predict`

Predicts the price of a car based on the provided features.

**Request body**

```json
{
  "year": 2019,
  "km_driven": 45000,
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual",
  "owner": "First Owner"
}
```

**Response**

```json
{
  "predicted_price": 650000.0
}
```

<details>
<summary><b>📋 Full Input Field Reference (click to expand)</b></summary>

<br/>

| Field | Type | Accepted Values |
|:---|:---|:---|
| `year` | `int` | `2005` – `2023` |
| `km_driven` | `int` | e.g. `10000`, `45000`, `120000` |
| `fuel` | `string` | `Petrol` · `Diesel` · `CNG` · `Electric` |
| `seller_type` | `string` | `Individual` · `Dealer` · `Trustmark Dealer` |
| `transmission` | `string` | `Manual` · `Automatic` |
| `owner` | `string` | `First Owner` · `Second Owner` · `Third Owner` |

</details>

> 💡 Explore and test all endpoints interactively at `http://localhost:8000/docs`

---

## 📁 Project Structure

```
Car_price_prediction/
│
├── 📄 app.py                         # FastAPI app & /predict endpoint
├── 📄 frontend.py                    # Streamlit UI
├── 📄 predict.py                     # Prediction logic
├── 📄 requirements.txt               # Python dependencies
├── 🐳 Dockerfile                     # Docker build instructions
├── 📄 .dockerignore
│
├── 📂 model/
│   └── 🧠 car_price_pipeline.pkl     # Trained Scikit-learn pipeline
│
└── 📂 schema/
    └── 📄 user_input.py              # Pydantic input validation schema
```

---

## 🧰 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

</div>

---

## 🐳 Docker Details

| Property | Value |
|:---|:---|
| Image | `mhdswalih/car_price-prediction` |
| Tag | `latest` |
| Platform | `linux/amd64` |
| Compressed Size | ~289 MB |
| API Port | `8000` |
| UI Port | `8501` |

🔗 [View on Docker Hub](https://hub.docker.com/r/mhdswalih/car_price-prediction)

---

## 🤝 Contributing

Contributions are welcome and appreciated!

```bash
# 1. Fork the repo and clone it
git clone https://github.com/YOUR_USERNAME/Car_price_prediction.git

# 2. Create a new branch
git checkout -b feature/your-feature-name

# 3. Make your changes and commit
git commit -m "feat: add your feature description"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

> Please open an issue first for major changes so we can discuss the approach.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 👤 Author

**Mohd Swalih**

[![GitHub](https://img.shields.io/badge/GitHub-mohdswalihc-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mohdswalihc)
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-mhdswalih-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/mhdswalih)

<br/>

**⭐ If this project helped you, please give it a star — it means a lot!**

<br/>

<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
&nbsp;
<img src="https://forthebadge.com/images/badges/made-with-python.svg" />

</div>
