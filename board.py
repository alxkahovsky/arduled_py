import serial


class Board(object):
    def __init__(self, port: str, speed: int):
        self.port = port
        self.speed = speed
        self.board = serial.Serial(port, speed)

    def check_data(self, data: bytearray):
        if not isinstance(data, bytearray):
            raise TypeError('Массив байтов!')

    def write(self, data: bytearray):
        self.check_data(data)
        self.board.write(data)


