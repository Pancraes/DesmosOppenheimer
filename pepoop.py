"""music wow omg boo"""
def octave(yes: list) -> list:
    fuck = []
    for x in yes:
        fuck.append(x[0] + str(int(x[1])-1))
    return fuck


def calcTime(yes:list)-> float:
    x = 0.0
    for y in yes:
        if isinstance(y, float):
            x += y
        else:
            x += sum(y)
    return x

def noteToNum(m:str)->str:
    num = 0
    if m[0] =="c":
        num = 0
    elif m[0] =="d":
        num += 2
    elif m[0] =="e":
        num += 4
    elif m[0] =="F":
        num += 6
    elif m[0] =="g":
        num += 7
    elif m[0] =="a":
        num += 9
    elif m[0] =="b":
        num += 11
    num += int(m[1])*12
    return str(num)


def num(note: list, dur: list) -> str:
    part=""
    end = round(dur[0] + dur[1][0], 4)
    part += str(dur[0]) + "<x<" + str(end) + ":" + noteToNum(note[0]) + ", "
    end += round(dur[1][1], 4)
    for x in range(2, len(dur)):
        end1 = round(end + dur[x][0], 4)
        part += str(end) + "<x<" + str(end1) + ":" + noteToNum(note[x-1]) + ", "
        end = round(end1 + dur[x][1], 4)
    return part


if __name__ == "__main__":
    durs = [18.8, [60/180*3*4, 60/180*3*2], [60/240*3*8, 60/70*8 + 60/93*8], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/80/6/5*3, 60/80/6/5*2 + 0.25], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/108/6/5*3, 60/108/6/5*2+0.1851851851851852], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/90/3/5*3, 60/90/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/120/3/5*3, 60/120/3/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/93/4/5*3, 60/93/4/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/130/3/5*3, 60/130/3/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/112/4/5*3, 60/112/4/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/144/3/5*3, 60/144/3/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/120/4/5*3, 60/120/4/5*2], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/80/6, 60/80/6], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/130/4, 60/130/4], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/85/6, 60/85/6], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/140/4, 60/140/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4], [60/150/4, 60/150/4]]
    notes =  ['c2', 'c2', 'a2', 'a2', 'a2', 'a2', 'a2', 'a2', 'a2', 'a2', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'd3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'c3', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'F2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2', 'g2']
    print(num(notes, durs))
