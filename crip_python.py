import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime

load_dotenv()
account_sid = os.getenv("SID")
auth_token  = os.getenv("TOKEN")

frases = {
    1:  "Hoy es un buen día para ser feliz.",
    2:  "Cada mañana es una página en blanco, escríbela bien.",
    3:  "No necesitas tenerlo todo claro, solo seguir.",
    4:  "Eres más fuerte de lo que crees, siempre.",
    5:  "El día de hoy no se repite, aprovéchalo.",
    6:  "Respira. Todo llega a su tiempo.",
    7:  "Hay algo hermoso esperándote hoy, aunque no lo veas aún.",
    8:  "No compitas con nadie, solo con quien eras ayer.",
    9:  "Los días difíciles también pasan.",
    10: "Hoy puede ser el día que lo cambia todo.",
    11: "Confía en el proceso, aunque no veas el resultado.",
    12: "Pequeños pasos también son avance.",
    13: "No tienes que ser perfecta, solo auténtica.",
    14: "El universo conspira a favor de quienes no se rinden.",
    15: "Hoy vale la pena intentarlo.",
    16: "Tu energía es tuya, cuídala.",
    17: "No todo tiene que tener sentido hoy.",
    18: "Eres exactamente donde necesitas estar.",
    19: "Date crédito por todo lo que ya superaste.",
    20: "Hoy es un buen día para ser amable contigo misma.",
    21: "Lo que buscas también te está buscando.",
    22: "No subestimes el poder de un buen día.",
    23: "Confía en ti, aunque nadie más lo haga todavía.",
    24: "Cada día trae su propia luz, búscala.",
    25: "No tienes que cargar todo sola.",
    26: "El mejor momento para empezar siempre es hoy.",
    27: "Eres suficiente, exactamente como eres.",
    28: "Hoy, un paso. Mañana, otro. Así se llega lejos.",
    29: "Las cosas buenas toman tiempo, y tú vales ese tiempo.",
    30: "Hoy es tuyo, hazlo significativo.",
    31: "Hoy es un buen día para ser feliz.",  # por si el mes tiene 31 días
}


dia = datetime.now().day

mensaje = frases.get(dia, "Hoy es un buen día para ser feliz.")

client = Client(account_sid, auth_token)
client.messages.create(
    from_= "whatsapp:+14155238886",
    to=    "whatsapp:+50583776225",
    body=  mensaje
)
    
print(f"Mensaje del día {dia} enviado: {mensaje}")
