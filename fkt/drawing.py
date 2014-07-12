

class Region(object):
    def draw(self):
        """
        Turns a custom region into a set drawing instructions.
        """

class TextRegion(Region):
    def __init__(self, *lines):
        self.lines = lines

    def draw(self):
        maxx, maxy = self.parent.get_max_chars()
        for x, line in enumerate(self.lines):
            self.parent.text_draw(0, x * maxy, line)

    def add_text(self, line, text):
        pass
