import serial
import time




class Game():
    def __init__(self, port="/dev/ttyUSB0", baud=115200):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)

        self.running = True

        self.puzzles = {}

    def send(self, node, command):
        msg = f"{node}:{command}\n"
        self.ser.write(msg.encode())

    def read_line(self):
        line = self.ser.readline().decode(errors="ignore").strip()
        return line

    def parse(self, line):
        try:
            _, node, event = line.split(":")
            return int(node), event
        except:
            return None, None
        
    def handle_event(self, node, event):
        pass

    def run(self):
        
        while self.running:
            line = self.read_line()

            if not line:
                continue

            node, event = self.parse(line)

            if node is None:
                continue

            self.handle_event(node, event)




if __name__ == "__main__":
    game = Game()
    game.run()
