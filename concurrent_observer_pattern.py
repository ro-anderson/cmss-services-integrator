"""
Observer Pattern with Threading Optimization:

The original problem consisted of a server listening for a client request and then doing its own task.
These tasks were sequential and time-consuming, leading to longer overall execution time. This code
implements the Observer pattern with threading to optimize the execution time.

- Observer Pattern:
    The Observer pattern is used to allow an object (known as a subject) to notify other objects
    (known as observers) about changes without knowing who or what those observers are. This provides
    a decoupled architecture which is more scalable and maintainable.

- Threading:
    Threading is used to allow the server and the client to operate concurrently. This reduces the total
    time required to execute the program because the server and client no longer have to wait for one
    another to finish their tasks.

Together, these changes allow the server to notify the client and then immediately proceed with its own
tasks, while the client processes its request in parallel.
"""


import threading

from time import sleep
from time import time


TIME_DELAY = 3  # Don’t change this variable


class Observer:
    """Observer (Client) that waits for updates from the Server (Subject)."""

    def __init__(self, time_delay: int) -> None:
        self.time_delay = time_delay

    def update(self, event_data: str) -> None:
        """Client request when notified by the server."""
        print(f"Received event: {event_data}")  # noqa T201
        sleep(self.time_delay)
        print("Processing event")  # noqa T201
        print("Client request processed.")  # noqa T201


class Subject:
    """Subject (Server) responsible for notifying observers about updates."""

    def __init__(self, time_delay: int) -> None:
        self._observers = []
        self.time_delay = time_delay

    def add_observer(self, observer: Observer) -> None:
        """Add an observer (client)."""
        self._observers.append(observer)

    def run(self) -> None:
        """Run method"""
        print("Starting server...")  # noqa T201

        # Spinning up a new thread to notify observers while the server continues its processing tasks.

        notify_thread = threading.Thread(target=self.notify_observers, args=("New data available",))
        notify_thread.start()

        sleep(self.time_delay)

        # Ensure the notification thread completes before exiting the run method
        notify_thread.join()
        print("The work is done!!!")  # noqa T201

    def notify_observers(self, event_data: str) -> None:
        """Notify all observers (clients) about an event."""

        # Analogous to the start of 'listen' method
        print("Listening event...")  # noqa T201

        for observer in self._observers:
            threading.Thread(target=observer.update, args=(event_data,)).start()


if __name__ == "__main__":
    server = Subject(TIME_DELAY)
    client = Observer(TIME_DELAY)

    server.add_observer(client)

    t0 = time()

    server.run()

    print(f"Time spent: {time() - t0}")  # noqa T201
