## Run the following commands to create the virtual environment in this directory
pip3 install virtualenv==20.23.0
python -m venv .

## Run the following command to activate the virtual environment
venv/Scripts/activate

## Run the following command to install the required dependencies
pip3 install -r requirements.txt

## Create a .env file 
add your IMAGGA_API_KEY and IMAGGA_API_SECRET into the .env file

## Run the following command to execute the code
python ./cv_model/main.py ./cv_model/raw_images ./cv_model/output --language=en --verbose=0 --merged-output=0 --include-colors=0
