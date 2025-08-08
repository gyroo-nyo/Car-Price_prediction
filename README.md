# 🚗 Car Price Prediction

This project predicts the price of a car based on features such as **year**, **mileage**, **fuel type**, and more, using **Machine Learning**.

## 📌 Features
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Machine Learning model training  
- Model evaluation using R² score  
- Visualization of actual vs predicted prices  

## 🛠 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/gyroo-nyo/Car-Price_prediction.git

2. Navigate into the project directory:

   bash
   Copy
   Edit
   cd Car-Price_prediction

3. Install required dependencies:

   bash
   Copy
   Edit
   pip install -r requirements.txt

# 📂 Dataset
The dataset Car_Price_Prediction.csv contains:

Year – Year of manufacture

Fuel Type – Petrol, Diesel, Electric (encoded as numbers)

Transmission – Manual or Automatic (encoded)

Engine Size – Size in liters

Mileage – Distance driven in miles

Price – Target variable to predict

# ⚙️ Model Workflow
Data Preprocessing – Handling categorical features by mapping to numerical values.

Feature Selection – Selecting Year, Fuel Type, Transmission, Engine Size, and Mileage.

Model Selection – Using LinearRegression with hyperparameter tuning via GridSearchCV.

Evaluation – R² score for training and testing datasets.

Visualization – Scatter plot of actual vs predicted prices.




# 🧠 Technologies Used
Python

Pandas & NumPy

Scikit-learn

Matplotlib

# 🚀 Future Improvements
Try advanced models like Random Forest, XGBoost.

Perform deeper feature engineering.

Deploy model as a web app using Streamlit or Flask.