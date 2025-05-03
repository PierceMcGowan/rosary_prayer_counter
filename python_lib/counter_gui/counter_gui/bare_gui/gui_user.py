from counter_gui.bare_gui.gui_api import RosaryAPI
from counter_gui.bare_gui.gui import RosaryGUI
from PyQt5.QtWidgets import QApplication
import sys
from typing import Tuple


def start_gui() -> Tuple[QApplication, RosaryAPI]:
    app = QApplication(sys.argv)
    api = RosaryAPI()
    gui = RosaryGUI(api)
    gui.show()
    return app, api


def wait_for_stop_gui(app: QApplication) -> None:
    sys.exit(app.exec_())
