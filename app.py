from fastapi import FastAPI ,HTTPException,Query,Path



from fastapi.responses import JSONResponse
import pickle
import pandas as pd

from schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERTION

#  import pickl file



app=FastAPI()




# creating a pidantic model to validate incoming data



@app.get('/')
def home():
    return{'messege':'car price prediction api'}

@app.get('/health')
def health_check():
    return{
        'status':'ok',
        'vertion':MODEL_VERTION,
        'model_loaded':model is not None
    }

@app.post('/predict')
def predict_premium(data:UserInput):
    user_input=pd.DataFrame([{
        'Make':data.Make,
        'Year':data.Year,
        'Engine Fuel Type':data.Engine_Fuel_Type,
        'Engine HP':data.Engine_HP,
        'Engine Cylinders':data.Engine_Cylinders,
        'Transmission Type':data.TransmissionType,
        
        'Driven_Wheels':data.Driven_Wheels,
        'Number of Doors':data.Number_of_Doors,
        'Market Category':data.Market_Category,
        'Vehicle Size':data.Vehicle_Size,
        'Vehicle Style':data.Vehicle_Style,
        'highway MPG':data.highway_MPG,
        'city mpg':data.city_mpg,
        'Popularity':data.Popularity



    }])

    try:
   

        prediction = predict_output(user_input)


        return {"predicted_price_is": prediction}
    except Exception as e:

        return JSONResponse(status_code=500,content=str(e))

   







