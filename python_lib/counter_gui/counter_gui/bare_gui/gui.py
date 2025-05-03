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
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, Qt
from counter_gui.bare_gui.gui_api import RosaryAPI


class RosaryGUI(QWidget):
    def __init__(self, api: RosaryAPI):
        super().__init__()
        self.api = api
        self.api.update_signal.connect(self.update_ui_from_api)

        self.setWindowTitle("Rosary Prayer")
        self.setGeometry(100, 100, 500, 300)

        self.layout = QVBoxLayout()

        self.mystery_label = QLabel("Mystery:")
        self.mystery_text = QTextEdit()
        self.mystery_text.setReadOnly(True)

        self.prayer_label = QLabel("Prayer:")
        self.prayer_text = QTextEdit()
        self.prayer_text.setReadOnly(True)

        self.counter_label = QLabel("Hail Mary Count: 0")

        self.button_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
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

    def next_prayer(self):
        if self.api.current_index < len(self.prayers) - 1:
            self.api.current_index += 1

    def prev_prayer(self):
        if self.api.current_index > 0:
            self.api.current_index -= 1

    def update_ui_from_api(self, data):
        self.mystery_text.setText(data["mystery"])
        self.prayer_text.setText(data["prayer"])
        self.counter_label.setText(data["hail_mary_count"])
