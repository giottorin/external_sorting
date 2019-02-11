import os
import re
#import time



print("Reverse sort? (y/N)", end= ' ')
st = input()
reverse_sort = "Y" == st.upper()



print("Splitters:", end=' ')
separators = input()


def make_regexp_for_split(separators):
    if separators == '':
        separators = " "
    if len(separators) == 1:
        if separators == '[':
            return  re.compile("\[")
        if separators == ']':
            return re.compile("\]")
    return re.compile(separators)

regexp_for_split = make_regexp_for_split(separators)


def read_lines(f, size):
    import sys

    part = []

    while sys.getsizeof(part) < size:
        s = f.readline()
        if s == '':
            break
        part.append(s)

    return part


def split_file(name, part_size):
    parts_names = []

    f = open(name, 'r')

    not_end = True

    while not_end:

        part = read_lines(f, part_size)

        if len(part) == 0:
            break

        part_name = 'part' + str(len(parts_names))

        part_file = open(part_name, 'w')

        for i in part:
            part_file.write(i)

        part_file.close()

        parts_names.append(part_name)

        if (f.tell() == os.fstat(f.fileno()).st_size) :
            not_end = False

    f.close()
    return parts_names


def sort_strings(arr):
    new_arr = []
    for s in arr:
        new_arr.append(re.split(regexp_for_split, s))
        new_arr[len(new_arr) - 1].append(s)
    new_arr.sort(reverse=reverse_sort)
    arr = []
    for s in new_arr:
        arr.append(s.pop())
    return arr


def sort_nums(arr):
    new_arr = []
    for s in arr:
        new_arr.append(re.split(regexp_for_split, s))
        new_arr.append([int(x) for x in new_arr.pop()])
        new_arr[len(new_arr) - 1].append(s)
    new_arr.sort(reverse=reverse_sort)
    arr = []
    for s in new_arr:
        arr.append(s.pop())
    return arr


def check_strings_or_nums_in_arr(file_name):
    with open(file_name, 'r') as f:
        arr = f.readlines()
        try:
            for i in arr:
                for j in re.split(regexp_for_split, i):
                    int(j)
        except ValueError:
            print(False)
            return False
#    print(True)
    return True



def sort_file(file_name):
    file = open(file_name, 'r')

    lines = []

    for s in file.readlines():
        lines.append(s)

    file.close()

    if sort_like_nums:
        lines = sort_nums(lines)
    else:
        lines = sort_strings(lines)

    file = open(file_name, 'w')
    for i in lines:
        file.write(str(i))
    file.close()


def merge(part_names, out_name):
    out_file = open(out_name, 'w')
    mass = []
    for i in part_names:
        part = open(i, 'r')
        mass.append(part)

    parts = []
    for i in mass:
        parts.append(i.readline())

    while parts != [''] * len(parts):

        idx = None

        for i, v in enumerate(parts):
            if v == '':
                continue

            if not reverse_sort:
                if idx is None or v < parts[idx]:
                    idx = i
            else:
                if idx is None or v > parts[idx]:
                    idx = i

        out_file.write(str(parts[idx]))

        parts[idx] = mass[idx].readline()

    for i in mass:
        i.close()

    out_file.close()


print('File name:', end= ' ')
name_of_file = input()
print('Memory limit (in bytes):', end= ' ')
parts_size = int(input())

#start_time = time.time()
sort_like_nums = check_strings_or_nums_in_arr(name_of_file)

parts = split_file(name_of_file, parts_size)
for f in parts:
    sort_file(f)


merge(parts, 'sorted')


def delete_files():
    dir = os.getcwd()
    dirs = os.listdir(dir)
    for d in dirs:
        if re.match(r"part\d+", d) is not None:
            os.remove(d)


delete_files()
#print("--- %s seconds ---" % (time.time() - start_time))