import smtplib
from email.mime.text import MIMEText
import time
import os
import random

os.system("bash fx.sh")
print("WELCOME CYBER SAVE YOUR TARGET !")
EMAIL = "budiyusf88@gmail.com"
PASSWORD = "murah123"
TO_EMAIL = "support@support.whatsapp.com"

nomor = input("This is unBanned Script !(example: 62xxxxx): ")

# List teks yang mau diacak
BODIES = [
    """salam whatsapp developeri kiminse whatsapp hesabını deaktiv etsin whatsapp proqramında narkotik formasında qadağan olunmuş əşyalar satdığı üçün qadağan olunmuş əşyaların satışının sayını azaltmaq və zərər görməmək üçün həmin şəxsin whatsapp hesabını deaktiv etməyi xahiş edirəm millət və dövlət nəsli, Mark Zukerberqdən kömək və whatsapp tərtibatçılarından xahiş edirəm, qadağan olunmuş əşyaların satıcısının whatsapp nömrəsi :{nomor}-dir mənə kömək etdikləri üçün Mark Zukerberqə və whatsapp tərtibatçısına təşəkkür edirəm.",
    "γεια σας προγραμματιστής whatsapp να απενεργοποιήσει τον λογαριασμό whatsapp κάποιου επειδή έχει πουλήσει απαγορευμένα αντικείμενα με τη μορφή φαρμάκων στην εφαρμογή whatsapp, ζητώ να απενεργοποιήσετε τον λογαριασμό whatsapp αυτού του ατόμου για να μειωθεί ο αριθμός των πωλήσεων των απαγορευμένων αντικειμένων και για να μην προκληθεί ζημιά η γενιά του έθνους και του κράτους, ζητώ βοήθεια από τον Mark Zuckerberg και τους προγραμματιστές του whatsapp,

ο αριθμός whatsapp του πωλητή απαγορευμένων αντικειμένων είναι {nomor}

ευχαριστώ τον Mark Zuckerberg και τον προγραμματιστή του whatsapp που με βοήθησαν",
    "привет разработчику WhatsApp деактивировать чей-то аккаунт WhatsApp, потому что он продавал запрещенные предметы в виде наркотиков в приложении Wh Арр, я прошу деактивировать аккаунт WhatsApp этого человека, чтобы уменьшить количество продаж запрещенных предметов, и чтобы не повредить поколение нации и государства, я прошу помощи у Марка Цукерберга и разработчиков WhatsApp,

WhatsApp номер продавца запрещенных товаров {nomor} спасибо Марку Цукербергу и разработчику WhatsApp за помощь",
    "hello whatsapp developer to deactivate someone's whatsapp account because he has sold prohibited items in the form of drugs in the whatsapp application, I ask to deactivate that person's whatsapp account in order to reduce the number of sales of prohibited items, and so as not to damage the nation and state generation, I ask Mark Zuckerberg for help and whatsapp developers,

the whatsapp number of the seller of prohibited items is {nomor} thanks to Mark Zuckerberg and whatsapp developer for helping me.",
    "ola desenvolvedor do whatsapp para desativar a conta do whatsapp de alguem por ter vendido itens proibidos em forma de drogas no aplicativo whatsapp, peço a desativação da conta do whatsapp dessa pessoa para diminuir o número de vendas de itens proibidos, e para não prejudicar a nação e a geração do estado, peço ajuda a Mark Zuckerberg e aos desenvolvedores do whatsapp,

o número do whatsapp do vendedor de itens proibidos é {nomor} obrigado a Mark Zuckerberg e ao desenvolvedor do whatsapp por me"""
]

JUMLAH_KIRIM = 100
DELAY = 8

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(EMAIL, PASSWORD)

for i in range(JUMLAH_KIRIM):
    BODY = random.choice(BODIES)  # Pilih teks secara acak
    msg = MIMEText(BODY)
    msg['Subject'] = ""
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    server.send_message(msg)
    print(f"[{i+1}] Laporan terkirim untuk nomor {nomor} dengan teks acak")
    time.sleep(DELAY)

server.quit()
print("Proses selesai...")
