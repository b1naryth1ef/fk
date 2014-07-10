

class Region(object):
    def __init__(self, parent):
        self.parent = parent

    def draw(self):
        """
        Turns a custom region into a set drawing instructions.
        """

class TextRegion(Region):
    LINES = []
    DEFAULT_STYLE = {}

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
            self.parent.char_draw(x * self.parent.FONT_LINE_HEIGHT[0], 0, line)


class Frame(object):
    def __init__(self, *regions):
        self.regions = {i.id: i for i in regions}
