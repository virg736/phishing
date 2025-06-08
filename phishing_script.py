import email
from email import policy
import sys

def analyser_eml(fichier):
with open(fichier, 'rb') as f:
msg = email.message_from_binary_file(f, policy=policy.default)

print("\nAnalyse de l'e-mail :\n")
print("From :", msg.get('From'))
print("Reply-To :", msg.get('Reply-To'))
print("Return-Path:", msg.get('Return-Path'))
print("Received :", msg.get_all('Received'))

print("\nContenu de l'e-mail :\n")
if msg.is_multipart():
for part in msg.walk():
content_type = part.get_content_type()
if content_type == "text/plain":
print(part.get_payload(decode=True).decode(errors="ignore"))
else:
print(msg.get_payload(decode=True).decode(errors="ignore"))

if __name__ == "__main__":
if len(sys.argv) < 2:
print("Usage : python phishing_script.py email.eml")
else:
analyser_eml(sys.argv[1])

