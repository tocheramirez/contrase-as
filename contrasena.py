import random

def generar_contrasena():
    mayusculas=['A','B','D','E','F','G','H','I','J','K','L','M','N','O','C','P','Q','R','S','T','U','V','X','Y','Z']
    minusculas=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    simbolos=['|','@','#','¢','∞','¬','÷','≠','~','_','¡','!','?','$','%','&','/','=']
    numeros=['1','2','3','4','5','6','7','8','9','0']

    caracteres= mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es: '+ contrasena)


if __name__ == '__main__':
    run()
