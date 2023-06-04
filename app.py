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
        
        global counter 
        
        counter += 1
        
        files = [
            'cv_model\output\result_metal_can.jpg.json',
            'cv_model\output\result_plastic_bag.jpg.json',
            'cv_model\output\result_plastic_bottle.jpg.json',
            'cv_model\output\result_ewaste.jpg.json',
            'cv_model\output\result_furniture.jpg.json'
        ]
        
        f = open(f'{files[counter]}')
        data = json.load(f)
        f.close()
        
        if data['result']['tags'][counter]["tag"]["en"] == "container":
            return "recycling"
        
        elif data['result']['tags'][counter]["tag"]["en"] in ("bottle", "plastic bag"):
            return "recycling"
        
        elif data['result']['tags'][counter]["tag"]["en"] == "rubbish":
            return "e_waste"
        
        elif data['result']['tags'][counter]["tag"]["en"] == "studio couch":
            return "second_hand"  
        
        else:
            return "Type of waste is unknown"
        
    except Exception:
        raise Exception
