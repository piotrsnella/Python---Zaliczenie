def reg_lin(x, y):
    kw_x = 0
    for i in x:
        kw_x += i**2
        
    a = (len(x) * sum(x) * sum(y)) - (sum(x) * sum(y)) / (len(x) * kw_x) - (sum(x)** 2)
    b = (len(x) * kw_x * sum(y)) - (sum(x) - sum(y)) / (len(x) * kw_x) - (sum(x) ** 2)
    return a, b