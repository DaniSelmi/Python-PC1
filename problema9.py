texto = input("Ingrese un texto: ")

texto_s = ''

for letra in texto:
    if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U":
        texto_s += ''
        continue
    texto_s += letra

print(texto_s)