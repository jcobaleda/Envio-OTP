import requests,sys,smtplib,ssl,pywhatkit,datetime,pyautogui as pg, webbrowser as web,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#variables
dato1=hash(sys.argv[1])
dato2=hash(sys.argv[2])
users= 'kobaledajona@gmail.com'
password= 'jonathan19naruto'
conexionSegura=ssl.create_default_context()
#revisar conexion a internet
def hayconexion():
    try:
        hay = requests.get('https://www.google.com',timeout=60)
    except:
        hay = False
    return hay
#si tiene conexion
if hayconexion(): 
    
#vista del Correo
    destinatario = sys.argv[1]
    asunto = 'Codigo OTP'
    mensaje = MIMEMultipart()
    mensaje["Subject"]=asunto
    mensaje["From"]=users
    mensaje["To"]=destinatario
    html =f"""
    <html>
    <body>
        Este es tu codigo <b> {dato1} </b>
    </body>
    </html>
    """
    convert_html = MIMEText(html,"html")
    mensaje.attach(convert_html)
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=conexionSegura) as smtp:
    smtp.login(users,password) 
    smtp.sendmail(users, destinatario, mensaje.as_string()) 
    print ("Correo Enviado")
#Envio de Whatsapp
web.open("https://web.whatsapp.com/send?phone="+sys.argv[2]+"&text="+" Tu Codigo es: "+str(dato2))
first = True
if first:
        time.sleep(5)
        first=False
width,height = pg.size()
pg.click(width/2,height/2)
time.sleep(3)
pg.press('enter')
time.sleep(6)
pg.hotkey('ctrl', 'w')
print("Mensaje Enviado")
