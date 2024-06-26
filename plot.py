import numpy as np
import matplotlib.pyplot as plt

aa = np.load("/home/turtlebot/Sudhanshu_shankar/cf_code/cf_circle_cyper_nice_vclose_laptop.npy")
traj = np.load("/home/turtlebot/Sudhanshu_shankar/cf_code/gt.npy")
aa = aa.T
plt.plot(-aa[1,:],aa[0,:])
plt.plot(np.array(traj)[:,0] - 0.7 ,np.array(traj)[:,1]+0.7,':',alpha = 0.5)
plt.axis('equal')
plt.grid(True)
plt.show()

# aa = np.load("/home/turtlebot/Sudhanshu_shankar/cf_code/cf_circle_cyclic_persuit_r06_v02.npy")
# traj = np.load("/home/turtlebot/Sudhanshu_shankar/cf_code/gt.npy")
# aa = aa.T
# plt.plot(-aa[1,:],aa[0,:])
# plt.plot(np.array(traj)[:,0] - 0.7 ,np.array(traj)[:,1]+0.7,':',alpha = 0.5)
# plt.axis('equal')
# plt.grid(True)
# plt.show()

# controls = np.load("/home/turtlebot/Sudhanshu_shankar/cf_code/control_signals.npy")
# print(controls[0])
# plt.scatter(controls[:,0],controls[:,1],)
# # plt.axis('equal')
# plt.ylim((0,1))
# plt.xlim((0,4))
# plt.grid(True)
# plt.show()
