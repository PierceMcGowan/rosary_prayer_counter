import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QHBoxLayout,
)
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from counter_gui.bare_gui.gui_api import RosaryAPI
from typing import Dict
from multiprocessing import Pipe, connection


class RosaryGUI(QWidget):
    update_ui_signal = pyqtSignal(dict)

    def __init__(self, pipe: connection.Connection) -> None:
        super().__init__()
        self.pipe = pipe

        self.setWindowTitle("Rosary Prayer")
        self.setGeometry(100, 100, 500, 300)

        self.layout: QVBoxLayout = QVBoxLayout()

        self.mystery_label: QLabel = QLabel("Mystery:")
        self.mystery_text: QTextEdit = QTextEdit()
        self.mystery_text.setReadOnly(True)

        self.prayer_label: QLabel = QLabel("Prayer:")
        self.prayer_text: QTextEdit = QTextEdit()
        self.prayer_text.setReadOnly(True)

        self.counter_label: QLabel = QLabel("Hail Mary Count: 0")

        self.button_layout: QHBoxLayout = QHBoxLayout()
        self.prev_button: QPushButton = QPushButton("Previous")
        self.next_button: QPushButton = QPushButton("Next")
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)

        self.layout.addWidget(self.mystery_label)
        self.layout.addWidget(self.mystery_text)
        self.layout.addWidget(self.prayer_label)
        self.layout.addWidget(self.prayer_text)
        self.layout.addWidget(self.counter_label)
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

        self.prev_button.clicked.connect(self.prev_prayer)
        self.next_button.clicked.connect(self.next_prayer)

        # Connect the signal to the slot
        self.update_ui_signal.connect(self.update_ui_from_api)

        # Start a thread to listen for updates from the API
        self.listener_thread = QThread()
        self.listener_thread.run = self.listen_for_updates
        self.listener_thread.start()

        self.current_index: int = 0

    def next_prayer(self) -> None:
        self.current_index += 1
        self.pipe.send({"index": self.current_index})  # Send action to API

    def prev_prayer(self) -> None:
        if self.current_index > 0:
            self.current_index -= 1
        self.pipe.send({"index": self.current_index})  # Send action to API

    def listen_for_updates(self) -> None:
        """Continuously listen for updates from the API."""
        while True:
            if self.pipe.poll():  # Check if there's data in the pipe
                data = self.pipe.recv()  # Receive data from the pipe
                self.update_ui_signal.emit(data)  # Emit the signal with the data

    @pyqtSlot(dict)
    def update_ui_from_api(self, data: Dict) -> None:
        """Update the UI from the API data."""
        self.mystery_text.setText(data["mystery"])
        self.prayer_text.setText(data["prayer"])
        self.counter_label.setText(str(data["hail_mary_count"]))
