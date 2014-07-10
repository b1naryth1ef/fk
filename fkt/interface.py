
class DrawInterface(object):
    def __init__(self):
        self.regions = []

    def draw(self):
        for reg in self.regions:
            reg.draw()

    def add_region(self, region):
        region.parent = self
        self.regions.append(region)
        region.draw()

    def rmv_region(self, region):
        self.regions.remove(region)

    def compile_operations(self):
        pass

    def text_draw(self, x, y, text, style={}):
        """
        Draws a set of styled `text`, at position (x, y) with any styles
        provided in `style`.
        """

    def clear(self):
        """
        Clears the entire screen for complete re-rendering.
        """

    def pixel_draw(self, x, y, style={}): pass

    def pixel_clear(self, x, y, style): pass

    def flip(self):
        """
        Actually updates the screen with all the content.
        """
