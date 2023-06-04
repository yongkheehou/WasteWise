from fastapi import FastAPI
from pydantic import BaseModel
import json

from BinFinder import BinFinder
from cv_model.main import main


app = FastAPI()
bin_finder = BinFinder()


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
