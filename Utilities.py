from PySide6.QtCore import Slot, Signal

def async_start():
    start_signal = Signal()
    start_signal.emit()
