#coding=utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
number_time = {}

for index in range(len(calls)):
    if calls[index][0] not in number_time:
        number_time[calls[index][0]] = int(calls[index][3])
    elif calls[index][0] in number_time:
        number_time[calls[index][0]] += int(calls[index][3])
    elif calls[index][1] not in number_time:
        number_time[calls[index][1]] = int(calls[index][3])
    elif calls[index][1] in number_time:
        number_time[calls[index][1]] += int(calls[index][3])

maxnum_time = [0,0]
for index in number_time:
    if number_time[index] > maxnum_time[1]:
        maxnum_time[0] = index
        maxnum_time[1] = number_time[index]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxnum_time[0],maxnum_time[1]))
