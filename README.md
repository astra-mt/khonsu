
# ASTRA Khonsu

A graphical user interface to monitor our rover "Scout". Currently migrating from PyQt5 to PySide6.

**Work in progress**

- [ ] Assicurarsi che la connessione sia stata correttamente stabilita. Attualmente lancia eccezione.
- [ ] Gestire comportamento quando chiudi la GUI durante un'operazione send-astruino
- [ ] Ricevere output da arduino e stamparlo su terminale in app
- [ ] Trova widget migliore per il log. Serve che abbia degli eventi "valueChanged" così da potere abilitare e disabilitare il tasto.
- [ ] Sistemare grandezza stream
- [ ] GUI [Commands to implement](https://www.notion.so/astra-team/Documentazione-comandi-e445912294c94576b910cc75a6e5b087)
- [ ] Implementare file .env


## Come creare un widget

The command:

    pyuic5 --output=./newfile.py ./newfile.ui

will generate the `new_main.py` file inside the folder where you execute the command.
The resulting file uses PyQt5

Replace `PyQt5` with `PySide6`, and then substitute the following lines:

``` python

    from PyQt5 import ... 

    ...

    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(400, 300)
```

with these ones

``` python


    from PySide6 import ... 

    ...


    class ExampleWidget(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            Form = self
            Form.setObjectName("ExampleWidget")
            Form.setAccessibleName("ExampleWidget")
```

Nomenclatura: `movement.ui`, `movement,py`, `MovementView(QtWidgets.QWidget)`, `MovementWidget()`

## Project Folders
 - The `res` folder contains the resources used by the interface(images,etc..)
 - The `ui` folder will contain the .ui file obtained with QT Designer

---

## Debugging

Open the file `bluetooth.ino` within the Arduino IDE, then load it on the board and run it. Open the serial plotter to see the received data, and choose the option `Both NL & CR`.

A list of commands can be acquired by sending the command `AT+HELP`. Some of those instructions don't work. That command and others can be found in the [Notion AT-09 Documentation](https://www.notion.so/astra-team/Documentation-of-bluetooth-module-AT-09-4bb4d29fb7db46d291fcfd81fea8ce22) that contains all the tested commands we've been able to send.

Make sure to select the board *Arduino Mega or Mega 2560*, in the dropdown menu in the top left border.   