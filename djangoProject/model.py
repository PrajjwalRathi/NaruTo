import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
dataset = pd.read_csv("djangoProject/Social_Network_Ads1.csv")
x = dataset.iloc[:, 1:3].values
y = dataset.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
Random = RandomForestClassifier(n_estimators=30, random_state=0, criterion='entropy')
Random.fit(x_train, y_train)


def pre(age, salary):
    variable = [[age, salary]]
    prediction = Random.predict(variable)
    if age < 18:
        return f"What you doing thinking about car , you are just {age}"
    else:
        if prediction == 1:
            return 'yeah! you worked very hard for it. Nice now go buy a CAR'
        else:
            return 'Sorry! bro try after 8 years'



