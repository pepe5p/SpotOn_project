from googletrans import Translator
import string

translator = Translator(service_urls=['translate.googleapis.com'])


def translate_ingr(ingr: string) -> string:
    translation = translator.translate(ingr, dest='pl')
    return translation.text
