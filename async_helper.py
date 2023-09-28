from PySide6.QtCore import QObject, Signal, Slot, QEvent
from PySide6.QtWidgets import QApplication
import asyncio

class AsyncHelper(QObject):

    class ReenterQtObject(QObject):

        def event(self, event):
            if event.type() == QEvent.Type.User + 1:
                event.fn()
                return True
            return False

    class ReenterQtEvent(QEvent):

        def __init__(self, fn):
            super().__init__(QEvent.Type(QEvent.Type.User + 1))
            self.fn = fn

    def __init__(self, worker, entry):
        super().__init__()
        self.reenter_qt = self.ReenterQtObject()
        self.entry = entry
        self.loop = asyncio.new_event_loop()
        self.done = False

        self.worker = worker
        if hasattr(self.worker, "astruino_start") and isinstance(self.worker.astruino_start, Signal):
            self.worker.astruino_start.connect(self.on_worker_started)
        if hasattr(self.worker, "astruino_done") and isinstance(self.worker.astruino_done, Signal):
            self.worker.astruino_done.connect(self.on_worker_done)

    @Slot()
    def on_worker_started(self):
        if not self.entry:
            raise Exception(
                "No entry point for the asyncio event loop was set.")
        asyncio.set_event_loop(self.loop)
        self.loop.create_task(self.entry())
        self.loop.call_soon(self.next_guest_run_schedule)
        # Set this explicitly as we might want to restart the guest run.
        self.done = False
        self.loop.run_forever()

    @Slot()
    def on_worker_done(self):
        self.done = True
        self.worker.set_all_buttons_enabled(True)

    def continue_loop(self):
        if not self.done:
            self.loop.call_soon(self.next_guest_run_schedule)
            self.loop.run_forever()

    def next_guest_run_schedule(self):
        self.loop.stop()
        QApplication.postEvent(
            self.reenter_qt, self.ReenterQtEvent(self.continue_loop))