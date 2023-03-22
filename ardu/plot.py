import os

import matplotlib.pyplot as plt


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt))
    os.chdir(pwd)
    plt.close()


def readData(path="results.txt"):
    with open(path, "r") as results_file:
        arr: list = results_file.readlines()
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    answer = dict()
    for i in range(1, len(arr)):
        stringFromTable = arr[i]
        classWithName = stringFromTable[0].split(sep=".")
        clas = classWithName[0]
        graphics = classWithName[1]
        if graphics not in answer:
            answer[graphics] = dict()
        dic = answer[graphics]
        if clas == "DifferentThreadsBenchmarking":
            name = f"ThreadAmount{int(stringFromTable[2])}"
            if not (name in dic):
                dic[name] = ([], [])
            amount = int(stringFromTable[1])
            dic[name][0].append(amount)
            dic[name][1].append(amount * float(stringFromTable[5].replace(",", ".")))
        elif clas == "DifferentTypesBenchmarking":
            name = classWithName[-1]
            if not (name in dic):
                dic[name] = ([], [])
            amount = int(stringFromTable[1])
            dic[name][0].append(amount)
            dic[name][1].append(amount * float(stringFromTable[5].replace(",", ".")))
        else:
            print("Wrong class", clas)
    return answer


def drawPlot(data: dict, title):
    print(data)
    for name, (size, throughput) in data.items():
        plt.plot(size, throughput, label=name)
    plt.title(title)
    plt.grid(True)
    plt.xlabel("Amount of numbers")
    # plt.ylim(0, 150000)
    plt.ylabel("Numbers per seconds")
    plt.xscale('log')
    plt.legend(loc='upper center')


def plots(arr: dict):
    for name, data in arr.items():
        drawPlot(data, name)
        save(name)
        plt.clf()
    plt.close()


plots(readData())
# drawPlot(readData())
# plt.show()


# plt.plot(x, f, label=u'Сумма cos и sin')
# plt.plot(x, y, label=u'Произведение cos и sin')
# plt.plot(xz, yz, label=u'Кардиоида')
#
# plt.grid(True)
# plt.xlabel(u'Число чисел')
# plt.ylabel(u'Пропускная способность')
# plt.title(u'Графики пропускных способностей')
#
# plt.legend()  # легенда для всего рисунка fig
#
# save('pic_12_1_1', fmt='png')
#
# plt.show()
