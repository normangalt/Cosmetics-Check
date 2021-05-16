'''
Google Cloud Vision API example.
'''

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    import os
    #Set the path to the key instead of the PATH string.
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'PATH'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    print(texts[0].description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    detect_text('example.jpg')
