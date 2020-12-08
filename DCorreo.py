#!/usr/bin/env python3
#Nombre: César Alejandro Rodríguez Pérez - Matricula: 1734223.
class mail():
    def __init__(self):
        try:
            print("Iniciando sesion...")
            import smtplib, ssl
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            
            print("IMPORTANTE: este script envia un meme, aviso por si se quiere hacer una prueva de envio y así evitar problemas.")
            sender_email = input("Ingrese su correo: ")
            password = input("Ingrese su contraseña: ")
            receiver_email = input("Ingrese un destinatario: ")
            

            print("Sesion iniciada!!")

            message = MIMEMultipart("alternative")
            message["Subject"] = input("Ingrese un asunto para el correo: ")
            message["From"] = sender_email
            message["To"] = receiver_email

            
            text="""
            Buenas Buenas, esto es un correo enviado como evidencia de un PIA del grupo: 064 - Materia: PC
            """
            html = """
            <img id="detailed-item-image-container" src="https://images7.memedroid.com/images/UPLOADED871/5e0d847fb7f4e.jpeg" class="img-responsive" alt="Lo vi en Facebook y me dio gracia - meme">
            """

            
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            
            message.attach(part1)
            message.attach(part2)

            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
            print("Mensaje con meme eviado!!")
            print("Adios!!")
        except:
            print("Ah ocurrido un error, favor de ejecutar el script nuevamente")
