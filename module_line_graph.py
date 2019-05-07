# -*-coding:utf-8-*-
# 折线图

import matplotlib.pyplot as plt
import numpy as np
import data_source

table_title = '我的话费统计'
table_x_label = '时间'
table_y_label = '话费金额（单位：元）'

mobile_176xxxx4617 = data_source.mobile_176xxxx4617
mobile_155xxxx9617 = data_source.mobile_155xxxx9617
mobile_173xxxx9636 = data_source.mobile_173xxxx9636
time = data_source.time

fig, ax = plt.subplots()

ax.plot(time, mobile_176xxxx4617, label='176xxxx4617')
ax.plot(time, mobile_155xxxx9617, label='155xxxx9617')
ax.plot(time, mobile_173xxxx9636, label='173xxxx9636')

ax.legend()

plt.title(table_title)
plt.xlabel(table_x_label)
plt.ylabel(table_y_label)

# 遍历每一个点，使用text将y值显示
for i, j in list(zip(time, mobile_176xxxx4617)):
    plt.text(i, j + 1, j, fontsize=12)

for i, j in list(zip(time, mobile_155xxxx9617)):
    plt.text(i, j + 1, j, fontsize=12)

for i, j in list(zip(time, mobile_173xxxx9636)):
    plt.text(i, j + 1, j, fontsize=12)

# 纵轴范围区间
my_y_ticks = np.arange(0, 75, 5)
plt.yticks(my_y_ticks)

def show_plt():
    plt.show()
