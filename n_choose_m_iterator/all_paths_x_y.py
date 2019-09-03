

def n_choose_m_iterator(N, M, startpoint=None):
    if startpoint is None:
        subscripts = list(range(M))
    else:
        subscripts = copy.deepcopy(startpoint)
    while True:
        yield subscripts
        off = M - 1
        while off > -1:
            rev_off = M - off
            if subscripts[off] < N - rev_off and off >= 0:
                break
            off -= 1
        if off < 0:
            break
        subscripts[off] += 1
        off += 1
        while off < M:
            subscripts[off] = subscripts[off - 1] + 1
            off += 1

def subs2directions(sub, n):
    dirs = ["right" for _ in range(n)]
    for s in sub:
        dirs[s] = "up"
    return dirs

def directions2coord(dirs):
    i = 0
    j = 0
    points = [(i, j)]
    for d in dirs:
        if d == "right":
            i += 1
        else:
            j += 1
        points.append((i, j))
    return points


def all_paths_x_y(x, y):
    n = x + y
    for sub in n_choose_m_iterator(x+y, y):
        '''0 right, 1 up'''
        dirs = subs2directions(sub, n)
        print("directions = ", dirs)
        points = directions2coord(dirs)
        print("points = ", points)

def main():
    x = 2
    y = 2
    all_paths_x_y(x, y)

if __name__ == '__main__':
    main()
