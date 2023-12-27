import csv
import matplotlib.pyplot as plt
import time
import os
import pathlib
import math

csv_name = 'log_0.3_2.csv'

folder = f'{int(time.time())}'
os.mkdir(folder)


def avg(*args):
    return sum(args) / len(args)


def read_model_file(file_name):
    res = []

    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            t, m, Vy, h = map(float, map(str.strip, row))
            res.append((t, m, Vy, h))

    return res


def read_ksp_file(file_name, max_t):
    res = []

    with open(file_name) as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            t, m, h, Vy = map(float, map(str.strip, row))
            t -= 35.41

            if t < 0:
                continue

            if t > max_t:
                break

            res.append((t, m, Vy, h))

    return res


ksp_file = read_ksp_file('log_1702930921.csv', 106)
model_file = read_model_file(csv_name)


def make_plot(name, x, y, y2, ylabel):
    length = min(len(x), len(y), len(y2))
    x = x[:length]
    y = y[:length]
    y2 = y2[:length]

    plt.cla()
    plt.clf()
    plt.title(f'{name}')
    plt.xlabel("время, c")
    plt.ylabel(ylabel)
    plt.plot(x, y, '-r', label="KSP")
    plt.plot(x, y2, label="Мат. модель")
    plt.legend()
    plt.savefig(f'{folder}/{pathlib.Path(csv_name).name}_{name}.png')


def select_by_time(func):
    res = []

    max_t = min(ksp_file[-1][0], model_file[-1][0])

    for t, m, h, Vy in ksp_file:
        if t > max_t:
            break
        model_line = next(filter(lambda a: a[0] > t, model_file))
        res.append(func(model_line))

    return res


make_plot('Масса', [row[0] for row in ksp_file], [row[1] for row in ksp_file], select_by_time(lambda l: l[1]), "масса, кг")
make_plot('Скорость', [row[0] for row in ksp_file], [row[2] for row in ksp_file], select_by_time(lambda l: l[2]), "скорость, м/с")
make_plot('Высота', [row[0] for row in ksp_file], [row[3] for row in ksp_file], select_by_time(lambda l: l[3]), "высота, м")
