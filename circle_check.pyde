#Jeffrey Hahner
#PVU249
#11362452
#CMPT 140 (1)
x = 75
y = 75
circle_x = 200
circle_y = 200
diameter = 150

def setup(): 
    size(500, 500)
    fill(0)
    stroke(255)
    textSize(72)

def draw(): 
    background(0)
    global circle_x, circle_y, diameter, x, y
    fill(0)
    ellipse(circle_x, circle_y, diameter, diameter)
    fill(255)
    ellipse(x, y, 5, 5)
    
    if (inside_circle(x, y, circle_x, circle_y, diameter/2)):
        text("Inside!", 10, 60)
    else:
        text("Outside!", 10, 60)

def inside_circle(x, y, circle_x, circle_y, radius):# calculates if distance from point is greater then the radius
    mouse_distance = ((x - circle_x) ** 2 + (y - circle_y) ** 2) ** 0.5
    if mouse_distance <= radius:
        return True # changes text if true
    else:
        return False # changes if not

def mouseClicked():
    global x, y
    x = mouseX
    y = mouseY
