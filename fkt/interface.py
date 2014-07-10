
class DrawInterface(object):
    def __init__(self, parent):
        self.parent = parent
        self.ops = []

    def compile_operations(self):
        pass

    def char_draw(self, x, y, char, style={}): pass
    def char_clear(self, x, y): pass
    def clear(self): pass
    def pixel_draw(self, x, y, style={}): pass
    def pixel_clear(self, x, y, style): pass
    def flip(self): pass
