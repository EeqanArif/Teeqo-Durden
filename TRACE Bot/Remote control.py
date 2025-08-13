import serial, sys, termios, tty

ARDUINO_PORT = '/dev/ttyACM1'
def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try: tty.setraw(fd); ch = sys.stdin.read(1)
    finally: termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    ser = serial.Serial(ARDUINO_PORT, 9600)
    while True:
        char = get_char()
        if char == 'q': break
        if char in ['w','a','s','d','x','c','v','b']:
            ser.write(char.encode())
    ser.close()
main()
