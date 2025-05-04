from typing import Dict
from multiprocessing import Pipe, connection


class RosaryAPI():
    def __init__(self, pipe: connection.Connection) -> None:
        super().__init__()
        self._data: Dict = {
            "mystery": "The Annunciation",
            "prayer": "Hail Mary",
            "hail_mary_count": "",
        }
        self.current_index: int = 0
        self.pipe = pipe

    def get_index(self) -> int:
        return self.current_index

    def set_data(self, new_data: Dict) -> None:
        self._data.update(new_data)
        self.pipe.send(self._data.copy())  # Send updated data through the pipe

    def listen_for_updates(self) -> None:
        """Continuously listen for updates from the GUI."""
        while True:
            if self.pipe.poll():  # Check if there's data in the pipe
                new_data = self.pipe.recv()  # Receive data from the pipe
                if "index" in new_data:
                    self.current_index = new_data["index"]
                else:
                    self.set_data(new_data)
