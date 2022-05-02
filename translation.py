from googletrans import Translator


translator = Translator(service_urls=['translate.googleapis.com'])


def translate_ingr(ingr: str) -> str:
    """
    :param ingr: ingredient
    :return: ingredient translated to polish
    """
    translation = translator.translate(ingr, dest='pl')
    return translation.text
