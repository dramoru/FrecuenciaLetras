import string 

with open('quijote.txt', encoding="utf-8") as archivo:
    texto = archivo.read().lower()

frec_caracteres: dict[str, int] = {}

for caracter in texto:
    if caracter in frec_caracteres:
        frec_caracteres[caracter] += 1
    else:
        frec_caracteres[caracter] = 1

frec_letras: dict[str, int] = {}

for letra in string.ascii_lowercase:
    frec_letras[letra] = frec_caracteres[letra]

for caracter, frecuencia in frec_letras.items():
    print(repr(caracter) + " : " + str(frecuencia))

