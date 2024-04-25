from sklearn.linear_model import LinearRegression

def predict(confirmed, deaths):
    # Sample linear regression model
    model = LinearRegression()
    X = [[confirmed, deaths]]
    y = [confirmed - deaths]
    
    model.fit(X, y)
    
    predicted_recovered = model.predict([[confirmed, deaths]])
    
    return int(predicted_recovered[0])
