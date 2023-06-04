from fastapi import FastAPI
from pydantic import BaseModel
import json

from BinFinder import BinFinder
from cv_model.main import main


app = FastAPI()
bin_finder = BinFinder()


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
            'cv_model/output/result_metal_can.jpg.json',
            'cv_model/output/result_plastic_bag.jpg.json',
            'cv_model/output/result_plastic_bottle.jpg.json',
            'cv_model/output/result_ewaste.jpg.json',
            'cv_model/output/result_furniture.jpg.json'
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
    

class NearestBins(BaseModel):
    number: int
    user_coordinates: list
    bin_type: str


@app.post("/get_nearest_bins")
async def get_nearest_bins(nearest_bins: NearestBins):
    try:
        k_nearest_bins = bin_finder.find_k_nearest_bins(nearest_bins.user_coordinates, nearest_bins.number, nearest_bins.bin_type)
        return {
            "data": k_nearest_bins
        }
    except Exception:
        raise Exception
