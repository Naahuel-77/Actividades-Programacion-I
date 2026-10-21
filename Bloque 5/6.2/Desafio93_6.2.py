traducciones = {
    "hello": {"es": "hola", "fr": "bonjour", "it": "ciao", "de": "hallo"},
    "thank you": {"es": "gracias", "fr": "merci", "it": "grazie", "de": "danke"},
    "water": {"es": "agua", "fr": "eau", "it": "acqua", "de": "wasser"},
    "book": {"es": "libro", "fr": "livre", "it": "libro", "de": "buch"},
    "cat": {"es": "gato", "fr": "chat", "it": "gatto"},
}


def traducir(palabra, idiomas):
    palabra = palabra.lower()
    if palabra not in traducciones:
        print(f"La palabra '{palabra}' no está en el diccionario")
        return

    print(f"Traducciones de '{palabra}':")
    for idioma in idiomas:
        traduccion = traducciones[palabra].get(idioma)
        if traduccion:
            print(f"- {idioma}: {traduccion}")
        else:
            print(f"- {idioma}: no se encontró traducción")


traducir("hello", ["es", "fr", "it", "de"])
traducir("cat", ["es", "de", "pt"])
traducir("house", ["es"])