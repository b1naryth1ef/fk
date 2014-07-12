import sdl2.sdlttf as ttf
import os, ctypes, string

class Font(object):
    def __init__(self, path, name, data):
        self.path = path
        self.name = name
        self.style = []

        self.cached_sizes = {}

        if '=' in data:
            self.style = map(str.lower, data.split("=")[1].split(","))

    def get_style(self):
        return self.data.get("style").lower().split(",")

    def get_size(self, s):
        if s in self.cached_sizes:
            return self.cached_sizes[s][0]

    def get_bounds(self, s):
        if s not in self.cached_sizes:
            raise Exception("Font not opened for size %s" % s)
        return self.cached_sizes[s][1]

    def open_size(self, s):
        self.cached_sizes[s] = [ttf.TTF_OpenFont(self.path, s), None]
        self.cache_size_bounds(s)
        return self.cached_sizes[s]

    def close_size(self, s):
        ttf.TTF_CloseFont(self.cached_sizes[s][0])
        del self.cached_sizes[s]

    def cache_size_bounds(self, s):
        x, y, _x, _y = 0, 0, ctypes.c_int(0), ctypes.c_int(0)
        for char in string.printable:
            ttf.TTF_SizeUTF8(self.get_size(s), char, ctypes.pointer(_x), ctypes.pointer(_y))
            if _x > x: x = _x
            if _y > y: y = _y
        self.cached_sizes[s][1] = (x.value, y.value)

    def close(self):
        for v in self.cached_sizes.values():
            ttf.TTF_CloseFont(v[0])

    def __repr__(self):
        return "<Font %s @ %s>" % (self.name, self.path)

class FontDB(object):
    def __init__(self):
        self.fonts = []
        self.refresh()

    def refresh(self):
        self.fonts = []

        for entry in os.popen("fc-list").read().split("\n"):
            if not entry: continue
            path, name, data = entry.split(":", 2)
            self.fonts.append(Font(path, name, data))

    def search(self, name, *style):
        # TODO: style, make readable lewl
        results = []
        for font in self.fonts:
            if name in font.name.lower():
                if len(style) != len(font.style): continue
                for s in style:
                    if s not in font.style:
                        break
                else:
                    results.append(font)
        return results
