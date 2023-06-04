## Run the following commands to create the virtual environment in this directory
- `pip3 install virtualenv==20.23.0`
- `python -m venv .`

## Run the following command to activate the virtual environment
- `venv/Scripts/activate`

## Run the following command to install the required dependencies
- `pip3 install -r requirements.txt`

## Create a .env file 
- add your IMAGGA_API_KEY and IMAGGA_API_SECRET into the .env file

## Run the following command to execute the cv model code
- `python ./cv_model/main.py ./cv_model/raw_images ./cv_model/output --language=en --verbose=0 --merged-output=0 --include-colors=0`

## Run the following command to start the app
- `uvicorn app:app --host 0.0.0.0 --port 8000`





# Instructions for BinFinder


## 1. Configure

Edit `BinFinder\config.py`
## 2. Pre-Process data

Gather data of recycling bin locations in CSV files with the following headers

> name,address,description,postal_code,lat,lon

Edit the variable to the csv file path in the file `generate_data.py`

Run the Following Commands

- `cd BinFinder`
- `py generate_data.py`

A new csv file should be generated in the data folder.

## 3. Final Config

Edit the variable in `BinFinder\BinFinder.py` to point to the newly generated csv file 
