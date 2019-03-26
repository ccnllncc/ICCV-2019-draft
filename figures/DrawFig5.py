# import matplotlib.pyplot as plt
#
# plt.scatter(141,28.14, color='tomato', label='CNN+LSTM')
# plt.scatter(237,31.92, color='orange', label='HieCoAttenVQA')
# plt.scatter(297,38.002, color='gold', label='Learning2Reason')
# plt.plot([401,591,680], [55.917411,62.2909381,64.0216593], linestyle='--', marker='o', color='navy', label='OursRL ($\gamma$=0.01, 0.5, 0.99)')
# plt.hlines(65.8452064,0,750, color='khaki',linestyles='--', label='AllTasks')
# plt.axis([0, 750, 10, 75])
# plt.legend(loc='lower right',fontsize=12)
# # plt.title('Inference Time vs. Accuracy', fontsize=20)
# plt.xlabel('CPU Time (ms)', fontsize=15)
# plt.ylabel('Accuracy (%)', fontsize=15)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

import mpltex

@mpltex.acs_decorator
def my_plot(t):
    fig, ax = plt.subplots(1)
    linestyles = mpltex.linestyle_generator()
    ax.plot(t, t, label='$t$', **next(linestyles))
    ax.plot(t, t**2, label='$t^2$', **next(linestyles))
    ax.plot(t, t**3, label='$t^3$', **next(linestyles))
    ax.plot(t, t**4, label='$t^4$', **next(linestyles))
    ax.plot(t, np.log(1+t), label='$\ln(1+t)$', **next(linestyles))
    ax.plot(t, t**(1./2), label='$t^{1/2}$', **next(linestyles))
    ax.plot(t, t**(1./3), label='$t^{1/3}$', **next(linestyles))

    ax.set_xlabel('$t$')
    ax.set_ylabel('$f(t)$')
    ax.legend(loc='best', ncol=2)
    fig.tight_layout(pad=0.1)
    fig.savefig('mpltex-acs-line-markers')
    # plt.savefig('mpltex-acs-line-markers', format='eps')
    #fig.show()

t = np.arange(0, 1.0+0.05, 0.05)
my_plot(t)
# plt.close('all')


#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#bar_positions=[1,2,3,4]
#bar_heights=[1,2,3,4]
#print(np.arange(len([2,2,3,4,5])+1))
#ax.bar(np.arange(len([2,2,3,4,5])),[1,2,3,4,5], 0.5)#设置x，y数据，区间
#ax.set_xticks([1,2,3,4,5,6])#设置x轴刻度
#ax.set_xticklabels([1,2,3,4,5], rotation=45)#设置x轴标签，旋转45度
#ax.set_yticks([1,2,3,4,5,6])#设置x轴刻度
#ax.set_yticklabels([1,2,3,4,5], rotation=45)#设置y轴标签，旋转45度
#ax.set_ylim(0, 7)#设置y轴范围
#ax.set_xlim(0, 7)#设置x轴范围，当然轴数据范围跟 坐标刻度不要冲突就好
##ax.set_facecolor("orange")#设置背景颜色为红色
#for a,b in zip(bar_positions,bar_heights):#显示数据标签
#    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
#plt.savefig('xxx.eps')#保存图片
#plt.show()
 
 
 