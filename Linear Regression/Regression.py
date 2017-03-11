import sys
import math
import time

# calculate the deviation value
def dev_cal(y, x1, x2, x3, x4, x5, x6, term):
    # basic terms: c, w0, w1, w2, w3, w4, w5, w6
    if term == 0:
        term = 1
    elif term == 1:
        term = x1
    elif term == 2:
        term = x2
    elif term == 3:
        term = x3
    elif term == 4:
        term = x4
    elif term == 5:
        term = x5
    elif term == 6:
        term = x6
    params = {}
    params['c'] = -2 * term * y
    params['w0'] = 2 * term * 1 # suppose x0 is always equal to 1, a const term
    params['w1'] = 2 * term * x1
    params['w2'] = 2 * term * x2
    params['w3'] = 2 * term * x3
    params['w4'] = 2 * term * x4
    params['w5'] = 2 * term * x5
    params['w6'] = 2 * term * x6

    return params

# create an empty polynomial whose initial values are set to zero on all terms
def create_params():
    params = {}
    params['c'] = 0
    params['w0'] = 0
    params['w1'] = 0
    params['w2'] = 0
    params['w3'] = 0
    params['w4'] = 0
    params['w5'] = 0
    params['w6'] = 0

    return params

def set_poly_terms(x_list):
    poly_terms = {}
    poly_terms['c'] = 0
    poly_terms['w0'] = x_list[0]
    poly_terms['w1'] = x_list[1]
    poly_terms['w2'] = x_list[2]
    poly_terms['w3'] = x_list[3]
    poly_terms['w4'] = x_list[4]
    poly_terms['w5'] = x_list[5]
    poly_terms['w6'] = x_list[6]

    return poly_terms

# calculate the deviation respective to specific term (w0, w1 or ... w6)
def get_deviation(term):
    cu_params = create_params()
    for i in range(0, len(y)):
        params = dev_cal(y[i], x1[i], x2[i], x3[i], x4[i], x5[i], x6[i], term)
        cu_params['c'] += params['c']
        cu_params['w0'] += params['w0']
        cu_params['w1'] += params['w1']
        cu_params['w2'] += params['w2']
        cu_params['w3'] += params['w3']
        cu_params['w4'] += params['w4']
        cu_params['w5'] += params['w5']
        cu_params['w6'] += params['w6']

    return cu_params

# used for test sample with only 2 varibles
def poly_val(w0, w1, poly_terms):
    value = w0 * poly_terms['w0'] + w1 * poly_terms['w1'] + poly_terms['c']

    return value

# used for the main problem where there are 7 varibles
def poly_val2(w_list, poly_terms):
    value = w_list[0] * poly_terms['w0'] + w_list[1] * poly_terms['w1'] + w_list[2] * poly_terms['w2'] + w_list[3] * poly_terms['w3'] + w_list[4] * poly_terms['w4'] + w_list[5] * poly_terms['w5'] + w_list[6] * poly_terms['w6'] + poly_terms['c']

    return value

# this is where we perform the Gradient Descent Algorithms to update the values of w_list: w0 ~ w6
def grad2(w_list, dev_list, step):
    new_w_list = [0, 0, 0, 0, 0, 0, 0]

    new_w_list[0] = w_list[0] - step * poly_val2(w_list, dev_list[0])
    new_w_list[1] = w_list[1] - step * poly_val2(w_list, dev_list[1])
    new_w_list[2] = w_list[2] - step * poly_val2(w_list, dev_list[2])
    new_w_list[3] = w_list[3] - step * poly_val2(w_list, dev_list[3])
    new_w_list[4] = w_list[4] - step * poly_val2(w_list, dev_list[4])
    new_w_list[5] = w_list[5] - step * poly_val2(w_list, dev_list[5])
    new_w_list[6] = w_list[6] - step * poly_val2(w_list, dev_list[6])

    return new_w_list

def is_stop_condition(w_list, dev_list):
    target = 1
    dev0 = poly_val2(w_list, dev_list[0])
    print 'deviation of w0: ' + str(dev0)
    dev1 = poly_val2(w_list, dev_list[1])
    print 'deviation of w1: ' + str(dev1)
    dev2 = poly_val2(w_list, dev_list[2])
    print 'deviation of w2: ' + str(dev2)
    dev3 = poly_val2(w_list, dev_list[3])
    print 'deviation of w3: ' + str(dev3)
    dev4 = poly_val2(w_list, dev_list[4])
    print 'deviation of w4: ' + str(dev4)
    dev5 = poly_val2(w_list, dev_list[5])
    print 'deviation of w5: ' + str(dev5)
    dev6 = poly_val2(w_list, dev_list[6])
    print 'deviation of w6: ' + str(dev6)

    # set a loose target for constant term w0 since it has less impact in this problem
    # other w1, w2, ... w6 are set with the target value for stop condition
    if abs(dev0) < 55 and abs(dev1) < target and abs(dev2) < target and abs(dev3) < target and abs(dev4) < target and abs(dev5) < target and abs(dev6) < target:
        return True
    else:
        return False

