import math

def binomial(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def bernstein(x, n, i):
    return binomial(n, i)*x**i*(1-x)**(n-i)

def bezierpoint(cords, t):
    n = len(cords)
    x = 0
    y = 0
    for i in range(n):
        z = bernstein(t, n-1, i)
        x = x + cords[i][0] * z
        y = y + cords[i][1] * z
    return x, y

def setup():
    size(700, 700);
    background(255)
    
def draw_bez(cords):
    stroke(69,93,255)
    N = 1000
    dt = 1.0/float(N-1)
    lastx, lasty = bezierpoint(cords, 0.0)
    for i in range(N):
        x, y = bezierpoint(cords, dt*i)
        line(lastx, lasty, x, y)
        lastx = x
        lasty = y

def draw_contr_poly(cords):
    stroke(0, 0, 0)
    fill(0,0,0)
    rect(cords[0][0] - 5, cords[0][1] - 5, 10, 10)
    annotate(cords[0])
    for i in range(len(cords) - 1):
        rect(cords[i+1][0] - 5, cords[i+1][1] - 5, 10, 10)
        line(cords[i][0], cords[i][1], cords[i+1][0], cords[i+1][1])
        annotate(cords[i+1])

def approx(cord, t):
    return cord[0][0] + (cord[1][0]-cord[0][0])*t, cord[0][1] + (cord[1][1]-cord[0][1])*t

def draw_line(cords, t):
    for i in range(len(cords) - 1):
        ellipse(cords[i][0], cords[i][1], 5, 5)
        ellipse(cords[i+1][0], cords[i+1][1], 5, 5)
        line(cords[i][0], cords[i][1], cords[i+1][0], cords[i+1][1])
    if len(cords) ==2 :
        x, y = approx(cords[0:2][:], t)
        ellipse(x, y, 10, 10)
        annotatet([x,y], t)

def draw_in_line(cords, i, t):
    if (i < 1):
        return
    fill(49,160,141)
    stroke(49,160,141)
    new_cords = []
    for i in range(len(cords)-1):
        new_cords.append(approx(cords[i:i+2][:], t))
    draw_line(new_cords, t)
    draw_in_line(new_cords, i-1, t)
    
def annotate(cord):
    x = (cord[0]-250)*0.1
    y = (cord[1]-250)*0.1
    text("(" + str(cord[0]) + ", " + str(cord[1])+")", cord[0]+x, cord[1]+y)
    
def annotatet(cord, t):
    pos = {0.25:-220,0.5:-160, 0.75:+10}
    text("(" + str(cord[0]) + ", " + str(cord[1]) + ", " + str(t) + ")", cord[0]+pos[t], cord[1])
         
def draw():
    cords = [[200, 600], [600, 600], [400, 300], [110,130], [500, 130]]
    draw_bez(cords)
    draw_contr_poly(cords)
    draw_in_line(cords, 3, 0.25)
    draw_in_line(cords, 3, 0.5)
    draw_in_line(cords, 3, 0.75)
    fill(0,0,0);
    text("Kontrollpolygon und Kontrollpunkte", 20, 20)
    fill(49,160,141)
    text("Hilfslinien und Hilfspunkte", 20, 40)
    fill(69,93, 255)
    text("Bezierkurve", 20, 60)
    save("outfile.jpg")
    noLoop()
        
