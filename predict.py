from sklearn.linear_model import LinearRegression
import pandas as pd 

data = pd.read_csv('ford.csv')

val1 = input('Mileage : ')
val2 = input('Miles Per Gallon : ')

x_train = data[['mileage', 'mpg']]
y_train = data['price']

model = LinearRegression()
model.fit(x_train, y_train)

x_new = [[int(val1), int(val2)]]
calculation = model.predict(x_new)

print (calculation)