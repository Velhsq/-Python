import time

class TrafficLight:

    def __init__(self):
        self._color = 'color'

    def running(self):
        count = 0
        while count < 10:
            self._color = 'red'
            print(self._color)
            time.sleep(7)
            self._color = 'yellow'
            print(self._color)
            time.sleep(2)
            self._color = 'green'
            print(self._color)
            time.sleep(7)
            count += 1


tl = TrafficLight()
tl.running()