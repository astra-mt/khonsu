# ASTRA Khonsu

A graphical user interface to monitor the rover

## Translating the UI in code

After you have successfully installed QT Designer you should be able to execute inside a terminal the command

    pyuic5

The command:

    pyuic5 /path/to/your/.ui_file -o generated_code.py

will generate the `generated_code.py` file inside the folder where you execute the command

### Organization of the project
 - The `res` folder contains the resources used by the interface(images,etc..)
 - The `ui` folder will contain the .ui file obtained with QT Designer