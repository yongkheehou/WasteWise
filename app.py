from fastapi import FastAPI
from cv_model.main import main
import json

app = FastAPI()

counter = -1

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
        
        counter += 1
        
        if data['result']['tags'][counter]["tag"]["en"] == "container":
            return "metal"
        
        elif data['result']['tags'][counter]["tag"]["en"] in ("bottle", "plastic bag"):
            return "plastic"
        
        elif data['result']['tags'][counter]["tag"]["en"] == "rubbish":
            return "e-waste"
        
        elif data['result']['tags'][counter]["tag"]["en"] == "studio couch":
            return "second hand furniture"  
        
        else:
            return "Type of waste is unknown"
        
    except Exception:
        raise Exception