# initial the y (crime rate) and x terms (x1 ~ x6) values for training data
y = [478, 494, 643, 341, 773, 603, 484, 546, 424, 548, 506, 819, 541, 491, 514, 371, 457, 437, 570, 432, 619, 357, 623, 547, 792, 799, 439, 867, 912, 462, 859, 805, 652, 776, 919, 732, 657, 1419, 989, 821, 1740, 815, 760, 936, 863, 783, 715, 1504, 1324, 940]
x1 = [184, 213, 347, 565, 327, 260, 325, 102, 38, 226, 137, 369, 109, 809, 29, 245, 118, 148, 387, 98, 608, 218, 254, 697, 827, 693, 448, 942, 1017, 216, 673, 989, 630, 404, 692, 1517, 879, 631, 1375, 1139, 3534, 706, 451, 433, 601, 1024, 457, 1441, 1022, 1244]
x2 = [40, 32, 57, 31, 67, 25, 34, 33, 36, 31, 35, 30, 44, 32, 30, 16, 29, 36, 30, 23, 33, 35, 38, 44, 28, 35, 31, 39, 27, 36, 38, 46, 29, 32, 39, 44, 33, 43, 22, 30, 86, 30, 32, 43, 20, 55, 44, 37, 82, 66]
x3 = [74, 72, 70, 71, 72, 68, 68, 62, 69, 66, 60, 81, 66, 67, 65, 64, 64, 62, 59, 56, 46, 54, 54, 45, 57, 57, 61, 52, 44, 43, 48, 57, 47, 50, 48, 49, 72, 59, 49, 54, 62, 47, 45, 48, 69, 42, 49, 57, 72, 67]
x4 = [11, 11, 18, 11, 9, 8, 12, 13, 7, 9, 13, 4, 9, 11, 12, 10, 12, 7, 15, 15, 22, 14, 20, 26, 12, 9, 19, 17, 21, 18, 19, 14, 19, 19, 16, 13, 13, 14, 9, 13, 22, 17, 34, 26, 23, 23, 18, 15, 22, 26]
x5 = [31, 43, 16, 25, 29, 32, 24, 28, 25, 58, 21, 77, 37, 37, 35, 42, 21, 81, 31, 50, 24, 27, 22, 18, 23, 60, 14, 31, 24, 23, 22, 25, 25, 21, 32, 31, 13, 21, 46, 27, 18, 39, 15, 23, 7, 23, 30, 35, 15, 18]
x6 = [20, 18, 16, 19, 24, 15, 14, 11, 12, 15, 9, 36, 12, 16, 11, 14, 10, 27, 16, 15, 8, 13, 11, 8, 11, 18, 12, 10, 9, 8, 10, 12, 9, 9, 11, 14, 22, 13, 13, 12, 15, 11, 10, 12, 12, 11, 12, 13, 16, 16]

# test data
test_x1 = [999, 576, 2304, 382, 738, 1723, 827, 182, 382, 1129]
test_x2 = [33, 76, 92, 27, 37, 33, 73, 29, 47, 49]
test_x3 = [50, 20, 81, 74, 67, 51, 78, 41, 39, 48]
test_x4 = [12, 21, 32, 17, 8, 25, 21, 31, 9, 11]
test_x5 = [55, 43, 22, 30, 33, 17, 18, 21, 7, 9]
test_x6 = [30, 60, 10, 22, 13, 28, 31, 19, 7, 12]

# suppose we let the model equation be y = w0 + w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6 + E
# we want to find the minimum of E square = (y - (w0 + w1x1 + ... w6x6))^2 = y^2 -2y(w0 + w1x1 + .. w6x6) + (w0 + w1x1 + .. w6x6)^2
# the deviation of w0: -2y + 2w0 +2(w1x1 + w2x2 + ... w6x6)
# the deviation of w1: -2x1y + 2w1x1^2 +2x1(w0 + w2x2 + ... w6x6) = x1(-2y + 2(w0 + w1x1 + .. w6x6))
# the deviation of w2: -2x2y + 2w2x2^2 +2x2(w0 + w1x1 + ... w6x6)
# the deviation of w3: -2x3y + 2w3x3^2 +2x3(w0 + w1x1 + ... w6x6)
# the deviation of w4: -2x4y + 2w4x4^2 +2x4(w0 + w1x1 + ... w6x6)
# the deviation of w5: -2x5y + 2w5x5^2 +2x5(w0 + w1x1 + ... w6x6)
# the deviation of w6: -2x6y + 2w6x6^2 +2x6(w0 + w1x1 + ... w5x5)

# get deviation formula for each w0, w1, w2 ... w6
dev_w0 = get_deviation(0)
print dev_w0
dev_w1 = get_deviation(1)
print dev_w1
dev_w2 = get_deviation(2)
print dev_w2
dev_w3 = get_deviation(3)
print dev_w3
dev_w4 = get_deviation(4)
print dev_w4
dev_w5 = get_deviation(5)
print dev_w5
dev_w6 = get_deviation(6)
print dev_w6

# select the start point as close to the minimum point as possible
# thus could improve the cost time, the start point can be adjusted
# based on some initial runs
w_list = [0.93757, 0.33614, 3.98101, 3.09188, 9.46728, 3.21803, -4.68228]
dev_list = [dev_w0, dev_w1, dev_w2, dev_w3, dev_w4, dev_w5, dev_w6]

while True:
    # step distance set as 0.00000002
    # since this problem has very coefs on each terms, it is important to
    # select a small step size carefully, otherwise the process won't converge
    w_list = grad2(w_list, dev_list, 0.00000002)
    print 'w list:'
    print w_list
    if is_stop_condition(w_list, dev_list):
        print 'A stop condition is meet'
        break
    print ''
    # can remove the sleep delay to reduce the cost time
    #time.sleep(0.2)

# feed test data
print ''
print 'predicted test y (overall crime rate):'
for i in range(0, len(test_x1)):
    poly_terms = set_poly_terms([1, test_x1[i], test_x2[i], test_x3[i], test_x4[i], test_x5[i], test_x6[i]])
    print poly_val2(w_list, poly_terms)

sys.exit(0)
