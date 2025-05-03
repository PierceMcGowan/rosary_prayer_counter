from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, Qt


class RosaryAPI(QObject):
    # Signals for thread-safe communication
    update_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self._data = {
            "mystery": "The Annunciation",
            "prayer": "Hail Mary",
            "hail_mary_count": 0,
        }
        self.current_index = 0

    def get_data(self):
        return self._data.copy()

    @pyqtSlot(dict)
    def set_data(self, new_data):
        self._data.update(new_data)
        self.update_signal.emit(self._data.copy())
