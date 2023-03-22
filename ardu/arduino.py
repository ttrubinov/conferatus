import json
import time
from itertools import count

import serial


def getConfig():
    try:
        with open("ardu/config.txt", "r") as f:
            dct = json.load(f)
            print(dct)
    except FileNotFoundError:
        dct = dict()
        dct["last"] = 0
        with open("ardu/config.txt", "w") as f:
            print(json.dumps(dct), file=f)
    return dct


# make sure the 'COM#' is set according the Windows Device Manager


def getSerialData(end):
    arr = []
    flag = True
    with serial.Serial('COM4', 19200, timeout=1) as ser:
        time.sleep(3)
        ser.write(b'start')

        start = time.time_ns()
        print("Started")
        for i in count():
            line = ser.readline()  # read a byte
            if line:
                string: str = line.decode()  # convert the byte string to a unicode string
                string = " ".join(string.strip().split())
                print(string)
                if "A" in string or "E" in string:
                    if "ALARM" in string:
                        break
                    if "END" in string:
                        ser.write(b'continue')
                        print("End, continue")
                        continue
                arr.append(string)
        end = time.time_ns()
    return arr


def saveData(dct, arr):
    lst = dct["last"]
    with open(f"ardu/sample{lst}.txt", "w") as outputFile:
        print(*arr, "End", sep="\n", file=outputFile)

    dct["last"] = dct["last"] + 1
    with open("config.txt", "w", encoding='utf-8') as f:
        print(json.dumps(dct), file=f)


def main():
    dct = getConfig()
    arr = getSerialData(50)
    saveData(dct, arr)


if __name__ == '__main__':
    main()
