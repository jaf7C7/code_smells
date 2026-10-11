def proc(d, n):
    r = []
    for i in range(len(d) - n + 1):
        w = d[i:i + n]
        r.append(sum(w) / n)
    return r


def chk(d, t):
    return [i for i, x in enumerate(d) if x > t]


def go(d, n, t):
    a = proc(d, n)
    return {"avg": a, "hi": chk(a, t)}
