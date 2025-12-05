import turtle

def draw_button(t, x, y, width, height, text, color):
#draws button
    t.penup()
    t.goto(x - width / 2, y - height / 2)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x, y - height / 4)
    t.write(text, align="center", font=("Arial", 16, "normal"))

def handle_click(x, y):
#user input
    global display_text, current_input, operation, first_operand

    for button in buttons:
        bx, by, bw, bh, text, _ = button
        if bx - bw / 2 < x < bx + bw / 2 and by - bh / 2 < y < by + bh / 2:
            if text.isdigit() or text == ".":
                current_input += text
                display_text.clear()
                display_text.write(current_input, align="left", font=("Arial", 24, "normal"))
            elif text in ["+", "-", "*", "/"]:
                if first_operand is None:
                    first_operand = float(current_input) if "." in current_input else int(current_input)
                else:
                    calculate()
                    first_operand = float(current_input) if "." in current_input else int(current_input)
                operation = text
                current_input = ""
                display_text.clear()
            elif text == "=":
                calculate()
                first_operand = None
                operation = None
            elif text == "C":
                current_input = ""
                display_text.clear()
                first_operand = None
                operation = None

#jimster
def calculate():
    #main function
    global current_input, first_operand, operation
    if first_operand is not None and current_input:
        second_operand = float(current_input) if "." in current_input else int(current_input)
        try:
            if operation == "+":
                result = first_operand + second_operand
            elif operation == "-":
                result = first_operand - second_operand
            elif operation == "*":
                result = first_operand * second_operand
            elif operation == "/":
                if second_operand == 0:
                    result = "Error"
                else:
                    result = first_operand / second_operand
            else:
                return
            current_input = str(result)
            display_text.clear()
            display_text.write(current_input, align="left", font=("Arial", 24, "normal"))
        except:
          current_input = "Error"
          display_text.clear()
          display_text.write(current_input, align="left", font=("Arial", 24, "normal"))
          first_operand = None
          operation = None
    else:
        if current_input == "" and first_operand is None and operation is None:
            return
        current_input = "Error"
        display_text.clear()
        display_text.write(current_input, align="left", font=("Arial", 24, "normal"))
        first_operand = None
        operation = None

screen = turtle.Screen()
screen.setup(width=300, height=400)
screen.title("Basic Calculator")
screen.tracer(0)  # Turn off animation

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

display_text = turtle.Turtle()
display_text.hideturtle()
display_text.penup()
display_text.goto(-120, 150)

# variables
current_input = ""
first_operand = None
operation = None

# button layout
buttons = [
    (-100, 100, 50, 50, "7", "lightgray"),
    (-50, 100, 50, 50, "8", "lightgray"),
    (0, 100, 50, 50, "9", "lightgray"),
    (50, 100, 50, 50, "/", "lightblue"),
    (-100, 50, 50, 50, "4", "lightgray"),
    (-50, 50, 50, 50, "5", "lightgray"),
    (0, 50, 50, 50, "6", "lightgray"),
    (50, 50, 50, 50, "*", "lightblue"),
    (-100, 0, 50, 50, "1", "lightgray"),
    (-50, 0, 50, 50, "2", "lightgray"),
    (0, 0, 50, 50, "3", "lightgray"),
    (50, 0, 50, 50, "-", "lightblue"),
    (-100, -50, 100, 50, "0", "lightgray"),
    (0, -50, 50, 50, ".", "lightgray"),
    (50, -50, 50, 50, "+", "lightblue"),
    (-100, -100, 200, 50, "=", "lightgreen"),
    (50,-100, 50, 50, "C", "lightcoral")
]

for button in buttons:
    draw_button(pen, *button)

#click handler
screen.onclick(handle_click)

screen.update()
turtle.done()