🚗 Car Price Prediction
This project predicts the price of a car based on features such as Year, Mileage, Fuel Type, Transmission, and Engine Size.
It uses Machine Learning techniques to train and evaluate a predictive model, helping users estimate car prices effectively.

📌 Features
Data Cleaning & Preprocessing – Handling categorical and numerical features

Feature Encoding – Converting text data like "Fuel Type" and "Transmission" into numeric values

Model Training – Uses Linear Regression with hyperparameter tuning via GridSearchCV

Model Evaluation – Performance measured using the R² score

Visualization – Plot of Actual vs Predicted prices for model validation

📂 Dataset
The dataset (Car_Price_Prediction.csv) contains columns:

Year – Manufacturing year of the car

Fuel Type – Petrol, Diesel, Electric

Transmission – Manual, Automatic

Engine Size – Size of the car's engine (in liters)

Mileage – Kilometers driven

Price – Target variable (in currency units)

🛠 Installation & Usage
Clone the repository

bash
Copy
Edit
git clone https://github.com/gyroo-nyo/Car-Price_prediction.git
cd Car-Price_prediction
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the script

bash
Copy
Edit
python car_price_prediction.py
📊 Example Output
After running the model:

Training R² score: ~0.85

Test R² score: ~0.83

Visualization:
The script generates a scatter plot comparing actual vs predicted car prices with a red dashed line representing perfect predictions.

🔍 Model Details
Algorithm: Linear Regression

Hyperparameters Tuned:

fit_intercept: True / False

positive: True / False

Cross-Validation: 5-fold CV via GridSearchCV

Scaling: StandardScaler (optional in pipeline)

📈 Visualization
The output includes a plot:

X-axis: Actual Price

Y-axis: Predicted Price

Line: Red dashed line → perfect prediction line

📌 Future Improvements
Try advanced models like Random Forest or XGBoost for better accuracy

Add feature importance analysis

Deploy the model using Streamlit or Flask for a web interface

Use more extensive datasets for improved generalization

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
