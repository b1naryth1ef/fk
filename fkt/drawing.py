

class Region(object):
    def draw(self):
        """
        Turns a custom region into a set drawing instructions.
        """

class TextRegion(Region):
    LINES = []
    DEFAULT_STYLE = {}

    def __init__(self, text=[]):
        self.LINES = text

    def draw(self):
        maxx, maxy = self.parent.get_max_chars()
        for x, line in enumerate(self.LINES):
            if x > maxx or len(line) > maxy: continue
            self.parent.text_draw(x * maxx, 0, line)
