
import numpy as np
import matplotlib.pyplot as plt
import mpltex

# @mpltex.acs_decorator
# def my_plot():
#     fig, ax = plt.subplots(1)
#     linestyles = mpltex.linestyle_generator()
#
#     ax.scatter(141, 28.14, color='tomato', label='CNN+LSTM')
#     ax.scatter(237, 31.92, color='orange', label='HieCoAttenVQA')
#     ax.scatter(297, 38.002, color='gold', label='Learning2Reason')
#     ax.plot([401, 591, 680], [55.917411, 62.2909381, 64.0216593],
#             #linestyle='--', marker='o', color='navy',
#             label='OursRL ($\gamma$=0.01, 0.5, 0.99)',
#             **next(linestyles))
#     ax.hlines(65.8452064, 0, 750, color='khaki', linestyles='--',
#               label='AllTasks')
#     ax.axis([0, 750, 10, 75])
#     #ax.legend(loc='lower right', fontsize=12)
#     # plt.title('Inference Time vs. Accuracy', fontsize=20)
#     #plt.xlabel('CPU Time (ms)', fontsize=15)
#     #plt.ylabel('Accuracy (%)', fontsize=15)
#     #plt.show()
#
#     # ax.plot(t, t, label='$t$', **next(linestyles))
#     # ax.plot(t, t**2, label='$t^2$', **next(linestyles))
#     # ax.plot(t, t**3, label='$t^3$', **next(linestyles))
#     # ax.plot(t, t**4, label='$t^4$', **next(linestyles))
#     # ax.plot(t, np.log(1+t), label='$\ln(1+t)$', **next(linestyles))
#     # ax.plot(t, t**(1./2), label='$t^{1/2}$', **next(linestyles))
#     # ax.plot(t, t**(1./3), label='$t^{1/3}$', **next(linestyles))
#
#     ax.set_xlabel('CPU Time (ms)')
#     ax.set_ylabel('Accuracy (\%)')
#     ax.legend(loc='lower right',)
#     fig.tight_layout(pad=0.1)
#     #fig.savefig('mpltex-acs-line-markers')
#     plt.savefig('mpltex-acs-line-markers.eps', format='eps', dpi=1000)
#     #fig.show()
#
# #t = np.arange(0, 1.0+0.05, 0.05)
# my_plot()
# # plt.close('all')


plt.scatter(141,28.14, color='tomato', label='CNN+LSTM')
plt.scatter(237,31.92, color='orange', label='HieCoAttenVQA')
plt.scatter(297,38.002, color='gold', label='Learning2Reason')
plt.plot([401,591,680], [55.917411,62.2909381,64.0216593], linewidth=3, linestyle='--', marker='o', color='navy', label='OursRL ($\gamma$=0.01, 0.5, 0.99)')
plt.hlines(65.8452064,0,750, linewidth=3, color='khaki',linestyles='--', label='AllTasks')
plt.axis([0, 750, 10, 75])
plt.legend(loc='lower right',fontsize=14)
# plt.title('Inference Time vs. Accuracy', fontsize=20)
plt.xlabel('CPU Time (ms)', fontsize=15)
plt.ylabel('Accuracy (%)', fontsize=15)
plt.tight_layout(pad=0.1)
#plt.show()
#plt.savefig('TimevsAcc.eps', format='eps', dpi=1000)
plt.savefig('TimevsAcc.eps', format='eps', dpi=1000)