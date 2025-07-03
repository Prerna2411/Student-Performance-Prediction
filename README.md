# 🎓 Student Performance Prediction

This project aims to predict student performance based on various features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and writing score. The goal is to help educators and institutions identify students at risk and implement timely interventions.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Machine Learning Models:** Scikit-learn, XGBoost, CatBoost, AdaBoost, Linear Regression, Random Forest  
- **Web Framework:** Flask (for backend development)  
- **Frontend (Optional):** Streamlit or HTML templates  
- **Deployment:** Azure App Service  
- **Others:** Docker, GitHub Actions (CI/CD)

---

## ✨ Features

- ✅ Data Preprocessing & Feature Engineering  
- ✅ Model Training & Evaluation  
- ✅ Hyperparameter Tuning  
- ✅ Performance Metrics (R² Score, MSE, RMSE)  
- ✅ Dockerized Setup for Production Readiness  
- ✅ Azure App Service Deployment Workflow  
- ✅ HTML Templates for UI Rendering (Optional)

---

## 📁 Project Structure

├── .github/workflows/ # Azure deployment CI/CD workflows
├── .vscode/ # VSCode settings
├── artifacts/ # Contains saved model artifacts
│ └── model/
├── notebook/ # Jupyter notebooks for EDA, model training
├── src/ # Source scripts
│ └── model/
├── templates/ # HTML templates for frontend
├── .gitignore # Ignore config
├── Dockerfile # Docker setup
├── README.md # Project documentation
├── app.py # Flask application
├── main.py # Core pipeline logic
├── requirements.txt # Python dependencies
├── setup.py # Project setup file
├── template.py # Template for dynamic HTML rendering



## 📊 Input Features

The model takes the following input features:

- **Gender**  
- **Race/Ethnicity**  
- **Parental Level of Education**  
- **Lunch Type**  
- **Test Preparation Course**  
- **Writing Score**

---

## 📈 Model Training & Evaluation

Multiple regression-based ML models have been tested and compared. Performance evaluation is based on:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 🚀 Getting Started

### 1. Clone the repository


git clone https://github.com/Prerna2411/student-performance-predictor.git
cd student-performance-predictor

2. Create a virtual environment and install dependencies

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the application locally

python app.py




🐳 Docker Setup (Optional)
To run the project inside a Docker container:


docker build -t student-performance-app .
docker run -p 5000:5000 student-performance-app

☁️ Deployment
Azure App Service deployment is configured via GitHub Actions.

CI/CD workflow is located in .github/workflows/.

🙌 Contributing
Feel free to fork the repository, make enhancements, and create pull requests. All contributions are welcome!

📄 License
This project is licensed under the MIT License.











