from ctypes import windll, Structure, c_long, byref

class c_point(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]

def get_cursor_pos():
    pt = c_point()
    windll.user32.GetCursorPos(byref(pt))
    return (pt.x, pt.y)

def set_cursor_pos(x: int, y: int):
    windll.user32.SetCursorPos(x, y)
