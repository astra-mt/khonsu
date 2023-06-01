from movement import View2
from arm import View3

class Logic():
    def addSubWindow(self, viewToAdd: str):
        """ Show a subwindow in the MDI central area """

        view = None

        if viewToAdd == "movement":
            view = View2()
        elif viewToAdd == "arm":
            view = View3()

        if view != None:
            subwindow = self.mdiArea.addSubWindow(view)
            subwindow.setWindowTitle("Example Widget")
            subwindow.show()

    def tryNewFunctionality(self):
        """ Testing """
        print("Prova")