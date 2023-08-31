from time import time, sleep
TIME_DELAY = 3 # Don’t change this variable

class Client:
    def __init__(self) -> None:
        self.time_delay = TIME_DELAY
    def request(self):
        sleep(self.time_delay)
class Server:
    def __init__(self):
        self.time_delay = TIME_DELAY
        def run(self, request):
            self.listen(request)
            print("starting server...")
            sleep(self.time_delay)
            print("The work is done!!!")
        def listen(self, client_request):
            print("listening event...")
            client_request()
            print("processing event")

if __name__ == '__main__':

	server = Server()
	client = Client()
	t0 = time()
	server.run(client.request)
	print(f"time spent: {time() - t0}")
