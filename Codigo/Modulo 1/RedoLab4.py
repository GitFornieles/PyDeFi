def promedio_variable(*args):
    c=0
    for n in args:
        c=c+n
    return c/len(args)

print(promedio_variable(12,3,4))