[![Tests](https://github.com/virg736/phishing/actions/workflows/python.yml/badge.svg)](https://github.com/virg736/phishing/actions/workflows/python.yml)


<!-- Image principale -->
<p align="center">
<img src="phisting1.PNG" alt="Image de couverture - phishing" width="100%" />
</p>

<!-- Badges centrés -->
<p align="center">
<img src="https://img.shields.io/badge/stabilité-stable-brightgreen" alt="stabilité stable" />
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
<img src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" alt="Licence Creative Commons BY-NC-SA 4.0" />
</p>

<!-- Mentions légales -->
<p align="center">
<b>© 2025 Virginie Lechene - Tous droits réservés</b><br>
Reproduction ou diffusion interdite sans autorisation. <i>Usage strictement pédagogique.</i>
</p>
<p align="center"><strong>📸 Image protégée — Propriété exclusive</strong></p>

<p align="center">

---

## 🛡️ Phishing : Comment se protéger - Bonnes pratiques

### 🔗 Sommaire
1. [Introduction](#introduction)
2. [Bonnes pratiques anti-phishing + outils de vérification](#bonnes-pratiques-anti-phishing--outils-de-vérification)
3. [Analyse d'un en-tête d'e-mail (headers)](#analyse-dun-en-tête-demail-headers)
4. [Pour aller plus loin](#pour-aller-plus-loin)
5. [Sécurité des macros – Pourquoi un fichier ne suffit pas](#sécurité-des-macros--pourquoi-un-fichier-ne-suffit-pas)
6. [Ce que cela signifie concrètement](#ce-que-cela-signifie-concrètement)
7. [🛑 Attention aux fichiers PDF](#-attention-aux-fichiers-pdf)
8. [🔍 Exemple d'utilisation](#exemple-dutilisation)
9. [À propos de l’usage](#à-propos-de-lusage)
10. [Droits sur les visuels](#droits-sur-les-visuels)




---

## Introduction

Le **phishing** (ou hameçonnage) est une technique très répandue chez les cybercriminels.
Elle vise à tromper la victime afin de lui faire **divulguer des informations sensibles** : mots de passe, coordonnées bancaires, identifiants, etc.

Ce projet a pour objectif de **sensibiliser** et de fournir de **bonnes pratiques concrètes**, accompagnées de **liens d’analyse** (email, pièces jointes, etc.).

---

## Bonnes pratiques anti-phishing + outils de vérification

1. **Vérifier l’adresse réelle de l’expéditeur**
🔗 [MailHeader Analyzer (Google)](https://toolbox.googleapps.com/apps/messageheader/)
🔗 [MXToolbox Email Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)

2. **Survoler les liens avec la souris avant de cliquer**
🔗 [VirusTotal - Scanner d'URL](https://www.virustotal.com/)
🔗 [URLScan.io](https://urlscan.io/)

3. **Analyser les pièces jointes avant de les ouvrir**
🔗 [VirusTotal – Analyse de fichier](https://www.virustotal.com/gui/home/upload)

4. **Afficher et lire les en-têtes d’un e-mail (headers)**
À examiner : `From`, `Reply-To`, `Return-Path`, `Received`, `SPF`, `DKIM`

5. **Vérifier si un site est signalé comme dangereux**
🔗 [Google Safe Browsing](https://transparencyreport.google.com/safe-browsing/search)
🔗 [PhishTank](https://phishtank.org/)

6. **Rechercher à qui appartient un domaine (whois)**
🔗 [Who.is](https://who.is/)
🔗 [SecurityTrails](https://securitytrails.com/)

Les outils et ressources externes mentionnés dans ce projet (ex. : VirusTotal, Google Header Analyzer, PhishTank…) sont tous **publics, légaux** et utilisés dans un **but exclusivement pédagogique**.

Aucune de ces plateformes n’est modifiée ou utilisée de manière détournée.
Les liens sont fournis uniquement pour **sensibiliser aux bonnes pratiques** en matière de cybersécurité (analyse d’e-mails, de liens, de fichiers…).

> Ce projet n’encourage en aucun cas l’usage de techniques offensives sans autorisation légale préalable.

 Pour plus d'informations sur l'utilisation de liens à des fins pédagogiques :
- [Legifrance – Code de la propriété intellectuelle, Article L122-5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278917/)
- [CNIL – Sensibilisation à la cybersécurité](https://www.cnil.fr)

----

8. **Mettre à jour son antivirus et activer les protections antiphishing**
✅ Activer SmartScreen (Windows)
✅ Activer les protections Gmail / Outlook

9. **Ne jamais cliquer sur un lien inconnu dans un e-mail**
✍️ Tapez l’URL directement dans votre navigateur.

---

 Analyse d'un en-tête d'e-mail (headers)

| **Élément** | **Ce qu’il faut analyser** |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **From** | Est-ce l’adresse attendue ? (ex. : `support@banque.fr`) |
| **Reply-To** | Est-elle identique à l’adresse "From" ? Si c’est une autre adresse (ex. : `offre-banque@protonmail.com`), cela peut être suspect. |
| **Return-Path** | Adresse réelle de retour. Peut différer du "From" en cas de spoofing, et doit être vérifiée. |
| **Received** | Liste des serveurs par lesquels est passé l’e-mail. Une origine inhabituelle (ex. : serveur basé à l’étranger, VPN, etc.) est un signal d’alerte. |
| **DKIM / SPF / DMARC** | Signatures utilisées pour vérifier que le domaine de l’expéditeur est autorisé à envoyer l’e-mail. Si elles sont absentes ou échouées, cela indique un danger. |



## Pour aller plus loin
🔗 [Cybermalveillance.gouv.fr - Hameçonnage](https://www.cybermalveillance.gouv.fr/)
🔗 [CNIL – Reconnaître un e-mail frauduleux](https://www.cnil.fr/)

---

## Sécurité des macros – Pourquoi un fichier ne suffit pas

Depuis 2022, **Microsoft Office (Excel, Word)** désactive les **macros par défaut** pour tout fichier **téléchargé depuis Internet ou reçu par e-mail**.


---

 Ce que cela signifie concrètement

- Tant que l’utilisateur **n’active pas les macros**, aucun code malveillant ne s’exécute.
- C’est **uniquement après avoir cliqué sur "Activer le contenu"** que la macro se lance.
- Ensuite, le fichier peut :
- Se connecter à un serveur distant
- Télécharger un **payload** (virus)
- L’exécuter discrètement

💡 Cette méthode est couramment utilisée dans les attaques de type **phishing par macro VBA**.


Exemple de simulation d'attaque macro :

Private Sub Workbook_Open()
MsgBox "Étape 1 - Réception d’un e-mail piégé"
MsgBox "Étape 2 - Ouverture du fichier Excel, clic sur 'Activer le contenu'"
MsgBox "Étape 3 - Exécution de la macro"
Shell "notepad.exe", vbNormalFocus
MsgBox "Étape 4 - Propagation et chiffrement"
End Sud

💡 Ce fichier Excel simule **visuellement** une attaque par macro, **sans aucun danger réel**. Il ne contient **aucun code malveillant**, ne chiffre rien et ne contacte aucun serveur. Il s’agit d’un **exemple éducatif** 100 % local.

<p align="center">
<img src="./simulation_macro2.PNG" alt="Simulation de macro Excel malveillante" width="80%">
</p>

### 🔎 À retenir :

- Les macros sont encore utilisées dans certains environnements **insuffisamment sécurisés**.
- Depuis 2022, **Microsoft bloque par défaut les macros** dans les fichiers téléchargés depuis Internet (`Office 2022+`, Microsoft`365`).
- Les attaquants contournent ces protections en :
- hébergeant les fichiers sur des serveurs internes compromis,
- utilisant des documents Word (`.docm`) ou PowerPoint avec macros,
- demandant à l’utilisateur de **désactiver manuellement** les protections.

---

### ✅ Conclusion

Cette méthode reste redoutablement **efficace** si l’utilisateur est piégé et **active manuellement** le contenu malveillant.

<p align="center">
<img src="./Simulation_macro3.PNG" alt="Simulation d'une attaque par macro Excel" width="80%">
</p>

----

## 🛑 Attention aux fichiers PDF

Les fichiers PDF peuvent également contenir des menaces :

- Ils peuvent intégrer des **scripts malveillants** ou des **liens piégés**.
- Certains PDF déclenchent une **demande d’activation de contenu dynamique** (JavaScript).
- Ils peuvent inciter à cliquer sur un **lien de phishing déguisé** (ex. : bouton "Voir la facture").

### 🛡️ Recommandations

- **Ne pas ouvrir directement les fichiers PDF suspects**, même dans un navigateur.
- **Analyser les fichiers PDF avec un antivirus** ou un service comme [VirusTotal – Analyse de fichier](https://www.virustotal.com/gui/home/upload).
- **Ne jamais cliquer sur un lien ou un bouton intégré à un PDF d’origine inconnue.**

----

##  Exemple d'utilisation

 ✅ À propos du script
Ce script Python a été développé dans un but **strictement pédagogique** pour aider à **analyser des e-mails suspects** (au format `.eml`) et **détecter des signes de phishing**.

🛡️ Il permet notamment d’extraire automatiquement des informations clés comme :

- l’expéditeur réel (`From`, `Reply-To`, `Return-Path`),
- les serveurs traversés (`Received`),
- la présence ou non d’authentifications (`SPF`, `DKIM`, `DMARC`),
- les liens contenus dans le message.

📌 Le script est **testé automatiquement** via **GitHub Actions** et validé ✅ (badge vert) à chaque modification.

  ---

Exécution par un utilisateur

Si vous souhaitez exécuter ce script :

 Cloner le dépôt GitHub
- git clone https://github.com/virg736/phishing.git && cd phishing
- Rendre le script exécutable
- chmod +x phishing_script.py
- Lancer l’analyse sur un e-mail .eml
- ./phishing_script.py samples/email_suspect.eml

![Exécution du script](script_phishing3.PNG)


---

## À propos de l’usage

📄 **Licence :**
Ce projet est distribué sous **licence MIT**, permettant l’usage, la modification et la redistribution **à condition de respecter les mentions d’origine**.

🔒 **Important :**
Ce script **ne collecte aucune donnée** et **ne communique avec aucun serveur externe**.
Il peut être utilisé **en local et hors ligne**, dans le cadre :
- d’une **formation en cybersécurité**,
- d’un **audit légal**,
- ou d’un **atelier de sensibilisation pédagogique**.
  
> L’auteure **ne cautionne ni n’autorise** l’utilisation de ce script en dehors d’un cadre légal strictement défini.
> Toute utilisation non conforme est interdite et relève **uniquement de la responsabilité de l’utilisateur**.

---

## Droits sur les visuels

Les visuels, illustrations ou captures présents dans ce dépôt sont la propriété exclusive de l’auteure.
Toute reproduction ou réutilisation sans **autorisation préalable** est interdite.

© 2025 Virginie Lechene - Tous droits réservés.






