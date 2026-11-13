
class Resource:
    def __enter__(self):
        print("Resource opened")
        return self

    def process(self):
        print("Processing resource")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")
        return False


with Resource() as r:
    r.process()
