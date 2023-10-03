
# ASTRA Khonsu

A graphical user interface to monitor our rover "Scout". Currently migrating from PyQt5 to PySide6.

**Work in progress**

- [ ] Assicurarsi che la connessione sia stata correttamente stabilita. Attualmente lancia eccezione.
- [ ] Gestire comportamento quando chiudi la GUI durante un'operazione send-astruino
- [ ] Ricevere output da arduino e stamparlo su terminale in app
- [ ] Trova widget migliore per il log. Serve che abbia degli eventi "valueChanged" così da potere abilitare e disabilitare il tasto.
- [ ] Implementare widget da mettere nella toolbox per il controllo della cam che possa fermare lo stream (timer.stop()) e farlo riprendere (timer.start(10))
- [ ] Sistemare grandezza stream

# Old, ignore

## Translating the UI in code

### Installing pyuic5

- Identify where you have installed python (the folder where ypu have python.exe)
- Open a cmd in that folder *(NOTE: if it is on the C main drive open the terminal with administrator privileges)* and execute: 

        python -m pip install PyQt5

After you have successfully installed PyQt5 you should be able to execute inside a terminal the command

    pyuic5

The command:

    pyuic5 --output=./new_main.py ./new_main.ui

will generate the `new_main.py` file inside the folder where you execute the command

### Organization of the project
 - The `res` folder contains the resources used by the interface(images,etc..)
 - The `ui` folder will contain the .ui file obtained with QT Designer

## Embedding windows

A useful resource: https://stackoverflow.com/questions/71027763/how-to-open-a-new-mdi-sub-window-in-pyqt5

Secondary windows can be modeled in QT Designer as 'Widgets' *(NOTE: requires a little change in the code, see section 'Adapting widget code' below)*. In the `example_widget` folder there are:
-  `example_widget.py` file which describe a secondary window 
-   `main.py` file where there's the code of the main window that embed `example_widget.py` secondary window

### Adapting Widget object code

Substitute the following lines:

    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(400, 300)

with these ones `(of course for the class name and variable names you can put whatever name you want bu you must keep consistency with the rest of the code)`:

    class ExampleWidget(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            Form = self
            Form.setObjectName("Form")
            Form.resize(400, 300)

## Layout weights

To specify weights for space of elements inside a container you have to search the parent layout and set the `layoutStretch` property as you want. See the example:

<img src="./images/stretch_example.png"></img>

where I specified `2,6,2` to get the 20% 60% 20% proportions of the 3 elements

## Check arduino output

On linux run

`ls /dev/ttyACM0 && sudo chmod a+rw /dev/ttyACM0`

---

Open the file `bluetooth.ino` within the Arduino IDE, then load it on the board and run it. Open the serial plotter to see the received data, and choose the option `Both NL & CR`.

A list of commands can be acquired by sending the command `AT+HELP`. Some of those don't work. That command and others can be found in the [Notion AT-09 Documentation](https://www.notion.so/astra-team/Documentation-of-bluetooth-module-AT-09-4bb4d29fb7db46d291fcfd81fea8ce22) that contains all the tested commands we've been able to send.

Make sure to select the board *Arduino Mega or Mega 2560*, in the dropdown menu in the top left border.   

GUI [Commands to implement](https://www.notion.so/astra-team/Documentazione-comandi-e445912294c94576b910cc75a6e5b087)