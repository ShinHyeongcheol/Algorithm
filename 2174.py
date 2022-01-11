def check_dir(dir):
    if dir == 'N':
        return 0
    elif dir == 'E':
        return 1
    elif dir == 'S':
        return 2
    elif dir == 'W':
        return 3
    return False
    # 0,1,2,3 = S,W,N,E -> 상하반전

def run(r_run):
    #번호, 명령, 반복
    way_x = [0,1,0,-1]
    way_y = [1,0,-1,0]
    dir = robot[r_run[0]][2]
    if r_run[1] == 'L':
        robot[r_run[0]][2] =  (dir - r_run[2]) % 4
        return 0, r_run[0]
    elif r_run[1] == 'R':
        robot[r_run[0]][2] =  (dir + r_run[2]) % 4
        return 0, r_run[0]
    elif r_run[1] == 'F':
        new_x = robot[r_run[0]][0]
        new_y = robot[r_run[0]][1]
        for i in range(r_run[2]):
            matrix[new_y][new_x] = 0
            new_x += way_x[dir]
            new_y += way_y[dir]
            robot[r_run[0]][0] = new_x
            robot[r_run[0]][1] = new_y
            if  matrix[new_y][new_x] != 0:
                return  matrix[new_y][new_x], r_run[0]
            matrix[new_y][new_x] = r_run[0]
    return 0, r_run[0]
   
A, B = tuple(map(int,input().split()))
N, M = tuple(map(int,input().split()))

matrix = [[0 for i in range(A+2)] for j in range(B+2)]
robot = [0]
for i in range(A+2):
    matrix[0][i] = -1
    matrix[-1][i] = -1
    
for i in range(B+2):
    matrix[i][0] = -1
    matrix[i][-1] = -1

for i in range(N):
    robot_data = input().split()
    robot_data[0] = int(robot_data[0])
    robot_data[1] = int(robot_data[1])
    robot_data[2] = check_dir(robot_data[2])
    matrix[robot_data[1]][robot_data[0]] = i + 1 #robot_num
    robot.append(robot_data) # x, y, dir
    #for i in range(B + 2):
       #print(matrix[i])

    
check_end = 0       
for i in range(M):
    robot_run = input().split()
    robot_run[0] = int(robot_run[0])
    robot_run[2] = int(robot_run[2])
    if check_end != 0:
        continue
    check_end, robot_num = run(robot_run)
    #for i in range(B + 2):
        #print(matrix[i])

if check_end == -1:
    print("Robot",robot_num,"crashes into the wall")
elif check_end != 0:
    print("Robot",robot_num,"crashes into robot",check_end)
else:
    print("OK")
# L과 R방향 수정필요??
