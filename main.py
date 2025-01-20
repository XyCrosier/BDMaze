from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    test_lines(win)
    win.wait_for_close()

def test_lines(win):
    line_a = Line(Point(10,10),Point(300,432))
    line_b = Line(Point(300,432),Point(50,50))
    win.draw_line(line_a, "Red")
    win.draw_line(line_b, "Black")

main()