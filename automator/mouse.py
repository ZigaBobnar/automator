from pynput import mouse

class Mouse:
    def listen(self):
        def on_move(x: int, y: int):
            print('Mouse moved: {0}'.format((x, y)))

        def on_click(x: int, y: int, button, pressed):
            print('{0} at {1}'.format(
                'Pressed' if pressed else 'Released',
                (x, y)
            ))
            if not pressed:
                return False  # To stop the listener

        def on_scroll(x: int, y: int, dx: int, dy: int):
            print('Scrolled {0} at {1}'.format(
                'down' if dy < 0 else 'up',
                (x, y)
            ))

        with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll
        ) as listener:
            listener.join()
