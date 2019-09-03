

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


def main():
    n = 4
    m = 2
    for sub in n_choose_m_iterator(n, m):
        print(sub)


if __name__ == '__main__':
    main()
