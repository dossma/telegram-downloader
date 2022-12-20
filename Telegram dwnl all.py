from telethon import TelegramClient, events, sync
import os.path

# Parameter:
folder = r"C:\path\to\your\folder"
channel = "DieStahlfeder"  # pasting the full link works too: https://t.me/DieStahlfeder
limit = 2  # Argument limit begrenzt die Zahl der Downloads, kann "None" sein

# Get API ID and API hash from https://core.telegram.org/api/obtaining_api_id#obtaining-api-id
api_id = 1234567  # These example values won't work. You must get your own api_id
api_hash = 'paste-your-api-hash-here'

client = TelegramClient('mySession', api_id, api_hash)
client.start()
print("Client gestartet")

print("Einträge einholen")
msgs = client.get_messages(channel, limit=limit)
print(len(msgs), "Einträge vorhanden")

os.chdir(folder)  # Arbeitsverzeichnis zum Zielordner ändern
errlist = []  # Nicht heruntergeladene message-Namen
counter = 0  # Zähler wieviele Nachrichten übrig sind

for msg in msgs:
    if not msg.file:  
        counter += 1
        print(len(msgs) - counter, " übrig", "\n")
        continue
    else:  # Prüfen, ob die Datei schon heruntergeladen wurde (im Verzeichnis vorhanden ist)
        if msg.file.name:
            filename = msg.file.name
        elif msg.text:
            filename = msg.text + msg.file.ext  # Name + Dateiendung
        elif msg.file.name:
            filename = msg.file.name + msg.file.ext  # Name + Dateiendung
        else:
            filename = "unknown" + msg.file.ext
        # Dateinamen Windows-konform aufbereiten
        filename = filename.replace("\n", " - ")
        filename = filename.replace("\\", "-")
        filename = filename.replace("/", "-")
        filename = filename.replace("?", "-")
        filename = filename.replace("\"", "!")
        filename = filename.replace(r"*", " ! ")
        filename = filename.replace(r"<", " ! ")
        filename = filename.replace(r">", " ! ")
        filename = filename.replace(r":", " - ")

        file_exists = os.path.exists(r"C:\Users\Katzi\HiDrive\Hörbücher + Podcasts\Diplomatenradio\%s" % filename)

        if file_exists:
            print ("Überspringe", filename)
            counter += 1
            print(len(msgs) - counter, " übrig", "\n")
            continue  # Wenn Datei schon vorhanden, überspringen

    try:  # Datei ist noch nicht im Verzeichnis. Versuchen, sie herunterzuladen
        msg.download_media(filename)
        print("msg:", filename, "runtergeladen")
        print(len(msgs) - counter, " übrig", "\n")
        counter += 1
        # id_list.append(msg.id)  # Erfolgreiche Message-ID in Liste speichern
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
        print ("msg:\n", filename, "\nkonnte nicht heruntergeladen werden")
        errlist.append(filename)

client.disconnect()
print("Einträge runterladen abgeschlossen")
print ("Nicht heruntergeladene Dateien:")
for x in zip(errlist):
    print(x)

