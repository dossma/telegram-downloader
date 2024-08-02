'''
Notice:
This program uses the Telegram API and is part of the Telegram ecosystem.
'''
from telethon import TelegramClient, events, sync
import os.path

# Input Parameter:
folder = r"C:\path\to\your\folder"
channel = r"DieStahlfeder"  # pasting the full link works too: https://t.me/DieStahlfeder
limit = None  # Set a number to limit the downloads or None for downloading all
# Get API ID and API hash from https://core.telegram.org/api/obtaining_api_id#obtaining-api-id
api_id = 1234567  # These example values won't work. You must get your own api_id
api_hash = 'paste-your-api-hash-here'

# Start of Program
client = TelegramClient('mySession', api_id, api_hash)
client.start()
print("Client startet, getting entries")
msgs = client.get_messages(channel, limit=limit)
print(len(msgs), "entries available\n")
os.chdir(folder)  # Arbeitsverzeichnis zum Zielordner ändern
errlist = []  # Nicht heruntergeladene message-Namen
counter = 0  # Zähler wieviele Nachrichten übrig sind

for msg in msgs:
    if not msg.file: 
        counter += 1
        continue
    else:  # Prüfen, ob die Datei schon heruntergeladen wurde, also im Verzeichnis vorhanden ist
        creatime = msg.date.date().isoformat()  # Datumsformat: yyyy-mm-dd
        if msg.file.name:
            filename = creatime + " " + msg.file.name
        elif msg.text:
            filename = creatime + " " + msg.text + msg.file.ext  # Name + Dateiendung
        elif msg.file.name:
            filename = creatime + " " + msg.file.name + msg.file.ext  # Name + Dateiendung
        else:
            filename = creatime + " " + "unknown" + msg.file.ext
        # Unerlaubte Dateizeichen ersetzen
        filename = filename.replace("\n", " - ") 
        filename = filename.replace("\\", "-")
        filename = filename.replace("/", "-")
        filename = filename.replace("?", "-")
        filename = filename.replace("\"", "!")
        filename = filename.replace(r"*", " ! ")
        filename = filename.replace(r"<", " ! ")
        filename = filename.replace(r">", " ! ")
        filename = filename.replace(r":", " - ")

        file_exists = os.path.exists(folder + "%s" % "\\" + filename)

        if file_exists:
            print("Skipping", filename)
            counter += 1
            print(len(msgs) - counter, " übrig", "\n")
            errlist.append(filename)
            continue  # Wenn Datei schon vorhanden, überspringen

    counter += 1
    try:  # Datei ist noch nicht im Verzeichnis. Versuchen, sie herunterzuladen
        print("Start downloading entry", counter, "of", str(len(msgs)) + ":\n", filename)
        msg.download_media(filename)
        # msg.download_media()
        print("Done")
        # print(len(msgs) - counter, "entries left", "\n")
        # id_list.append(msg.id)  # Erfolgreiche Message-ID in Liste speichern
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
        print ("msg:\n", filename, "\ncould not be downloaded")
        errlist.append(filename)

client.disconnect()
print("F I N I S H E D")
if len(errlist) < 1:
    print ("All files could be downloaded")
else:
    print ("Files which were not downloaded:")
    for x in zip(errlist):
        print(x)

