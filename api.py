'''
Google Cloud Vision API example.
'''

import io
import os
from google.cloud import vision

class Knot:
    """Lightweight, nonpublic
    class for storing a singly linked node.
    """

    __slots__ = "_element", "_next"     

    def __init__(self, element = None, next = None):  
        self._element = element         
        self._next = next     

    @property
    def element(self):
        return self._element
    
    @element.setter
    def element(self, value):
        self._element = value
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value

class Cream:
    def __init__(self):
        '''
        The initialization of an instance of the object.
        '''
        self.ingrediets = Knot() 
        self.damage_rate = self.callculate_damate_rate()

    def check_ingredients(self, path, data):
        '''
        Forms a list of ingredients in the 'cream'.
        '''
        ingredients_words = self.detect_ingredients(path)
        ingredients = self.ingrediets
        for ingredient in ingredients_words:
            entry = (Ingredient())
            if data.is_find(ingredient):
                entry = Ingredient(data.retrieve(ingredient))
            ingredients.next = Knot()
            ingredients = ingredients.next

    def find_ingredients(self, path):
        '''
        Finds the ingredients of the file on the given path.
        '''
        detected_text = self.detect_text(path)
        detected_text_words = self.process_text(detected_text)
        return detected_text_words

    def callculate_damate_rate(self):
        pass

    @staticmethod
    def detect_text(photo):
        """Detects text in the file."""

        os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'/Users/ya_tvoy_bro/Documents/python_projects/testtask_MacPaw/MacPaw-testtask/CosmeticsBot/simpletextrecognition.json'
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
        '''
        Processes retrieved container with text.
        '''
        detected_text_strign = detected_text[0].description

        detected_text_words = detected_text_strign.split()

        return detected_text_words

class Ingredient:
    __slots__ = ('name', 'damage_rate', 'properties')
    def check(self, entry):
        self.name = entry['name']
        self.damage_rate = entry['Damage_rate']
        self.properties = entry['Properties']
