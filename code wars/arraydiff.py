#https://www.codewars.com/kata/523f5d21c841566fde000009/solutions/python
def array_diff(a, b):
    c=a[:]
    d=[]
    a=list(set(a)-set(b))
    for i in c:
        if i in a:
            d.append(i)
    print(d)

array_diff([1,2,2,3,3],[1])