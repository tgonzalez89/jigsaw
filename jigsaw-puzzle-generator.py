import math

seed = 1

def random():
    global seed
    x = math.sin(seed) * 10000
    seed += 1
    return x - math.floor(x)

def uniform(min, max):
    r = random()
    return min + r * (max - min)

def rbool():
    global seed
    return random() > 0.5

a = 0
b = 0
c = 0
d = 0
e = 0
t = 0
j = 0
flip = 0
xi = 0
yi = 0
xn = 0
yn = 0
vertical = 0
offset_x = 0
offset_y = 0
width = 0
height = 0

def first():
    global e, j
    e = uniform(-j, j)
    next()

def next():
    global a, b, c, d, e, j, flip
    flipold = flip
    flip = rbool()
    a = -e if flip == flipold else e
    b = uniform(-j, j)
    c = uniform(-j, j)
    d = uniform(-j, j)
    e = uniform(-j, j)

def sl():
    global xn , yn, height, width, vertical
    return height / yn if vertical else width / xn

def sw():
    global xn , yn, height, width, vertical
    return width / xn if vertical else height / yn

def ol():
    global xi , yi, offset_x, offset_y, vertical
    return (offset_y if vertical else offset_x) + sl() * (yi if vertical else xi)

def ow():
    global xi , yi, offset_x, offset_y, vertical
    return (offset_x if vertical else offset_y) + sw() * (xi if vertical else yi)

def l(v):
    ret = ol() + sl() * v
    return round(ret * 100) / 100

def w(v):
    global flip
    ret = ow() + sw() * v * (-1.0 if flip else 1.0)
    return round(ret * 100) / 100

def p0l():
    return str(l(0.0))

def p0w():
    return str(w(0.0))

def p1l():
    return str(l(0.2))

def p1w():
    global a
    return str(w(a))

def p2l():
    global b, d
    return str(l(0.5 + b + d))

def p2w():
    global c, t
    return str(w(-t + c))

def p3l():
    global b, t
    return str(l(0.5 - t + b))

def p3w():
    global c, t
    return str(w(t + c))

def p4l():
    global b, d, t
    return str(l(0.5 - 2.0 * t + b - d))

def p4w():
    global c, t
    return str(w(3.0 * t + c))

def p5l():
    global b, d, t
    return str(l(0.5 + 2.0 * t + b - d))

def p5w():
    global c, t
    return str(w(3.0 * t + c))

def p6l():
    global b, t
    return str(l(0.5 + t + b))

def p6w():
    global c, t
    return str(w(t + c))

def p7l():
    global b, d
    return str(l(0.5 + b + d))

def p7w():
    global c, t
    return str(w(-t + c))

def p8l():
    return str(l(0.8))

def p8w():
    global e
    return str(w(e))

def p9l():
    return str(l(1.0))

def p9w():
    return str(w(0.0))

strings = list()

