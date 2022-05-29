#Найти НОК двух чисел

'''num1 = int(input())
num2 = int(input())
nok = 1
while (nok % num1 != 0) | (nok % num2 != 0):
    nok += 1
print(nok)'''

#Вычислить число Пи c заданной точностью d
#Пример: при d = 0.001,  c= 3.141.

'''import math
def ost(d):
    n = d.find('.')
    count = len(d) - n - 1
    return count

num = input()
h = ost(num)
h = int(h)
p = math.pi
p = str('{:.{}f}'.format(p, h))
k = ''
for i in range(h+2):
    k += p[i]
print(k)'''

#Составить список простых множителей натурального числа N
'''def list(arr, n):
    while n > 1:
        q = 2
        if n % q > 0:
            while n % q != 0:
                q += 1
        n = n / q
        arr.append(q)
    return arr

array = []
num = int(input('Введите натуральное число: '))
print(list(array, num))'''

#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

'''def create_array(arr):
    a = input('Введите натуральное число, если захотите закончит введите "end": ')
    while a != 'end':
        a = int(a)
        arr.append(a)
        a = input('Введите натуральное число, если захотите закончит введите "end": ')
    return arr

def sort_list(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] not in arr2:
                arr2.append(arr1[i])
    return arr2

array1 = []
create_array(array1)
array2 = [array1[0]]
print(sort_list(array1, array2))'''

#Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

'''def creat_file():
    with open('file.txt', 'a') as nums:
        a = input('Введите натуральное число, если захотите закончит введите "end": ')
        while a != 'end':
            nums.write(a + '\n')
            a = input('Введите натуральное число, если захотите закончит введите "end": ')

def del_num_chet():
    with open("file.txt", "r") as f:
        lines = f.readlines()
    with open("file.txt", "w") as f:
        for line in lines:
            if int(line.strip("\n")) % 2 != 0:
                f.write(line)

creat_file()
del_num_chet()'''

        


    