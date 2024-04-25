import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
def load_data():
    d = pd.read_csv(r'C:/Users/91950/OneDrive/Documents/deena.ml.assugn/streamlite/country_wise_latest.csv')
    return d

df = load_data()

# Prepare data
X = df[['Confirmed', 'Deaths']]
y = df[['Recovered']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict function
def predict(confirmed, deaths):
    return model.predict([[confirmed, deaths]])[0][0]

# Streamlit App
def main():
    st.title('COVID-19 MLOps Project')

    st.sidebar.title('Prediction Parameters')
    confirmed = st.sidebar.slider('Confirmed Cases', min_value=0, max_value=int(X['Confirmed'].max()), value=int(X['Confirmed'].mean()))
    deaths = st.sidebar.slider('Deaths', min_value=0, max_value=int(X['Deaths'].max()), value=int(X['Deaths'].mean()))

    prediction = predict(confirmed, deaths)

    st.write(f'Predicted Recovered Cases: {int(prediction)}')

if __name__ == '__main__':
    main()
