"""
GERADOR DE SENHAS

"""
chave = input("Digite a base da sua senha: ")

senha = " "

for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "%"
    elif letra in "Ee": senha = senha + "14"
    elif letra in "Ff": senha = senha + "15"
    elif letra in "Gg": senha = senha + "$"
    elif letra in "Hh": senha = senha + "#"
    elif letra in "Ii": senha = senha + "18"
    elif letra in "Jj": senha = senha + "@"
    elif letra in "Kk": senha = senha + "20"
    elif letra in "Ll": senha = senha + "-"
    elif letra in "Mm": senha = senha + "22"
    elif letra in "Nn": senha = senha + "*"
    elif letra in "Oo": senha = senha + "24"
    elif letra in "Pp": senha = senha + "50"
    elif letra in "Qq": senha = senha + "51"
    elif letra in "Rr": senha = senha + "52"
    elif letra in "Ss": senha = senha + "&"
    elif letra in "Tt": senha = senha + "54"
    elif letra in "Uu": senha = senha + "55"
    elif letra in "Vv": senha = senha + "56"
    elif letra in "Xx": senha = senha + "57"
    elif letra in "Yy": senha = senha + "58"
    elif letra in "Ww": senha = senha + "59"
    else: senha = senha + letra
print(senha)

