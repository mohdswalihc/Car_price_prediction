import pickle
import pandas as pd

with open("model/car_price_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

# ML flow

MODEL_VERTION='1.0.0'


def predict_output(user_input:dict):

    input_df=pd.DataFrame(user_input)

    output=float(model.predict(input_df)[0])

    return output