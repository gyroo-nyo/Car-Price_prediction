import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

df=pd.read_csv('Car_Price_Prediction.csv')
df["Fuel Type"]=df["Fuel Type"].map({"Petrol":0,"Electric":1,"Diesel":2})
df["Transmission"]=df["Transmission"].map({"Manual":0,"Automatic":1})

X=df[["Year","Fuel Type","Transmission","Engine Size","Mileage"]].values
y=df["Price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=LinearRegression()

'''pipe=Pipeline([
    ("scale",StandardScaler()),
    ("model",LinearRegression()),
])'''


param_grid={
    "fit_intercept": [True, False],
    "positive": [True, False],
}

Grid=GridSearchCV(estimator=model,
                  param_grid=param_grid,
                  cv=5,
                  scoring="r2")
Grid.fit(X_train,y_train)

best_model=Grid.best_estimator_
print(Grid.score(X_train,y_train))
print(Grid.score(X_test,y_test))

from matplotlib import pyplot as plt
y_pred=best_model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # line of perfect prediction
plt.show()
