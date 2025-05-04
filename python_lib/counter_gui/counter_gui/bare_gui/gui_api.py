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
from typing import Dict


class RosaryAPI(QObject):
    # Signals for thread-safe communication
    update_signal = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._data: Dict[str, str, int] = {
            "mystery": "The Annunciation",
            "prayer": "Hail Mary",
            "hail_mary_count": 0,
        }
        self.current_index: int = 0

    def get_data(self) -> int:
        return self.current_index

    @pyqtSlot(dict)
    def set_data(self, new_data: Dict[str, str, int]) -> None:
        self._data.update(new_data)
        self.update_signal.emit(self._data.copy())
