import time
from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
    _fields_= [('x', c_long), ('y', c_long)]

def query_mouse_position():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {
        'x': pt.x,
        'y': pt.y
    }

for i in range(100):
    pos = query_mouse_position()
    print(pos)
    time.sleep(0.1)
