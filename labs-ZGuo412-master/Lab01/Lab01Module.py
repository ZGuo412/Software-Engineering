import sys
import os
a = 1
def findLongest():
    C = [8]
    while int(C[len(C) - 1]) <= 1000000:
     #   print(C[len(C) - 1])
        if (int(int(C[len(C) - 1]) / 2) != (int(C[len(C) - 1]) / 2.0)):
            C.append(2 * int(C[len(C) - 1]))
        else:
            if(int((int(C[len(C) - 1]) - 1) / 3) != ((int(C[len(C) - 1]) - 1) / 3)):
                C.append(int(C[len(C) - 1]) * 2)
            else:
                C.append((int(C[len(C) - 1]) - 1) / 3)
    return(C[len(C) - 2])


def findSmallest():
    number = '125874'
    while True:
        t_n = 2 * int(number)
        t_n = str(t_n)
      #  print(sorted(number),sorted(t_n))
        if sorted(number) == sorted(t_n):
            tr_n = 3 * int(number)
            tr_n = str(tr_n)
      #      print(1)
            if sorted(tr_n) == sorted(number):
                t_n = 4 * int(number)
                t_n = str(t_n)
        #        print(2)
                if sorted(t_n) == sorted(number):
                    t_n = 5 * int(number)
                    t_n = str(t_n)
          #          print(3)
                    if sorted(t_n) == sorted(number):
                        t_n = 6 * int(number)
                        t_n = str(t_n)
                        if sorted(t_n) == sorted(number):
                            return number
        temp = int(number) + 1
     #   print(temp)
        number = str(temp)