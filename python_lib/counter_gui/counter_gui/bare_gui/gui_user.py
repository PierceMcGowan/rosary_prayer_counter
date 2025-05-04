from counter_gui.bare_gui.gui_api import RosaryAPI
from counter_gui.bare_gui.gui import RosaryGUI
from PyQt5.QtWidgets import QApplication
import sys
from typing import Tuple
from threading import Thread
from multiprocessing import Pipe


def start_gui() -> Tuple[QApplication, RosaryAPI]:
    app = QApplication(sys.argv)

    # Create a pipe for communication
    parent_conn, child_conn = Pipe()

    # Initialize API and GUI
    api = RosaryAPI(pipe=child_conn)
    gui = RosaryGUI(pipe=parent_conn)

    # Start API listener in a separate thread
    api_thread = Thread(target=api.listen_for_updates, daemon=True)
    api_thread.start()

    gui.show()
    return app, api


def wait_for_stop_gui(app: QApplication) -> None:
    sys.exit(app.exec_())
