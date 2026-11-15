
import time

def timer(func):
    def wrapper(self):
        start = time.time()

        func(self)

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


class Task:
    @timer
    def process(self):
        time.sleep(1)
        print("Task completed")


t = Task()
t.process()
