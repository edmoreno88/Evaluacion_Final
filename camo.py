# se traen los paquetes que se instalan para la ejecucion del programa
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import smtplib
from PIL import ImageGrab

#nombre del asistente virtual
name= 'camo'
#variable para reconocernos y variable para iniciar el pyttsx3
listener = sr.Recognizer()

engine = pyttsx3.init()

#traer un listado de las voces y seteamos la propiedad voice en la posicion 1 y como tiene varios atributos solo 
#traemos el ID
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Definimos el metodo talk el cual pasa un texto ocupando el engine para que diga el texto 
def talk(text):
    engine.say(text)
    engine.runAndWait()

#hacemos una funcion listen para la escucha desde el microfono si hay un problema lo ignora con el except
#ponemos una impresion en consola para el escuchando, variable rec para la api de google y pasmos el voice
#llamaos el metodo lower para hacer una condicion el cual el nombre de el asistente pase por el microfono
#entra y reasgamos la variable 
def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

#declarmamos la funcion run donde cuando se diga reproduce va a abrir el paquete whatkit y al metodo playnyt
#para que abra un video de youtube
def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)

# luego realizamos la funcion para cuando se diga hora traiga del datatima la hora actual del sistema y con el talk
# nos diga son las x horas
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("son las "+hora)

# luego realizamos la funcion para cuando se diga busca haga una consulta con la api wikipedia de acuerdo a lo que
# le escribamos en consola en el text
# luego imprime el resultado de lo buscado 
    elif 'busca' in rec:
        text= input("buscar:\n")
        wikipedia.set_lang("es")
        info= wikipedia.summary(text)
        print("\nWikipedia: ",info)

# luego realizamos la funcion para cuando se diga abrir google con el webbrowser.open nos abra la pagina de google
#en el equipo y reproduzca con el talk 
    elif 'abrir google' in rec:
        webbrowser.open("https://www.google.com")
        talk("abriendo google")

# luego realizamos la funcion para cuando se diga enviar correo indicamos:
    elif 'enviar correo' in rec:
        remitente = "edwardm8910@gmail.com"
        recibido = "edwardm8910@gmail.com"
        password = input(str("ingrese su contraseña: "))
        mensaje = "hola, prueba de correo electronico"

        server = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
        server.starttls()
        server.login(remitente, password)
        print("ingreso correcto")
        server.sendmail(remitente, recibido, mensaje)
        print("el correo a sido enviado", recibido)

# luego realizamos la funcion para cuando se diga tomar foto con el imagengrab tome un screenshot de la pantalla y
#se guarde en un archivo de nombre foto
    elif 'tomar foto' in rec:
        im = ImageGrab.grab()
        im.save("foto.jpg")
        talk("se ha tomado una foto a su pantalla")

    else:
        talk("vuelve a intentarlo")  

while True:
    run()