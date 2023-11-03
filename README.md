# NOTE IMPORTANTI

- Tutti i file vanno runnati con python3: paho mqtt ha un modo strano di mandare i messaggi con python2, nel senso che accetta solo stringhe, perciò c'è bisogno di fare tutto con python3

- Ricordarsi di runnare come sudoer tutti gli script che runnano sul gateway e usano Coral, in quanto il gateway è impostato di modo che solo i sudoer possono accedere alle periferiche

# NEXT STEPS

- Raffinare il codice, dovrebbe funzionare tutto

## PICCOLI ACCORGIMENTI

- Tutti i file necessary al gateway vengono copiati nella cartella /home/fvolante/coral/tests e bisogna passare anche gli altri file necessari (es: i modelli tflite o i txt con i label)

- code_snippets.py, default_inference_video.py, default_rtsp_listener.py e classify_image_default.py sono rimasugli di altri codice, tenuti ancora qui in fase di sviluppo, andranno rimossi perchè non facenti parte dello stack. Per ora rimangono perchè hanno delle parti di codice che potrebbero tornare utili in fase di debug o implementazione di altre features