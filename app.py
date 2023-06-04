from fastapi import FastAPI
from cv_model.main import main
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "I'm Alive!"}

@app.post("/get_predictions")
async def get_predictions():
    try:
        main(tag_input='./cv_model/raw_images', tag_output="./cv_model/output")
        
        f = open('./cv_model/output/result_metal_can.jpg.json')
        data = json.load(f)
        f.close()
        
        if data['result']['tags'][0]["tag"]["en"] == "container":
            return "metal"
        
        elif data['result']['tags'][0]["tag"]["en"] == "bottle":
            return "plastic"
        
        elif data['result']['tags'][0]["tag"]["en"] == "plastic bag":
            return "plastic bag" 
        
        else:
            return "Type of waste is unknown"
        
    except Exception:
        raise Exception
