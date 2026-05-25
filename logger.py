class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.file = open("app.log", "a")
        return cls._instance

    def log(self, message):
        print(message)
        self.file.write(message + "\n")
        self.file.flush()