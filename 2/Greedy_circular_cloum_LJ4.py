# 椭圆高度差 横/竖
adh = 7.771
adv = 7.771

# 立方体长宽高
length = 6060
width = 2160
height = 240

# 椭圆横径竖径
td = 58
ver = 58

# 行列数
row: int = 0

arr: int = 0
arr1: int = 0
arr2: int = 0

# 并排排列（横排）b
while row * ver <= width:
    row = row + 1
while arr * td <= length:
    arr = arr + 1

row -= 1
arr -= 1
print('在' + str(length) + '*' + str(width) + '视图中：\n并排排列（横排）可以容纳' + str(row * arr) + '个LJ4截面,' + str(row) + '行' + str(arr) + '列')

row = 0
arr = 0

# 并排排列（纵排）b
while row * td <= width:
    row = row + 1
while arr * ver <= length:
    arr = arr + 1

row -= 1
arr -= 1
print('并排排列（纵排）可以容纳' + str(row * arr) + '个LJ4截面,' + str(row) + '行' + str(arr) + '列\n')

row = 0
arr = 0

# 并排排列（横排）s
while row * ver <= height:
    row += 1
while arr * td <= length:
    arr += 1

row -= 1
arr -= 1
print('在' + str(length) + '*' + str(height) + '视图中：\n并排排列（横排）可以容纳' + str(row * arr) + '个LJ4截面,' + str(row) + '行' + str(arr) + '列')

row = 0
arr = 0

# 并排排列（纵排）s
while row * td <= height:
    row = row + 1
while arr * ver <= length:
    arr = arr + 1

row -= 1
arr -= 1
print('并排排列（纵排）可以容纳' + str(row * arr) + '个LJ4截面,' + str(row) + '行' + str(arr) + '列\n')

row = 0
arr = 0

# 品排排列（横排）b
while arr1 * td <= length:
    arr1 += 1
while arr2 * td + td / 2 <= length:
    arr2 += 1
while row * ver - (row - 1) * adh <= width:
    row += 1

row -= 1
arr1 -= 1
arr2 -= 1
if arr1 == arr2:
    print('在' + str(length) + '*' + str(width) + '视图中：\n品排排列（横排）可以容纳' + str(row * arr1) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列')
else:
    if row % 2 == 0:
        print('在' + str(length) + '*' + str(width) + '视图中：\n品排排列（横排）可以容纳' + str((row // 2) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2')
    else:
        print('在' + str(length) + '*' + str(width) + '视图中：\n品排排列（横排）可以容纳' + str(((row // 2) + 1) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2')

row = 0
arr1 = 0
arr2 = 0

# 品排排列（纵排）b
while arr1 * ver <= length:
    arr1 += 1
while arr2 * ver + ver / 2 <= length:
    arr2 += 1
while row * td - (row - 1) * adv <= width:
    row += 1

row -= 1
arr1 -= 1
arr2 -= 1
if arr1 == arr2:
    print('品排排列（纵排）可以容纳' + str(row * arr1) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列\n')
else:
    if row % 2 == 0:
        print('品排排列（纵排）可以容纳' + str((row // 2) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2\n')
    else:
        print('品排排列（纵排）可以容纳' + str(((row // 2) + 1) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2\n')

row = 0
arr1 = 0
arr2 = 0

# 品排排列（横排）s
while arr1 * td <= length:
    arr1 += 1
while arr2 * td + td / 2 <= length:
    arr2 += 1
while row * ver - (row - 1) * adh <= height:
    row += 1

row -= 1
arr1 -= 1
arr2 -= 1
if arr1 == arr2:
    print('在' + str(length) + '*' + str(height) + '视图中：\n品排排列（横排）可以容纳' + str(row * arr1) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列')
else:
    if row % 2 == 0:
        print('在' + str(length) + '*' + str(height) + '视图中：\n品排排列（横排）可以容纳' + str((row // 2) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2')
    else:
        print('在' + str(length) + '*' + str(height) + '视图中：\n品排排列（横排）可以容纳' + str(((row // 2) + 1) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2')

row = 0
arr1 = 0
arr2 = 0

# 品排排列（纵排）s
while arr1 * ver <= length:
    arr1 += 1
while arr2 * ver + ver / 2 <= length:
    arr2 += 1
while row * td - (row - 1) * adv <= height:
    row += 1

row -= 1
arr1 -= 1
arr2 -= 1
if arr1 == arr2:
    print('品排排列（纵排）可以容纳' + str(row * arr1) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列\n')
else:
    if row % 2 == 0:
        print('品排排列（纵排）可以容纳' + str((row // 2) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2\n')
    else:
        print('品排排列（纵排）可以容纳' + str(((row // 2) + 1) * arr1 + (row // 2) * arr2) + '个LJ4截面,' + str(row) + '行' + str(arr1) + '列1,' + str(arr2) + '列2\n')

row = 0
arr1 = 0
arr2 = 0
