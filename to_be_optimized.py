from time import sleep
from time import time


TIME_DELAY = 3  # Don’t change this variable


class Client:
    """Client class"""

    def __init__(self) -> None:
        self.time_delay = TIME_DELAY

    def request(self) -> None:
        """Client request"""
        sleep(self.time_delay)


class Server:
    """Server class"""

    def __init__(self) -> None:
        self.time_delay = TIME_DELAY

    def run(self, request: None) -> None:
        """Run method"""
        self.listen(request)
        print("Starting server...")  # noqa T201
        sleep(self.time_delay)
        print("The work is done!!!")  # noqa T201

    def listen(self, client_request: None) -> None:
        """Listen method"""
        print("Listening event...")  # noqa T201
        client_request()
        print("Processing event")  # noqa T201


if __name__ == "__main__":
    server = Server()
    client = Client()
    t0 = time()
    server.run(client.request)
    print(f"Time spent: {time() - t0}")  # noqa T201
