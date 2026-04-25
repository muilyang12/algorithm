class Logger:
    def __init__(self):
        self.mesage_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mesage_timestamp:
            self.mesage_timestamp[message] = timestamp

            return True
        else:
            if timestamp >= self.mesage_timestamp[message] + 10:
                self.mesage_timestamp[message] = timestamp

                return True
            else:
                return False
