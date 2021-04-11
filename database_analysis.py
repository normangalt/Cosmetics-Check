'''Lab10 Task2'''
import pandas as pd
import re

def read_data(path_to_file):
    '''
    reads the file and returns the DataFrame object, without additional data processing
    '''
    path_to_file = 'CDPH.csv'
    df = pd.read_csv(path_to_file)
    return df


def bad_ingr_list(df):
    unique_ingr = df['Ingredient Name'].unique()
    return unique_ingr

def clean_num(ingr: str):
    """removes numbers from string"""
    ingr_lst = ingr.split()
    cleaned_list = []
    for _, el in enumerate(ingr_lst):
        if not re.fullmatch(r"\d*(\-\d*){2}", el) and not re.fullmatch(r"\(\d*(\-\d*){2}\)", el):
            cleaned_list.append(el)
    return ' '.join(cleaned_list)

def clean_list(ingr_list):
    """..."""
    for indx, el in enumerate(ingr_list):
        ingr_list[indx] = clean_num(el)
    return ingr_list


df = read_data('CDPH.csv')
bad_list = clean_list(bad_ingr_list(df))

def find_bad(input_ingr, bad_list):
    for _, el in enumerate(bad_list):
        if re.fullmatch(input_ingr, el):
            return f'found harmful ingridient {el}'
    return f'no {el} found'

if __name__ == '__main__':
    df = read_data('CDPH.csv')
    bad_list = clean_list(bad_ingr_list(df))
    print(bad_list)
    print(find_bad('Carbon-black extracts', bad_list))