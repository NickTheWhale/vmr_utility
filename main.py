import serial
from serial import SerialException

# from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

from app import App

# constants
KIND = 'potato'


def main():
    app = App('Voicemeeter Remote')
    
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()


if __name__ == "__main__":
    main()
