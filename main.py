import time
from winapi.cursor import get_cursor_pos, set_cursor_pos

delay = 0.01
points = []
for i in range(200):
    points.append(get_cursor_pos())
    time.sleep(delay)

for i in points:
    set_cursor_pos(i[0], i[1])
    time.sleep(delay)
