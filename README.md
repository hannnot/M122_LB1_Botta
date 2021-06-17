# M122_LB1_Botta

1. Erstellen Sie ein .txt Dokument in einem beliebigen Ordner
    * Schreiben Sie in dieses Dokument eine gültige E-Mail Adresse
2. Erstellen oder kopieren Sie ein .pdf Dokument
3. Clonen Sie das Projekt aus folgendem Repo:
    * https://github.com/hannnot/M122_LB1_Botta.git
4. Erstellen Sie eine config.ini Datei wie folgt:
[EMAILFILE]<br>
path = path_to_your_mail_txt_file/mail.txt

[ATTACHMENTFILE]<br>
path = path_to_your_pdf_file/attachment.pdf

[OUTPUTFILE]<br>
path = C:\Users\path_to_your_output_folder

[GMAILCONFIG]<br>
email = you@gmail.com<br>
pwd = yourpassword

Beachten Sie dass sie eine Gmail Adresse als Absenderadresse verwenden müssen<br>
Erstellen Sie ein App-Passwort nach folgendem Link<br>
https://support.google.com/accounts/answer/185833?hl=de&ref_topic=7189145

5. Überprüfen Sie Ihren Computer auf eine vorhandene Python installation in dem sie nachfolgenden Befehl in ein Windows Terminal eingeben: python

    * falls Python 3.9.5 (tags/v3.9.5:0a7dcbd, May 3 2021, 17:27:52) bereits installiert ist fahren Sie bei Punkt 6 fort
    * falls nicht installieren Sie python über die Entwicklerseite<br>
    https://www.python.org/downloads/windows/<br>
    und installieren Sie den Python 3

6. Falls Sie python zu Ihren Umgebungsvariabeln hinzugefügt haben:

    * öffnen Sie ein Windows Terminal im Ordner des geclonten Projekts und geben Sie folgenden Befehl ein:<br>
    python main.py

    * falls nicht:<br>
    öffnen Sie einen Windwos Explorer und navigieren Sie in den Installationsordner von Python, kopieren Sie den Pfad (incl. \python.exe)
    öffnen Sie ein Windows Terminal im Ordner des geclonten Projekts und geben Sie folgenden Befehl ein:
    path_to_your\python.exe main.py
