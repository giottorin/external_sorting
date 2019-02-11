import re


#first test
done = len(re.findall(r"[\n']+?", open('sorted').read()))
undone = len(re.findall(r"[\n']+?", open('unsorted').read()))


if undone == done:
    print('first test passed');
else:
    print('first test fault');


#second test


# with open('sorted', 'r') as f:
#     previous = f.readline(0)
#     current = f.readline(0)
#     revers_ok = 2
#     revers_not_ok = 2
#     revers = 0
#
#     for i in range(4, done + 5):
#         previous = current
#         current = f.readline(i+1)
#
#         print(previous, 'p')
#         print(current,'c')
#
#         if previous >= current:
#             revers_ok +=1
#             print(i-4,'ok')
#         else:
#             revers_not_ok +=1
#             print(i - 4,'not ok')
#
# print(revers_ok)
# print (revers_not_ok)
# print (done)
# if ((revers_ok +1) == done) or (revers_not_ok == done):
#     print('second test passed')
# else:
#     print('second test fault')


with open('sorted', 'r') as f:

    first = f.readline()
    ok = 1
    not_ok = 1

    for line in f:
        if int(line) > int(first):
            ok+=1
        elif int(line) == int(first):
            not_ok +=1
            ok += 1
        else:
            not_ok += 1
        first = line




if (ok == done) or (not_ok == done):
    print ('second test passed')
else:
    print('second test fault')

