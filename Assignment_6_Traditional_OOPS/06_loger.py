class Logger:
    def __init__(self):
        print("Logger Object Created")

    def __del__(self):
        print("Logger object destroyed")

log = Logger()
del log
