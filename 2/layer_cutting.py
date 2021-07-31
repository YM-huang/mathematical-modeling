# 零件 每层可放置数量(个) 生产任务(件) 完成生产任务所需要的层数(层)
# LJ1 6231            1272000    205
# LJ2 7471            1521000    204
# LJ3 2387            1161000    487
# LJ4 4347            3229500    743
# LJ5 4928            2434500    495
# LJ6 5452            2421000    445

import math

# 每种材料体积
VLJ1 = 75306
VLJ2 = 62800
VLJ3 = 191037.6
VLJ4 = 105629.6
VLJ5 = 94985
VLJ6 = 84905.6

# 立方体长宽高
length = 6060 * 0.97
width = 2160
height = 240

# 立方体体积
VC = length * width * height

# 每层可切割的零件数
# ins = [6417, 7688, 2465, 4494, 5063, 5617]
# ins = [6231, 7471, 2387, 4347, 4928, 5452]
ins = [6014, 7254, 2310, 4221, 4770, 5288]

# 生产任务
tar = [1272000, 1521000, 1161000, 3229500, 2434500, 2421000]

# 需要的层数
lay = []
for i in range(len(ins)):
    lay.append(math.ceil(tar[i]/ins[i]))

# 每种材料切割后剩余数量
remain = []
for i in range(len(ins)):
    remain.append(lay[i]*ins[i]-tar[i])
print(remain)

# LJ1 LJ2剩余层数
n1 = lay[1]//3
r1 = lay[0] - n1 * 3
r2 = lay[1] - n1 * 3
print(r1)
print(r2)

# LJ3 LJ5剩余层数
n2 = lay[2]//3
r3 = lay[2] - n2 * 3
r4 = lay[4] - n2 * 3
print(r3)
print(r4)

# LJ4剩余层数
n3 = lay[3]//6
r5 = lay[3] - n3 * 6
print(r5)

# LJ6剩余层数
n4 = lay[5]//6
r6 = lay[5] - n4 * 6
print(r5)

print("切割方案1:LJ1(3层)/LJ2(3层)  共:" + str(n1) + "块原材料，利用率:" + str((VLJ1*ins[0]+VLJ2*ins[1])*3/VC) + "  共分别生产LJ1:" + str(ins[0]*n1*3) + "  LJ2:" + str(ins[1]*n1*3))
print("切割方案2:LJ3(3层)/LJ5(3层)  共:" + str(n2) + "块原材料，利用率:" + str((VLJ3*ins[2]+VLJ5*ins[4])*3/VC) + "  共分别生产LJ3:" + str(ins[2]*n2*3) + "  LJ5:" + str(ins[4]*n2*3))
print("切割方案3:LJ4(6层)  共:" + str(n3) + "块原材料，利用率:" + str(VLJ4*ins[3]*6/VC) + "  共生产LJ4:" + str(ins[3]*n3*6))
print("切割方案4:LJ6(6层)  共:" + str(n4) + "块原材料，利用率:" + str(VLJ6*ins[5]*6/VC) + "  共生产LJ6:" + str(ins[5]*n4*6))
print("切割方案5:LJ5(2层)/LJ4(1层)/LJ6(1层)/LJ1(1层)/LJ3(1层)  共:" + str(5) + "块原材料，利用率:" + str(((VLJ5*ins[4]*2+VLJ4*ins[3]+VLJ6*ins[5]+VLJ1*ins[0]+VLJ3*ins[2])*5)/(VC*5)) + "  共分别生产LJ5:" + str(ins[4]*5*2) + "  LJ4:" + str(ins[3]*5) + "  LJ6:" + str(ins[5]*5) + "  LJ1:" + str(ins[0]*5) + "  LJ3:" + str(ins[2]*5))

print("总利用率:" + str(((VLJ1*ins[0]+VLJ2*ins[1])*3+(VLJ3*ins[2]+VLJ5*ins[4])*3++VLJ4*ins[3]*6+VLJ6*ins[5]*6+(VLJ5*ins[4]*2+VLJ4*ins[3]+VLJ6*ins[5]+VLJ1*ins[0]+VLJ3*ins[2])*5)/(VC*9)))

# -(VLJ5*ins[4]+VLJ1*ins[0]*4+VLJ3*ins[2]*4)