# this 
class CustomOpen:
    """this is a custom context manager for file operations.
    It opens a file in the specified mode and ensures it is closed after use.   
    If an exception occurs, it prints the exception message.
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
        return True

if __name__ == "__main__":
    # Example usage of CustomOpen
    with CustomOpen("example.txt", "w") as f:
        f.write("Hello, world!")
        print("File written successfully.")
        
    with CustomOpen("example.txt", "r") as f:
        content = f.read()
        raise Exception("This is a test exception")
        print("Read content:", content)

