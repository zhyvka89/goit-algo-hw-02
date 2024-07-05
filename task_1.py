import uuid
from queue import Queue
from time import sleep


request_queue = Queue()

def generate_request():
  new_request = {
    "id": uuid.uuid4(),
    "status": 200
  }
  request_queue.put(new_request)
  print(F'Request with id {new_request["id"]} is created!')


def process_request():
  if request_queue.empty():
    print('Queue is empty!')
  else:
    current_request = request_queue.get()
    print(F'Request with id {current_request["id"]} is processed!')



def main():
  try:
    while True:
      generate_request()
      sleep(0.2)
      process_request()
      sleep(0.2)
  except KeyboardInterrupt:
    print("Finish file processing")


if __name__ == "__main__":
  main()