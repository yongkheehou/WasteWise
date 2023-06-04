import os
import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('IMAGGA_API_KEY')
API_SECRET = os.environ.get('IMAGGA_API_SECRET')

ENDPOINT = 'https://api.imagga.com/v2'

FILE_TYPES = ['png', 'jpg', 'jpeg', 'gif']


class ArgumentException(Exception):
    pass

if API_KEY == 'YOUR_API_KEY' or  \
        API_SECRET == 'YOUR_API_SECRET':
    raise ArgumentException('You haven\'t set your API credentials. '
                            'Edit the script and set them.')

auth = HTTPBasicAuth(API_KEY, API_SECRET)


def upload_image(image_path):
    if not os.path.isfile(image_path):
        raise ArgumentException('Invalid image path')

    # Open the desired file
    with open(image_path, 'rb') as image_file:
        filename = image_file.name

        # Upload the multipart-encoded image with a POST
        # request to the /uploads endpoint
        content_response = requests.post(
            '%s/uploads' % ENDPOINT,
            auth=auth,
            files={'image': image_file})
        
        uploaded_file = content_response.json()['result']

        # Get the upload id of the uploaded file
        upload_id = uploaded_file['upload_id']

    return upload_id


def tag_image(image, upload_id=False, verbose=False, language='en'):
    tagging_query = {
        'image_upload_id' if upload_id else 'image_url': image,
        'verbose': verbose,
        'language': language
    }
    tagging_response = requests.get(
        '%s/tags' % ENDPOINT,
        auth=auth,
        params=tagging_query)

    return tagging_response.json()


def extract_colors(image, upload_id=False):
    colors_query = {
        'image_upload_id' if upload_id else 'image_url': image,
    }

    colors_response = requests.get(
        '%s/colors' % ENDPOINT,
        auth=auth,
        params=colors_query)

    return colors_response.json()


def main(tag_input, tag_output, images, language="en", verbose=0, merged_output=0, include_colors=0):

    print('Tagging images started')

    results = {}
    if os.path.isdir(tag_input):
        # images = [filename for filename in os.listdir(tag_input)
        #           if os.path.isfile(os.path.join(tag_input, filename)) and
        #           filename.split('.')[-1].lower() in FILE_TYPES]
        
        images_count = len(images)
        for iterator, image_file in enumerate(images):
            image_path = os.path.join(tag_input, image_file)
            print('[%s / %s] %s uploading' %
                  (iterator + 1, images_count, image_path))
            try:
                upload_id = upload_image(image_path)
            except requests.exceptions.JSONDecodeError:
                print('API image upload response error %s' % image_path)
                continue
            except Exception:
                continue

            try:            
                tag_result = tag_image(upload_id, True, verbose, language)
            except requests.exceptions.JSONDecodeError:
                print('API response error with image %s' % image_path)
                continue
			
            if not include_colors:
                results[image_file] = tag_result
            else:
                colors_result = extract_colors(upload_id, True)
                results[image_file] = {
                    'tagging': tag_result,
                    'colors': colors_result
                }
            print('[%s / %s] %s tagged' %
                  (iterator + 1, images_count, image_path))
    else:
        raise ArgumentException(
            'The input directory does not exist: %s' % tag_input)

    if not os.path.exists(tag_output):
        os.makedirs(tag_output)
    elif not os.path.isdir(tag_output):
        raise ArgumentException(
            'The output folder must be a directory')

    if merged_output:
        with open(
            os.path.join(tag_output, 'results.json'),
                'wb') as results_file:
            results_file.write(
                json.dumps(
                    results, ensure_ascii=False, indent=4).encode('utf-8'))
    else:
        for image, result in results.items():
            with open(
                os.path.join(tag_output, 'result_%s.json' % image),
                    'wb') as results_file:
                results_file.write(
                    json.dumps(
                        result, ensure_ascii=False, indent=4).encode('utf-8'))

    print('Done')

if __name__=="__main__":
    main(tag_input="./cv_model/raw_images", tag_output="./cv_model/output")
