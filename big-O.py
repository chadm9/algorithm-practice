
import datetime


def n_complexity():
    for i in range(1,100000):
        print i*1



def n2_complexity():
    for i in range(1, 2000):
        for j in range(1, 2000):
            print (str(i) + ', ' + str(j))




def factorial(n):
    result = n
    if n == 2:
        return 2

    result = result*factorial(result-1)

    return result

#print factorial(5)

# def run_program():
#     n2_complexity()
#
# start_time = datetime.datetime.now()
# run_program()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("This program ran in " + str(duration))

def x_to_n(x,n):
    result = x

    for i in range(1, n):
        result = result*x

    return result

print x_to_n(5,3)





def x_times_y(x,y):
    result = 0

    for i in range(1, y+1):
        result += x

    return result


print x_times_y(5,7)



def rec_x_to_n(x,n):
    result = x
    if n == 1:
        return x
    else:
        result = result*rec_x_to_n(x, n-1)

    return result

print rec_x_to_n(5,3)



def rec_x_times_y(x,y):
    result = x
    if y == 1:
        return x
    else:
        result =  result + rec_x_times_y(x, y-1)
    return result

print rec_x_times_y(5,4)