def gen_d(_seed, _tabsize, _jitter, _xn, _yn):
    global seed, vertical, xi, yi, xn, yn, offset_x, offset_y, width, height, t, j, strings

    seed = _seed
    t = _tabsize / 250.0
    j = _jitter / 100.0
    xn = _xn
    yn = _yn

    string = ""
    for _yi in range(yn):
        strings.append(list())
        for _xi in range(xn):
            strings[_yi].append("")

    vertical = 0
    yi = 1
    for _ in range(yi, yn):
        xi = 0
        first()
        string += "M" + p0l() + "," + p0w() + " "
        for _ in range(xi, xn):
            string += "C" + p1l() + "," + p1w() + " " + p2l() + "," + p2w() + " " + p3l() + "," + p3w() + " "
            string += "C" + p4l() + "," + p4w() + " " + p5l() + "," + p5w() + " " + p6l() + "," + p6w() + " "
            string += "C" + p7l() + "," + p7w() + " " + p8l() + "," + p8w() + " " + p9l() + "," + p9w() + " "

            offset_x = (width / xn / 2) - (width * xi / xn)
            offset_y = (height / yn / 2) - (width * yi / yn)

            strings[yi][xi] += "M" + p0l() + "," + p0w() + " "
            strings[yi][xi] += "C" + p1l() + "," + p1w() + " " + p2l() + "," + p2w() + " " + p3l() + "," + p3w() + " "
            strings[yi][xi] += "C" + p4l() + "," + p4w() + " " + p5l() + "," + p5w() + " " + p6l() + "," + p6w() + " "
            strings[yi][xi] += "C" + p7l() + "," + p7w() + " " + p8l() + "," + p8w() + " " + p9l() + "," + p9w() + " "

            offset_y = (height / yn / 2) - (width * (yi-1) / yn)

            strings[yi-1][xi] += "M" + p0l() + "," + p0w() + " "
            strings[yi-1][xi] += "C" + p1l() + "," + p1w() + " " + p2l() + "," + p2w() + " " + p3l() + "," + p3w() + " "
            strings[yi-1][xi] += "C" + p4l() + "," + p4w() + " " + p5l() + "," + p5w() + " " + p6l() + "," + p6w() + " "
            strings[yi-1][xi] += "C" + p7l() + "," + p7w() + " " + p8l() + "," + p8w() + " " + p9l() + "," + p9w() + " "

            if yi-1 == 0:
                p1 = width * xi / xn
                p2 = width * (xi + 1) / xn
                strings[yi-1][xi] += "M" + str(offset_x + p1) + "," + str(offset_y) + " "
                strings[yi-1][xi] += "L" + str(offset_x + p2) + "," + str(offset_y) + " "

            offset_y = (height / yn / 2) - (width * yi / yn)

            if yi == yn-1:
                p1 = width * xi / xn
                p2 = width * (xi + 1) / xn
                py = height
                strings[yi][xi] += "M" + str(offset_x + p1) + "," + str(offset_y + py) + " "
                strings[yi][xi] += "L" + str(offset_x + p2) + "," + str(offset_y + py) + " "

            offset_x = 0
            offset_y = 0

            next()
            xi += 1
        yi += 1

    vertical = 1
    xi = 1
    for _ in range(xi, xn):
        yi = 0
        first()
        string += "M" + p0w() + "," + p0l() + " "
        for _ in range(yi, yn):
            string += "C" + p1w() + "," + p1l() + " " + p2w() + "," + p2l() + " " + p3w() + "," + p3l() + " "
            string += "C" + p4w() + "," + p4l() + " " + p5w() + "," + p5l() + " " + p6w() + "," + p6l() + " "
            string += "C" + p7w() + "," + p7l() + " " + p8w() + "," + p8l() + " " + p9w() + "," + p9l() + " "

            offset_x = (width / xn / 2) - (width * xi / xn)
            offset_y = (height / yn / 2) - (width * yi / yn)

            strings[yi][xi] += "M" + p0w() + "," + p0l() + " "
            strings[yi][xi] += "C" + p1w() + "," + p1l() + " " + p2w() + "," + p2l() + " " + p3w() + "," + p3l() + " "
            strings[yi][xi] += "C" + p4w() + "," + p4l() + " " + p5w() + "," + p5l() + " " + p6w() + "," + p6l() + " "
            strings[yi][xi] += "C" + p7w() + "," + p7l() + " " + p8w() + "," + p8l() + " " + p9w() + "," + p9l() + " "

            offset_x = (width / xn / 2) - (width * (xi-1) / xn)

            strings[yi][xi-1] += "M" + p0w() + "," + p0l() + " "
            strings[yi][xi-1] += "C" + p1w() + "," + p1l() + " " + p2w() + "," + p2l() + " " + p3w() + "," + p3l() + " "
            strings[yi][xi-1] += "C" + p4w() + "," + p4l() + " " + p5w() + "," + p5l() + " " + p6w() + "," + p6l() + " "
            strings[yi][xi-1] += "C" + p7w() + "," + p7l() + " " + p8w() + "," + p8l() + " " + p9w() + "," + p9l() + " "

            if xi-1 == 0:
                p1 = height * yi / yn
                p2 = height * (yi + 1) / yn
                strings[yi][xi-1] += "M" + str(offset_x) + "," + str(offset_y + p1) + " "
                strings[yi][xi-1] += "L" + str(offset_x) + "," + str(offset_y + p2) + " "

            offset_x = (width / xn / 2) - (width * xi / xn)

            if xi == xn-1:
                p1 = height * yi / yn
                p2 = height * (yi + 1) / yn
                px = width
                strings[yi][xi] += "M" + str(offset_x + px) + "," + str(offset_y + p1) + " "
                strings[yi][xi] += "L" + str(offset_x + px) + "," + str(offset_y + p2) + " "

            offset_x = 0
            offset_y = 0

            next()
            yi += 1
        xi += 1

    string += "M" + str(offset_x) + "," + str(offset_y) + " "
    string += "L" + str(offset_x + width) + "," + str(offset_y) + " "
    string += "L" + str(offset_x + width) + "," + str(offset_y + height) + " "
    string += "L" + str(offset_x) + "," + str(offset_y + height) + " "
    string += "L" + str(offset_x) + "," + str(offset_y) + " "

    return string

def generate(_seed, _tabsize, _jitter, _xn, _yn, _width, _height):
    global width, height, offset_x, offset_y

    width = _width
    height = _height
    offset_x = 0.0
    offset_y = 0.0

    data = "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.0\" "
    data += "width=\"" + str(width) + "mm\" height=\"" + str(height) + "mm\" viewBox=\"0 0 " + str(width) + " " + str(height) + "\">"
    data += "<path fill=\"none\" stroke=\"black\" stroke-width=\"1.0\" d=\""
    data += gen_d(_seed, _tabsize, _jitter, _xn, _yn)
    data += "\"></path></svg>"

    with open("jigsaw.svg", 'w') as f:
        f.write(data)

def generate2():
    for _yi in range(yn):
        for _xi in range(xn):
            data = "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.0\" "
            data += "width=\"" + str(2 * width / xn) + "mm\" height=\"" + str(2 * height / yn) + "mm\" viewBox=\"0 0 " + str(2 * width / xn) + " " + str(2 * height / yn) + "\">"
            data += "<path fill=\"none\" stroke=\"black\" stroke-width=\"1.0\" d=\""
            data += strings[_yi][_xi]
            data += "\"></path></svg>"

            with open(f"jigsaw-{_xi}-{_yi}.svg", 'w') as f:
                f.write(data)

if __name__ == "__main__":
    import sys
    argv1 = int(sys.argv[1])
    argv2 = int(sys.argv[2])
    argv3 = float(sys.argv[3])
    argv4 = float(sys.argv[4])
    argv5 = int(sys.argv[5])

    print(argv4 * 7 / 15)
    generate(
        _seed=argv5,
        _tabsize=argv3,  # min 15, max 30
        _jitter=argv4 * 7 / 15,  # min 1, max 15
        _xn=argv1,
        _yn=argv2,
        _width=argv1 * 50,
        _height=argv2 * 50,
    )
    generate2()

