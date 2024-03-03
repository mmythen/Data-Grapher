import numpy as np
import matplotlib.pyplot as plt


def graph_relation(filename: str, name1: str, index1: int, name2: str, index2: int):

    file_handle = open(filename, 'r')
    file_handle.readline()

    x_to_y = {}

    x = []
    y = []

    for line in file_handle:
        line = line.split(',')

        x_val = float(line[index1])
        y_val = float(line[index2])

        if x_val in x_to_y:
            x_to_y[x_val].append(y_val)
        else:
            x_to_y[x_val] = [y_val]


    for key in x_to_y:
        sum = 0
        length = len(x_to_y[key])
        for num in range(length):
            sum += x_to_y[key][num]
        x_to_y[key] = sum/length


    for key in x_to_y:

        x.append(key)
        y.append(x_to_y[key])







    x = np.array(x)
    y = np.array(y)


    a, b = np.polyfit(x, y, 1)

    plt.scatter(x, y, color='purple')

    plt.xlabel(name1)
    plt.ylabel(name2)

    plt.plot(x, a*x+b, color='steelblue', linewidth='2')



    plt.show()


file = input('what is your filename? ')
name1 = input('what is your first data element? (x value) ')
index1 = int(input('what is its index in the data set? '))
name2 = input('what is your second data element? (y value) ')
index2 = int(input('what is its index in the data set? '))


graph_relation(file, name1, index1, name2, index2)
