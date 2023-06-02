'''
Translator functions between English to French and French to English
'''
from deep_translator import MyMemoryTranslator

def english_to_french(en_text):
    '''
    Translate the provided english text and returns it in french
    '''
    fr_text = MyMemoryTranslator(source ='english',target='french').translate(en_text)
    return fr_text

def french_to_english(fr_text):
    '''
    Translate the provided french text and returns it in english
    '''
    en_text = MyMemoryTranslator(source = 'french', target = 'english').translate(fr_text)
    return en_text
