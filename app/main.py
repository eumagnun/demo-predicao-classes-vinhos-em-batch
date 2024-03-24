import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist


app = FastAPI(title="Previsão classe de vinhos")

#Objeto a ser usado como input. Uma lista de vinhos
class Wine(BaseModel):
    instances: List[conlist(item_type=float, min_length=13, max_length=13)]


@app.on_event("startup")
def load_clf():
    # carregar modelo
    with open("../app/model.pkl", "rb") as file:
        global clf
        clf = pickle.load(file)


# Endpoint default com indicação de onde encontrar documentação da API
@app.get("/")
def home():
    return "ver OAS em /docs"

# Endpoint para fins de healthcheck 
# O Vertex requer um endpoint de healthcheck)
@app.get("/status")
def status():
    return "ok"

# Enpoint para predição
# O Vertex requer que a resposta contenha a chave 'predictions'
@app.post("/predict")
def predict(wine: Wine):
    instances = wine.instances
    np_instances = np.array(instances)
    pred = clf.predict(np_instances).tolist()
    return {"predictions": pred}
