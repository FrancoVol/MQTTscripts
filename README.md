# NOTE IMPORTANTI

- Tutti i file vanno runnati con python3: paho mqtt ha un modo strano di mandare i messaggi con python2, nel senso che accetta solo stringhe, perciò c'è bisogno di fare tutto con python3

- Ricordarsi di runnare come sudoer tutti gli script che runnano sul gateway e usano Coral, in quanto il gateway è impostato di modo che solo i sudoer possono accedere alle periferiche

# NEXT STEPS

- Aggiornare subscriber_image.py di modo che mandi un messaggio con il risultato su un broker

- Aggiornare publish_image.py di modo che sia in ascolto una volta mandata l'immagine

- Aggiornare classify_image_custom.py di modo che fornisca i risultati in un json/stringa

## PICCOLI ACCORGIMENTI

- classify_image_default.py è il codice di default degli esempi di Coral per classificare l'immagine, usato solo per prendere spunto per il custom

- Tutti i file necessary al gateway vengono copiati nella cartella /home/fvolante/coral/tests e bisogna passare anche gli altri file necessari (es: i modelli tflite o i txt con i label)

- code_snippets.py ha rimasugli di codice per la LSTM che è ancora da testare.