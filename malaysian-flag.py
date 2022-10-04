import turtle as trtl
trtl.speed(speed=2)

# color(r, g, b)
merah = (255, 0, 0)
biru = (0, 0, 255)
kuning = (255, 255, 0)
putih = (255, 255, 255)
hitam = (0, 0, 0)

trtl.penup()
trtl.left(90)
trtl.forward(50)
trtl.right(90)
trtl.right(180)
trtl.forward(150)
trtl.right(180)
trtl.pendown()

trtl.left(90)
trtl.forward(4)
trtl.right(90)
trtl.forward(284)
trtl.right(90)
trtl.forward(144)
trtl.right(90)
trtl.forward(284)
trtl.right(90)
trtl.forward(140)
trtl.right(90)

def stripes(color):
    trtl.color(color)
    trtl.begin_fill()
    trtl.forward(280)
    trtl.right(90)
    trtl.forward(10)
    trtl.right(90)
    trtl.forward(280)
    trtl.end_fill()
    trtl.right(180)

# Red and white stripes

for i in range(0, 7):
    stripes(merah)
    stripes(putih)

# Reset position to top left

trtl.left(90)
trtl.forward(140)
trtl.right(90)

# Blue rectangle

trtl.color(biru)
trtl.begin_fill()
trtl.forward(140)
trtl.right(90)
trtl.forward(80)
trtl.right(90)
trtl.forward(140)
trtl.end_fill()

# Reset position to top left corner

trtl.right(90)
trtl.forward(80)
trtl.right(90)

# Move to center of circle

trtl.forward(65)
trtl.right(90)
trtl.forward(40)
trtl.right(180)
trtl.color(kuning)
trtl.begin_fill()
trtl.circle(25)
trtl.end_fill()
trtl.right(90)
trtl.forward(5)
trtl.left(90)
trtl.color(biru)
trtl.begin_fill()
trtl.circle(22)
trtl.end_fill()
trtl.color(merah)

# trtl.forward(87.5)
# trtl.right(90)
# trtl.forward(40)
# trtl.right(180)

# # Yellow star lines

trtl.right(90)
trtl.forward(20)
trtl.right(90)
trtl.forward(5)
trtl.left(90)
trtl.left(90)
trtl.color(kuning)



trtl.begin_fill()
for i in range(14):
    trtl.right(77)
    trtl.forward(18)
    trtl.left(154)
    trtl.forward(18)
trtl.end_fill()

trtl.color(kuning)
trtl.begin_fill()
trtl.forward(5)
trtl.right(90)
trtl.forward(4)
trtl.left(90)
trtl.circle(11)
trtl.end_fill()

# exec("""\nimport turtle as trtl\ntrtl.speed(speed=2)\n\n# color(r, g, b)\nmerah = (255, 0, 0)\nbiru = (0, 0, 255)\nkuning = (255, 255, 0)\nputih = (255, 255, 255)\nhitam = (0, 0, 0)\n\ntrtl.penup()\ntrtl.left(90)\ntrtl.forward(50)\ntrtl.right(90)\ntrtl.right(180)\ntrtl.forward(150)\ntrtl.right(180)\ntrtl.pendown()\n\ntrtl.left(90)\ntrtl.forward(4)\ntrtl.right(90)\ntrtl.forward(284)\ntrtl.right(90)\ntrtl.forward(144)\ntrtl.right(90)\ntrtl.forward(284)\ntrtl.right(90)\ntrtl.forward(140)\ntrtl.right(90)\n\ndef stripes(color):\n    trtl.color(color)\n    trtl.begin_fill()\n    trtl.forward(280)\n    trtl.right(90)\n    trtl.forward(10)\n    trtl.right(90)\n    trtl.forward(280)\n    trtl.end_fill()\n    trtl.right(180)\n\n# Red and white stripes\n\nfor i in range(0, 7):\n    stripes(merah)\n    stripes(putih)\n\n# Reset position to top left\n\ntrtl.left(90)\ntrtl.forward(140)\ntrtl.right(90)\n\n# Blue rectangle\n\ntrtl.color(biru)\ntrtl.begin_fill()\ntrtl.forward(140)\ntrtl.right(90)\ntrtl.forward(80)\ntrtl.right(90)\ntrtl.forward(140)\ntrtl.end_fill()\n\n# Reset position to top left corner\n\ntrtl.right(90)\ntrtl.forward(80)\ntrtl.right(90)\n\n# Move to center of circle\n\ntrtl.forward(65)\ntrtl.right(90)\ntrtl.forward(40)\ntrtl.right(180)\ntrtl.color(kuning)\ntrtl.begin_fill()\ntrtl.circle(25)\ntrtl.end_fill()\ntrtl.right(90)\ntrtl.forward(5)\ntrtl.left(90)\ntrtl.color(biru)\ntrtl.begin_fill()\ntrtl.circle(22)\ntrtl.end_fill()\ntrtl.color(merah)\n\n# trtl.forward(87.5)\n# trtl.right(90)\n# trtl.forward(40)\n# trtl.right(180)\n\n# # Yellow star lines\n\ntrtl.right(90)\ntrtl.forward(20)\ntrtl.right(90)\ntrtl.forward(5)\ntrtl.left(90)\ntrtl.left(90)\ntrtl.color(kuning)\n\n\n\ntrtl.begin_fill()\nfor i in range(14):\n    trtl.right(77)\n    trtl.forward(18)\n    trtl.left(154)\n    trtl.forward(18)\ntrtl.end_fill()\n\ntrtl.color(kuning)\ntrtl.begin_fill()\ntrtl.forward(5)\ntrtl.right(90)\ntrtl.forward(4)\ntrtl.left(90)\ntrtl.circle(11)\ntrtl.end_fill()\n""")

