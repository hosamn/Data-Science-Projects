import csv
import datetime as dt
import matplotlib.pyplot as plt

with open('potus_visitors_2015.csv') as f:
    potus = list(csv.reader(f))

print('Got potus list of lists')

# 0. name
# 1. appt_made_date
# 2. appt_start_date
# 3. appt_end_date
# 4. visitee_namelast
# 5. visitee_namefirst
# 6. meeting_room
# 7. description


for i in potus[1:]:
    i[2] = dt.datetime.strptime(i[2], '%m/%d/%y %H:%M')
    i[3] = dt.datetime.strptime(i[3], '%m/%d/%y %H:%M')
    i.append(i[3] - i[2])
    if i[8] > dt.timedelta(days=16):
        print('appt made in', i[1],
              'to meet with', i[5],
              'in', i[6], 'by', i[0])

# print('Got datetimes in potus')

# visit_len = [i[8] for i in potus[1:]]

# print('Got list of visit lenths')

# max_length = max(visit_len)
# min_length = min(visit_len)

# print('Min visit time', min_length,
#       '\n  it happened', visit_len.count(min_length), 'times',
#       '\n  Visitor was:\n', [i[0] for i in potus if min_length in i])

# print('Max visit time', max_length,
#       'and it happened', visit_len.count(max_length), 'times'
#       '\n  Visitor was:\n', [i[0] for i in potus if max_length in i])

# visit_his = {i: visit_len.count(i) for i in visit_len}

# for k, v in visit_his.items():
#     print(v, k)


# ipython -pylab
# li = [i.seconds for i in visit_len]
# plt.hist(li)

# plt.figure()
# plt.plot()
