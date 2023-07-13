a=[1, 2, 3, 4, 5, 6, 7]
b=0
c=0
# for i in a:
#     if c == len(a)-1:
#         break
#     b=b+i
#     c=c+1

# print(b)

#Solución óptima
for i in a[:-1]:
    c=c+i

print(c)