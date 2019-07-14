

id = {"idaap nso"}
pattern = "diapason "
s = set(id)
print(s)
curStr = ['i', 'd', 'a', 'a', 'p', ' ', 'n', 's', 'o']
q = []
q.append(curStr)
print(q)
nextStr = []
flag = 1
z = ""
x = 0
# D I A
# P A S
# O N ''

# D I A
# P ''A
# S O N
count = 0
while flag > 0:
    count = count + 1
    #finding space
    temp = 0
    while temp < 8:
        if q[0][temp] == ' ':
            break
        temp = temp + 1

    #right
    if temp != 2 and temp != 5 and temp != 8:
        q[0][temp] = q[0][temp+1]
        q[0][temp+1] = ' '
        g = ""
        for i in range(9):
            g = g + q[0][i]

        if g not in id:
            id.add(g)

            nextStr = []
            for x in q[0]:
                nextStr.append(x)
            nextStr.append('r')
            k = 0
            for i in range(9):
                if g[i] == pattern[i]:
                    k = k + 1
                if k == 9:
                    print(100)
                    print(nextStr)
                    flag = 0
                    ans = len(nextStr) - 9
                    print(ans)
            q.append(nextStr)

            del nextStr

        q[0][temp+1] = q[0][temp]
        q[0][temp] = ' '

      #left
    if temp != 3 and temp != 6 and temp != 0:
        q[0][temp] = q[0][temp - 1]
        q[0][temp-1] = ' '
        g = ""
        for i in range(9):
            g = g + q[0][i]

        if g not in id:
            id.add(g)

            nextStr = []
            for x in q[0]:
                nextStr.append(x)
            nextStr.append('l')
            k = 0
            for i in range(9):

                if g[i] == pattern[i]:
                    k = k + 1
                if k == 9:
                    print(100)
                    print(nextStr)
                    flag = 0
                    ans = len(nextStr) - 9
                    print(ans)
            q.append(nextStr)

            del nextStr

        q[0][temp - 1] = q[0][temp]
        q[0][temp] = ' '

    #up
    if temp > 2:
        q[0][temp] = q[0][temp - 3]
        q[0][temp - 3] = ' '
        g = ""
        for i in range(9):
            g = g + q[0][i]
        if g not in id:
            id.add(g)

            nextStr = []
            for x in q[0]:
                nextStr.append(x)
            nextStr.append('u')
            k = 0
            for i in range(9):
                if g[i] == pattern[i]:
                    k = k + 1
                if k == 9:
                    print(100)
                    print(nextStr)
                    flag = 0
                    ans = len(nextStr) - 9
                    print(ans)
            q.append(nextStr)

            del nextStr

        q[0][temp - 3] = q[0][temp]
        q[0][temp] = ' '
    #down
    if temp < 6:
        q[0][temp] = q[0][temp + 3]
        q[0][temp + 3] = ' '
        g = ""
        for i in range(9):
            g = g + q[0][i]

        if g not in id:
            id.add(g)
            nextStr = []
            for x in q[0]:
                nextStr.append(x)
            nextStr.append('d')
            k = 0
            for i in range(9):
                if g[i] == pattern[i]:
                    k = k +1
                if k == 9:
                    print(100)
                    print(nextStr)
                    flag = 0
                    ans = len(nextStr) - 9
                    print(ans)
            q.append(nextStr)

            del nextStr

        q[0][temp + 3] = q[0][temp]
        q[0][temp] = ' '
    q.pop(0)

























