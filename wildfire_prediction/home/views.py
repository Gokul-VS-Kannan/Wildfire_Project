from django.shortcuts import render
from joblib import load
import numpy as np
import pandas as pd

# load modal and scaler
model = load('ml_model/ml_wildfire_73.joblib')
scaler = load('ml_model/scaler_73.joblib')

# Feature names (must match training data)
FEATURE_NAMES = ["FFMC", "DMC", "DC", "ISI", "temp", "RH", "wind", "rain"]

# Create your views here.
def home(request):
    return render(request,'wildfire.html')

# def make_prediction(request):

    # if request.method == "POST":
    #     FFMC = float(request.POST["fuel_moisture"])
    #     DMC = float(request.POST["duff_moisture"])
    #     DC = float(request.POST["drought"])
    #     ISI = float(request.POST["initial_spread"])
    #     temp = float(request.POST["temperature"])
    #     RH = float(request.POST["humidity"])
    #     wind = float(request.POST["wind_speed"])
    #     rain = float(request.POST["rain"])
        
    #     # Prepare input as a list for prediction
    #     user_input = np.array([[FFMC, DMC, DC, ISI, temp, RH, wind, rain]])

    #     # Scale the input using the trained scaler
    #     user_scaled = scaler.transform(user_input)

    #     # Make prediction using the model
    #     Y_pred = model.predict(user_scaled)

    #     if Y_pred[0] == 1:
    #         prediction = "Fire Likely! There is a high probability of a fire occurring based on the input conditions."

    #     else:
    #         prediction = "No Fire Risk. Conditions are safe, and the likelihood of a fire is low."

    #     return render(request, "wildfire.html", {"prediction": prediction})




def make_prediction(request):
    if request.method == "POST":
        try:
            # Convert input values to float
            input_data = {
                "FFMC" : float(request.POST["fuel_moisture"]),
                "DMC" : float(request.POST["duff_moisture"]),
                "DC" : float(request.POST["drought"]),
                "ISI" : float(request.POST["initial_spread"]),
                "temp" : float(request.POST["temperature"]),
                "RH" : float(request.POST["humidity"]),
                "wind" : float(request.POST["wind_speed"]),
                "rain" : float(request.POST["rain"]),
            }

            # Convert input to DataFrame with correct feature names
            user_df = pd.DataFrame([input_data], columns=FEATURE_NAMES)
            

            # Scale the input using the trained scaler
            user_scaled = scaler.transform(user_df)

            # Make prediction using the trained model
            Y_pred = model.predict(user_scaled)

            # Format prediction result
            if Y_pred[0] == 1:
                prediction = "Fire Likely! High probability of wildfire."
            else:
                prediction = "No Fire Risk. Conditions are safe."

        except Exception as e:
            prediction = f"Error: {str(e)}"

        return render(request, "prediction_result.html", {"prediction": prediction})

    return render(request, "wildfire.html")