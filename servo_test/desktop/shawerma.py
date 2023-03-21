from time import sleep
import serial

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', 
                    level=logging.INFO)

port = '/dev/ttyUSB0'
baudrate = 9600

def main():
    ser = serial.Serial(port, baudrate, timeout=1)
    sleep(1)

    logging.info('connected to something on {}'.format(port))

    while True:
        try:
            rotation_angle = int(input())
        except ValueError:
            logging.error('не цифорка')
            continue

        if not 0 <= rotation_angle <= 180:
            logging.error('фаза это ноль')
            continue
        
        ser.write(rotation_angle.to_bytes(1, 'little'))

if __name__ == '__main__':
    main()