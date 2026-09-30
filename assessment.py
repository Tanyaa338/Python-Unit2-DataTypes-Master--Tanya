def spaces(N, y, t):
    y = ("C", "C", ".", ".", "C")
    t = (".", "C", "C", ".", ".")
    for i in range(N):
        y[i] and t[i]
    if y[i] == "c" and t[i] == "c":
        print("+1")
    else: 
        print("+0")
