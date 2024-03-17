import pandas as pd
from pandas import DataFrame

def model_predict(data, model):
    # Get model predictions
    prediction_prospect = model.predict(data[data['bought_toon']==False].drop('bought_toon', axis=1))
    prediction_probability = model.predict_proba(data[data['bought_toon']==False].drop('bought_toon', axis=1))
    
    prospects = DataFrame(prediction_prospect, columns=['possible_prospect']) 
    chances = DataFrame(prediction_probability, columns=['reject_toon_chance','buy_toon_chance'])
    list_for_marketing = pd.concat([ 
        prospects.reset_index(drop=True),
        chances.reset_index(drop=True)],
        axis=1)
    return list_for_marketing
