from queue import Queue
import random
import time

q = Queue()
request_id = 0


def generate_request():
    global request_id
    num_new_requests = random.randint(0, 5)

    for _ in range(num_new_requests):
        request_id += 1
        q.put(f"Request-{request_id}")

    print(f"{q.qsize()} requests in queue")


def process_request():
    if not q.empty():
        max_process = min(5, q.qsize())
        to_process = random.randint(1, max_process)
        print(f"{to_process} requests are being processed")

        for _ in range(to_process):
            current_request = q.get()
            print(f"{current_request} closed")
    else:
        print(f"Queue is empty. Service center stopped.")
        return "Done"


print("Service center started. Press Ctrl+C to stop.")
try:
    while True:
        generate_request()
        result = process_request()
        if result == "Done":
            break
        time.sleep(1)
except KeyboardInterrupt:
    print("\nService center stopped.")
