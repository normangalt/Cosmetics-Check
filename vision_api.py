'''
Google Cloud Vision API processing.
'''

import os
from google.cloud import vision

class Knot:
    """
    Lightweight, nonpublic
class for storing a singly linked node.
    """
    __slots__ = "_element", "_next"     

    def __init__(self, element = None, next = None):  
        """
        Inititialization of an instance of the object.

        Args:
            element ([object], optional): [value to store in the 'Knot']. Defaults to None.
            next ([object], optional): [object linked next to the one]. Defaults to None.
        """        
        self._element = element         
        self._next = next     

    @property
    def element(self):
        """
        element property for '_element' storage.

        Returns:
            [object]: [the element stored in the _element property].
        """        
        return self._element
    
    @element.setter
    def element(self, value):
        """
        Setter function for element property.

        Args:
            value ([object]): [object to set as a value of the _element property].
        """        
        self._element = value
    
    @property
    def next(self):
        """
        next property for '_next' storage. 

        Returns:
            [object]: [the element stored in the _next property].
        """        
        return self._next
    
    @next.setter
    def next(self, value):
        """
        Setter function for element property.

        Args:
            value ([object]): [object to set as a value of the _next property].
        """        
        self._next = value

class Cream:
    def check_ingredients(self, photo, dataset):
        """
        Check the ingredients.

        Args:
            photo ([type]): [description]
            dataset ([type]): [description]

        Returns:
            [type]: [description]
        """
        ingredients_words = self.find_ingredients(photo)
        ingredients = Knot()
        ingredients_list_head = ingredients
        for ingredient in ingredients_words:
            ingredients.element = dataset.retrieve(ingredient)
            ingredients.next = Knot()
            ingredients = ingredients.next

        return ingredients_list_head

    def find_ingredients(self, path):
        """
        Finds ingredients on a photo.

        Args:
            path ([str]): [path to a photo].

        Returns:
            [list]: [list of words found on the photo].
        """
        detected_text = self.detect_text(path)
        detected_text_words = self.process_text(detected_text)

        return detected_text_words

    @staticmethod
    def detect_text(photo):
        """
        Detects and returns text on a photo.

        Args:
            photo ([str]): [photo in 64bit encoded string].

        Raises:
            Exception: [Exception]
        """
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'simpletextrecognition.json'
        client = vision.ImageAnnotatorClient()

        image = vision.Image(content=photo)

        result = client.text_detection(image=image)

        detected_text = result.text_annotations

        if result.error.message:
            raise Exception(
                '{}\nOoops! Some error occured! Sorry for the troubles.\
Try making a different image, if nothing changes please try again later.'.format(
                    detected_text.error.message))

        return detected_text

    @staticmethod
    def process_text(detected_text):
        """
        Processes texts found on a photo and returns words.

        Args:
            detected_text ([type]): [description]

        Returns:
            [list]: [list of words found on the photo].
        """
        detected_text_strign = detected_text[0].description

        detected_text_words = detected_text_strign.split(',')

        detected_text_words = [word.strip() for word in detected_text_words]

        detected_text_words = [el for word in detected_text_words for el in word.split('\n')]

        return detected_text_words
