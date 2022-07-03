from collections import deque

class Const:
    red = (255,0,0)
    white = (255,255,255)
    black = (0,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    
    light_color = (255,249,239)
    edge_color = (96,68,35)

    all_vectors = [(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,-1),(-1,0),(-1,1)]

    def equal(color1, color2, sensitivity = 20):
        for i in range(3):
            if abs(color1[i] - color2[i]) > sensitivity:
                return False
        return True

    def find_max(arr):
        min_x, min_y = arr[0]
        max_x, max_y = arr[0]
        for i, j in arr:
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j
        return min_x, max_x, min_y, max_y

    def push_dot(x, y, pix, color, space = 0):
        for i in range(x-space,x+space+1):
            for j in range(y-space,y+space+1):
                pix[i,j] = color


class Color:
    def color_all(pix, im_size):
        color = [50,0,0]
        andis_color = 0
        ans_arr = []
        for i in range(im_size[0]):
            for j in range(300, im_size[1] - 300):
                if pix[i, j] == Const.light_color:
                    ans_arr.append(Color.dfs_color(i, j, pix, tuple(color)))
                    color[andis_color] += 80

                    # set andis_color
                    for i in color:
                        if i > 200: 
                            color = [50,0,0]
                    if andis_color == 2: andis_color = 0
                    else: andis_color += 1
        return ans_arr

    def dfs_color(x, y, pix, color):
        arr_all_point = []
        pix[x, y] = color
        queue = deque()
        queue.append((x,y))
        arr_all_point.append((x,y))
        while len(queue) > 0:
            (x, y) = queue.popleft()
            for i, j in Const.all_vectors:
                if Const.equal(pix[x+i, y+j], Const.light_color):
                    queue.append((x+i, y+j))
                    pix[x+i, y+j] = color
                    arr_all_point.append((x+i,y+j))        
        # colorize_block_to_point
        if len(arr_all_point) > 64:
            min_x, max_x, min_y, max_y = Const.find_max(arr_all_point)
            x = (max_x + min_x) // 2
            y = (max_y + min_y) // 2
            Const.push_dot(x, y, pix, Const.green, space = 5)
            return x, y

    
