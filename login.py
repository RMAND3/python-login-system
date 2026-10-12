usuario = ""
contrasena_correcta = "diego123"
contador = 0

while usuario == "":
    usuario = input("Cual es tu usuario?").strip()

while contador < 3:
    contrasena = input("Cual es tu contraseña?").strip()
    if contrasena == contrasena_correcta:
        print(f'Bienvenido {usuario.capitalize()}')
        break
    else:
        print("Contraseña incorrecta")
        contador += 1

if contador == 3:
    print("Has excedido el número de intentos")

