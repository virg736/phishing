# Phishing

#  Comment se protéger du phishing – Les bonnes pratiques

## Sommaire

1. [Introduction](#introduction)
2. [Bonnes pratiques anti-phishing + outils de vérification](#bonnes-pratiques-anti-phishing--outils-de-vérification)
3. [Pour aller plus loin](#pour-aller-plus-loin)
4. [Sécurité des macros – Pourquoi un fichier ne suffit pas](#sécurité-des-macros--pourquoi-un-fichier-ne-suffit-pas)
5. [Ce que cela signifie concrètement](#ce-que-cela-signifie-concrètement)
6. [Ce que dit Microsoft](#ce-que-dit-microsoft)
7. [Résumé technique](#résumé-technique)
8. [Mentions importantes](#mentions-importantes)
9. [Analyse d’un en-tête d’e-mail (headers)](#analyse-dun-en-tete-demail-headers)

---

## Introduction

Le **phishing** (ou hameçonnage) est l’une des techniques les plus répandues parmi les cybercriminels. Cela consiste à tromper la victime pour lui faire **divulguer des informations sensibles** (mots de passe, données bancaires, accès à un compte, etc.).

Ce projet vise à **sensibiliser** et à fournir de **bonnes pratiques concrètes**, accompagnées de **liens vers des outils en ligne** pour analyser les e-mails ou fichiers suspects.

---

##  Bonnes pratiques anti-phishing et outils de vérification

1. **Vérifier l’adresse e-mail réelle de l’expéditeur**
🔗 [MailHeader Analyzer (Google)](https://toolbox.googleapps.com/apps/messageheader/)
🔗 [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)

2. **Survoler les liens avec la souris avant de cliquer**
🔗 [VirusTotal – Scanner d’URL](https://www.virustotal.com/gui/home/url)
🔗 [URLScan.io](https://urlscan.io/)

3. **Analyser les pièces jointes avant de les ouvrir**
🔗 [VirusTotal – Analyse de fichier](https://www.virustotal.com/gui/home/upload)

4. **Afficher et lire les en-têtes d’un e-mail (headers)**
🔗 [Google Header Tool](https://toolbox.googleapps.com/apps/messageheader/)
 À examiner : `From`, `Reply-To`, `Return-Path`, `Received`, `SPF`, `DKIM`

5. **Vérifier si un site ou lien est signalé comme dangereux**
🔗 [Google Safe Browsing](https://transparencyreport.google.com/safe-browsing/search)
🔗 [PhishTank](https://phishtank.org/)

6. **Rechercher à qui appartient un domaine (Whois)**
🔗 [Who.is](https://who.is/)
🔗 [SecurityTrails](https://securitytrails.com/)

7. **Mettre à jour son antivirus et activer les protections antiphishing**
✔️ Activer SmartScreen (Windows)
✔️ Activer les protections avancées dans Gmail / Outlook

8. **Ne jamais cliquer sur un lien inconnu dans un e-mail**
✍ Tapez manuellement l’adresse du site dans votre navigateur.

---

##  Pour en savoir plus sur le phishing et les moyens de s 'en protéger :

- [Cybermalveillance.gouv.fr – Hameçonnage](https://www.cybermalveillance.gouv.fr/tous-nos-contenus/fiches-reflexes/hameconnage-phishing)
- [CNIL – Reconnaître un e-mail frauduleux](https://www.cnil.fr/fr/cybersecurite-comment-reconnaitre-un-message-frauduleux)

---

##  Sécurité des macros – Pourquoi un fichier ne suffit pas

Depuis plusieurs années (et renforcée en 2022), **Microsoft Office (Excel, Word)** désactive automatiquement les macros pour tout fichier **téléchargé depuis Internet ou reçu par e-mail**.

> 📎 Source : Microsoft – Documentation officielle
> 🔗 https://learn.microsoft.com/fr-fr/deployoffice/security/internet-macros-blocked

---

###  Ce que cela signifie concrètement

- Tant que **l'utilisateur n’active pas les macros**, **aucun code malveillant ne s’exécute**.
-  C’est **uniquement après avoir cliqué sur “Activer le contenu”** que la macro est lancée.
-  À partir de ce moment-là, le fichier peut :
- Se connecter à un **serveur distant**
- Télécharger un **payload** (malware)
- L’exécuter **discrètement**

 C’est une méthode classique utilisée dans les campagnes de phishing avec **dropper + macro VBA**.

----

Private Sub Workbook_Open()

' Étape 1 : Piège
MsgBox "🧩 Étape 1 – Le piège : réception d’un e-mail suspect" & vbCrLf & _
"Objet : Facture urgente - client important" & vbCrLf & _
"Expéditeur : facturation@exemple-client.fr" & vbCrLf & _
"Pièce jointe : Facture_URGENTE.xlsm" & vbCrLf & vbCrLf & _
"Message : Bonjour, merci de traiter cette facture aujourd’hui même pour éviter une pénalité.", _
vbInformation, "Simulation phishing - Étape 1"

' Étape 2 : Ouverture
MsgBox " Étape 2 – L’utilisateur ouvre le fichier Excel." & vbCrLf & _
"Il voit une alerte : 'Le contenu a été désactivé pour votre sécurité'." & vbCrLf & _
"Mais il clique sur “Activer le contenu”.", _
vbInformation, "Simulation phishing - Étape 2"

' Étape 3 : Macro active
MsgBox " Étape 3 – Exécution de la macro malveillante." & vbCrLf & _
"✅ Connexion à un serveur distant." & vbCrLf & _
"✅ Téléchargement d’un payload." & vbCrLf & _
"✅ Lancement silencieux du malware.", _
vbExclamation, "Simulation phishing - Étape 3"

' Simule l'exécution d'un faux "payload"
Shell "notepad.exe", vbNormalFocus ' innocente et visible

' Étape 4 : Propagation
MsgBox "Étape 4 – L’attaque se propage." & vbCrLf & _
" Extraction de fichiers." & vbCrLf & _
" Envoi de données sensibles." & vbCrLf & _
"🔒 Chiffrement de fichiers (ransomware)." & vbCrLf & _
"  Propagation sur le réseau.", _
vbCritical, "Simulation phishing - Étape 4"

' Étape 5 : Conséquences
MsgBox " Étape 5 – Constat de l’incident." & vbCrLf & _
" Fichiers chiffrés" & vbCrLf & _
" Ralentissements suspects" & vbCrLf & _
" Demande de rançon", _
vbCritical, "Simulation phishing - Étape 5"

' Leçon
MsgBox "🛡️ Leçon : cette attaque aurait pu être évitée si..." & vbCrLf & _
"- L’utilisateur avait reconnu le phishing." & vbCrLf & _
"- Il n’avait pas activé la macro." & vbCrLf & _
"- L’antivirus avait bloqué le fichier." & vbCrLf & _
"- Les macros étaient désactivées par défaut.", _
vbInformation, "Fin de la simulation"

End Sub

---

<pre lang="markdown">
```text
📧 L’attaquant joint le fichier Excel contenant une macro malveillante dans un e-mail piégé.
Il utilise un objet accrocheur et un contenu pressant pour pousser la victime à ouvrir le fichier et à cliquer sur "Activer le contenu".
Une fois cela fait, le code malveillant intégré s’exécute automatiquement.

📌 À retenir :
Les hackers l’utilisent encore dans des environnements mal protégés.
Mais Microsoft bloque désormais les macros par défaut pour les fichiers venant d’Internet (Office 2022+, M365).
Les attaquants contournent cette protection en hébergeant les fichiers sur des serveurs internes compromis,
ou en utilisant des documents Word (.docm) ou PowerPoint avec macros.

Conclusion : cette méthode fonctionne encore si l’utilisateur est piégé et active le contenu manuellement.
```
</pre>



---

###  Ce que dit Microsoft

Un fichier Excel ou Word contenant une macro **ne présente aucun danger** tant que l’utilisateur **n’a pas activé les macros manuellement**.

Par défaut, **Microsoft Office bloque automatiquement l'exécution des macros** provenant d'Internet ou d'une pièce jointe.

> 📎 “Par défaut, les macros dans les fichiers provenant d’Internet sont désormais bloquées dans Office.”
> 🔗 Source officielle Microsoft :
> https://learn.microsoft.com/fr-fr/deployoffice/security/internet-macros-blocked

---

### Résumé technique

- Le simple fait ouvrir un fichier ne suffit pas à exécuter du code malveillant.
- **C’est n'est qu'après avoir cliqué sur “Activer le contenu”** que la macro peut s’exécuter.
- Une fois activée, elle peut :
- Contacter un serveur distant
- Télécharger un virus (payload)
- L’exécuter en silence sur l’ordinateur

Ce type d’attaque est une méthode classique de **dropper** utilisée dans les campagnes de phishing.

---

## Mentions importantes

Les outils et ressources externes mentionnés dans ce projet (ex. : VirusTotal, Google Header Analyzer, PhishTank…) sont tous **publics, légaux** et utilisés dans un **but exclusivement pédagogique**.

Aucune de ces plateformes n’est modifiée ou détournée.
Les liens sont fournis uniquement pour **sensibiliser aux bonnes pratiques** en matière de cybersécurité (analyse d’e-mails, de liens, de fichiers…).

> Ce projet n’encourage en aucun cas l’usage de techniques offensives sans autorisation légale préalable.

 Pour plus d'informations sur l'utilisation de liens à des fins pédagogiques :
- [Legifrance – Code de la propriété intellectuelle, Article L122-5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278917/)
- [CNIL – Sensibilisation à la cybersécurité](https://www.cnil.fr)

---

###  Analyse d'un en-tête d'e-mail (headers)

| **Élément** | **Ce qu’il faut analyser** |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **From** | Est-ce l’adresse attendue ? (ex. : `support@banque.fr`) |
| **Reply-To** | Est-ce identique à l’adresse "From" ? Si c’est une autre adresse (ex. : `offre-banque@protonmail.com`), cela peut être suspect. |
| **Return-Path** | Adresse réelle de retour. Peut différer du "From" en cas de spoofing. |
| **Received** | Liste des serveurs par lesquels est passé l’e-mail. Une origine inattendue (ex. : serveur basé à l’étranger, VPN, etc.) est un signal d’alerte. |
| **DKIM / SPF / DMARC** | Signatures utilisées pour vérifier que le domaine de l’expéditeur est autorisé à envoyer l’e-mail. Si elles sont absentes ou échouées, cela indique un danger. |

---
