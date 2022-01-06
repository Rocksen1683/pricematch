from google.cloud import vision
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\rrohi\\OneDrive\\Desktop\\HTN\\pricematch-326403-6a5dbc1d336a.json"

def detect_logos(img):

    """Detects logos in the file."""

    client = vision.ImageAnnotatorClient()

    #with io.open(path, 'rb') as image_file:
    #    content = image_file.read()
    #    print(type(content))

    image = vision.Image(content=img)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations

    logo_list = []

    for logo in logos:
        logo_list.append(logo.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return logo_list[0]


path = "C:\\Users\\rrohi\\OneDrive\\Desktop\\poop.jpg"
#print(detect_logos(path))
