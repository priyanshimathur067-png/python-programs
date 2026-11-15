
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File opened")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")
        return False


with FileManager("student.txt", "w") as f:
    f.write("Welcome to Python OOP")

print("Writing completed")
