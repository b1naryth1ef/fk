

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

    def calc_max_chars(self):
        """
        Calculates the maximum number of characters that can be drawn
        on the screen for width/height dimensions.
        """
        x = self.parent.SIZE[0] / self.parent.FONT_LINE_HEIGHT[0]
        y = self.parent.SIZE[1] / self.parent.FONT_LINE_HEIGHT[1]

        return x, y

    def draw(self):
        maxx, maxy = self.calc_max_chars()
        for x, line in enumerate(self.LINES):
            if x > maxx or len(line) > maxy: continue
            self.parent.text_draw(x * self.parent.FONT_LINE_HEIGHT[0], 0, line)
