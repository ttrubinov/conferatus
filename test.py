# import itertools
# a = itertools.count(start=10, step=1) # 10 11 12 13 14 15 16 17 18 19 20
# a = itertools.cycle(['1','2','3']) # 1 2 3 1 2 3 1 2 3 1 2 3
# a = itertools.repeat(([1],), times=100) # ([1],) ([1],) ([1],) ([1],)
# b = itertools.chain([1,2,3], ('5','6','7')) # 1 2 3 5 6 7
# b = itertools.combinations('1a5b', 3) # ('1', 'a', '5') ('1', 'a', 'b') ('1', '5', 'b') ('a', '5', 'b')
# b = itertools.combinations_with_replacement('1a~', 2) # ('1', '1') ('1', 'a') ('1', '~') ('a', 'a') ('a', '~') ('~', '~')
# #itertools.compress(data, selectors) - (d[0] if s[0]), (d[1] if s[1]),
# c = itertools.compress(["a", "b", "<"], selectors=[True, False, True])# a <
# c = itertools.dropwhile(lambda x: x % 2, [1,3,2,3,1,2]) # 2 3 1 2
# c = itertools.filterfalse(lambda x: (x%5==0) or (x%3==0), itertools.count(start=1, step = 1))
#
# #starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
# # print("#", end=" ")
# #itertools.takewhile(func, iterable) - элементы до тех пор, пока func возвращает истину.
# control = 501
# for i in c:
#     if control>500:
#         break
#     print(i, end=" ")
#     control+=1

# for x,y in zip([1,2,3],['a', 'b']):
#     print(x,y)
# for x,y in itertools.zip_longest([1,2,3],['a', 'b'], fillvalue='-'):
#     print(x,y)
# a = [1,2,3]
# b = ['a', 'b', 'c']
# c = [(y,x) for x, y in zip(a,b)]
# variable = print
# len = enumerate(itertools.cycle(range(-1, 1)))
# map = itertools.takewhile(lambda x: x[0]<15,len)
# for print in map:
#     variable(print)
# import re
# def print_last():
#     file_name = (("".join(itertools.takewhile(lambda x: x!='\\',(__file__)[::-1])))[::-1])
#     with open(file_name, "r") as f:
#         a = f.readlines()
#     string_for_exec = f"print ({a[-1]})"
#     exec(string_for_exec)
# text = "Gooogle, Gogle, Goooooogle"
# match = re.findall(r"o{2,5}", text)
# print_last()
# a = (i for i in range(0,20))
# b = zip(a, itertools.cycle(['a', 'b', 'c']))
# c = [f"{y}{x}" for x,y in b]
#
# import functools
# match

# import itertools
#
# cases1 = [i for i in range(1, 9)]
# cases4 = list(itertools.product(cases1, repeat=4))
#
# targetList = [(1 / 8) ** 4, (1 / 8) ** 3, 105 / 256, 21 / 512]
# n = len(cases4)
# iterList = [0] * 4
#
#
# def fooAll5(tup: tuple[int, int, int, int]):
#     return (tup[0] == tup[1]) and (tup[2] == tup[3]) and (tup[1] == tup[2]) and (tup[0] == 5)
#
#
# def fooAllAny(tup: tuple[int, int, int, int]):
#     return (tup[0] == tup[1]) and (tup[2] == tup[3]) and (tup[1] == tup[2])
#
#
# def fooDiff(tup: tuple[int, int, int, int]):
#     tmp = list(itertools.combinations(tup, r=2))
#     return sum([1 if (i, i) in tmp else 0 for i in tup]) == 0
#
#
# def calc(foo):
#     return (sum([1 if foo(x) else 0 for x in cases4])) / n
#
#
# def pairWiseDiff(tup: tuple[int, int, int, int]):
#     tmp = sorted(tup)
#     return (tmp[0] == tmp[1]) and (tmp[2] == tmp[3]) and (tmp[1] != tmp[2])
#
#
# iterList[0] = calc(fooAll5)
# iterList[1] = calc(fooAllAny)
# iterList[2] = calc(fooDiff)
# iterList[3] = calc(pairWiseDiff)
#
# delta = [x for x in zip(targetList, iterList)]
# print(delta)
# n = 1000
#
# import re
#
# pattern = r'((1(01*0)*1)|0)*'
# for i in range(0, 3 * n + 1, 1):
#     bi = bin(i)[2:]
#     fi = re.match(pattern, bi)
#     if (fi.span()[1] - fi.span()[0]) == len(bi):
#         print(i, i%3, bi, end= " ")
#         try:
#             print(int(str(fi.group()), base=2))
#         except ValueError:
#             print(None)
#         if (i%3):
#             raise ValueError
# #
#
# import random
#
# with open("txt.txt", mode="r") as f:
#     print(f"{random.random()}", file=f)
#
#
#
#
# import random
# import time
#
#
# def qsort(arr):
#     if not arr:
#         return arr
#     x = arr.pop(0)
#     return qsort([i for i in arr if i <= x]) + [x] + qsort([i for i in arr if i > x])
#
#
# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#
# l = []
# beg = time.time()
# for i in range(10000):
#     l.append(qsort([random.randint(0, 200_000) for i in range(45)]))
# print(time.time() - beg)
# l = []
# beg = time.time()
# for i in range(10000):
#     l.append(insertionSort([random.randint(0, 200_000) for i in range(45)]))
# print(time.time() - beg)
# [].sort()
# import itertools
#
# dice1 = [1, 2, 2, 2, 3, 4]
# dice2 = [1, 4, 4, 5, 6, 8]
# results = dict([(x, 0) for x in range(1, 1 + max(dice1) + max(dice2))])
# for x, y in itertools.product(dice1, dice2):
#     results[x + y] += 1
# print(results)
# for x, y in results.items():
#     print(f"{x}: {y}")
from scipy.fft import fft, ifft
import numpy as np
from scipy.fft import fft, fftfreq
import numpy as np
# Number of sample points
N = 600
# sample spacing
T = 1
T = 1
# x = np.linspace(0.0, N*T, N, endpoint=False)
#
# y = np.sin(50.0 * 2.0*np.pi*x) + 2*np.sin(30.0 * 2.0*np.pi*x) + 0*0.25*np.sin(25.0 * 2.0*np.pi*x)
arr = []
arr2 = []
for i in range(0, 100):
    x = i/80
    y = (i+np.pi)/5
    arr.append(50*np.sin(2 * np.pi * x)+5*np.sin(2 * np.pi * y))
    x = i/5
    y = (i+7)/25
    arr2.append(30*np.sin(3 * np.pi * x)+3*np.sin(2 * np.pi * y))
# arr = [5, 1, 6, 2, 1, 3]
N = len(arr)
y = np.array(arr)
yf = fft(y)
y2 = np.array(arr2)
yf2 = fft(y2)

xf = fftfreq(N, T)[:N//2]
print(xf, "\n\n\n")
print(2.0/N * np.abs(yf[1:N//2]), "\n", 2.0/N * np.abs(yf2[1:N//2]))
import matplotlib.pyplot as plt
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
plt.legend(['FFT', 'FFT w. window'])
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf2[1:N//2]), '-y')
plt.legend(['FFT2', 'FFT2 w. window'])
plt.grid()
plt.show()
