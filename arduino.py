import json
import time

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
    with serial.Serial('COM3', 230400, timeout=1) as ser:
        time.sleep(3)
        ser.write(b'start')
        start = time.time_ns()
        print("Started")
        for i in range(0, 100000):
            line = ser.readline()  # read a byte
            if line:
                string: str = line.decode()  # convert the byte string to a unicode string
                string = " ".join(string.strip().split())
                if "A" in string:
                    print(string)
                    if "ALARM 0 0" in string:
                        start = time.time_ns()
                        continue
                    if i > 100:
                        print(string)
                        break
                # num = int(string)  # convert the unicode string to an int
                arr.append(string)
        print(i)
        end = time.time_ns()
        print(end-start)
        print(i*10**9/(end-start))
    return arr


def saveData(dct, arr):
    lst = dct["last"]
    with open(f"ardu/sample{lst}", "w") as outputFile:
        print(*arr, "End", sep="\n", file=outputFile)

    dct["last"] = dct["last"] + 1
    with open("ardu/config.txt", "w", encoding='utf-8') as f:
        print(json.dumps(dct), file=f)


def main():
    dct = getConfig()
    arr = getSerialData(50)
    saveData(dct, arr)


if __name__ == '__main__':
    main()
