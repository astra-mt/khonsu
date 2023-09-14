"""
    Manages signals from the UI
"""

import sys

def tryNewFunctionality(message: str=None):
        """ Testing """
        if message:
            print(message)
        else:
            print("Prova")
   
def handleSaveLog():
    """ Handles Save Log"""
    print("Handling Save Log")

def set_dc_engine_value(value): 
    """ Returns a value for the DC engine. Highest value: , Lowest value: 255 """
    print (f"DC engine set to: {value}") 
    return value*255