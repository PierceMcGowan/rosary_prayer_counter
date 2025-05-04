from rosary.runner.rosary_runner import setup_rosary, Rosary
from counter_gui.bare_gui.gui import RosaryGUI
from counter_gui.bare_gui.gui_api import RosaryAPI
from counter_gui.bare_gui.gui_user import start_gui, wait_for_stop_gui
import threading
import time

def rosary_worker(api: RosaryAPI) -> None:
    # Initialize the rosary object
    rosary = setup_rosary()

    while True:

        # Get data from gui API
        data = api.get_index()

        # Update rosary object with new data
        prayer, mystery = rosary.get_prayer_from_index(data)

        # Update the API with the new data
        api.set_data({
            "mystery": mystery,
            "prayer": prayer,
            "hail_mary_count": 0,
        })
        time.sleep(1)  # Simulate some processing time


def main():
    app, api = start_gui()

    # Launch rosary_worker in its own thread
    worker_thread = threading.Thread(target=rosary_worker, args=(api,))
    worker_thread.daemon = True  # Ensures the thread exits when the main program exits
    worker_thread.start()

    # Wait for the GUI to stop
    wait_for_stop_gui(app)


if __name__ == "__main__":
    main()