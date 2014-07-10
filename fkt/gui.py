from .interface import DrawInterface

import ctypes, time, logging, string
from sdl2 import *
from sdl2.sdlttf import *

class GUI(DrawInterface):
    FPS_TIME = 1.0 / 60

    log = logging.getLogger(__name__)

    SIZE = (500, 500)

    # Font information
    FONT_LINE_HEIGHT = (0, 0)
    FONT_SIZE = 15
    FONT = None

    DEFAULT_COLOR = SDL_Color(0, 0, 0, 255)

    CHANGED = True

    def flip(self):
        self.CHANGED = False
        SDL_RenderPresent(self.renderer)

    def text_draw(self, x, y, text, style={}):
        color = self.DEFAULT_COLOR
        if 'color' in style:
            color = SDL_Color(*style['color'])

        surf = TTF_RenderText_Solid(self.FONT, text, color)
        rect = SDL_Rect()
        SDL_GetClipRect(surf, rect)
        textu = SDL_CreateTextureFromSurface(self.renderer, surf)

        SDL_RenderCopy(self.renderer, textu, None, rect)
        self.CHANGED = True

        # WTF?
        self.flip()

    def clear(self):
        self.CHANGED = True
        SDL_RenderClear(self.renderer)

    def select_font(self, font_name):
        """
        Selects a new font based on a path for rendering. This must be called
        for font-face and font-size changes.
        """
        if self.FONT:
            TTF_CloseFont(self.FONT)
        self.FONT = TTF_OpenFont(font_name, self.FONT_SIZE)
        self.cache_line_height()

    def cache_line_height(self):
        """
        Obtains the largest (width, height) combination that will ever be
        rendered with the current font.
        """
        if not self.FONT:
            raise Exception("No font selected to cache line height for!")
        x, y, _x, _y = 0, 0, ctypes.c_int(0), ctypes.c_int(0)
        for char in string.printable:
            TTF_SizeUTF8(self.FONT, char, ctypes.pointer(_x), ctypes.pointer(_y))
            if _x > x: x = _x
            if _y > y: y = _y
        self.FONT_LINE_HEIGHT = (x.value, y.value)

    def setup(self, parent):
        self.parent = parent

        SDL_Init(SDL_INIT_EVERYTHING)
        TTF_Init()
        self.window = SDL_CreateWindow(self.parent.name,
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            self.SIZE[0], self.SIZE[1], SDL_WINDOW_SHOWN)

        self.renderer = SDL_CreateRenderer(self.window, 0, SDL_RENDERER_ACCELERATED)

        SDL_SetRenderDrawColor(self.renderer, 255, 0, 0, 255)
        self.clear()
        self.flip()

        self.select_font("ubuntu.ttf")

    def loop(self):
        event = SDL_Event()
        while True:
            while SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == SDL_QUIT:
                    self.parent.handle_quit()
                elif event.type == SDL_KEYDOWN:
                    if event.key.keysym.sym <= 256:
                        self.parent.handle_key_down(chr(event.key.keysym.sym))
                    else:
                        self.log.debug("Unhandled keydown: %s", event.key.keysym.sym)
                elif event.type == SDL_KEYUP:
                    if event.key.keysym.sym <= 256:
                        self.parent.handle_key_down(chr(event.key.keysym.sym))
                    else:
                        self.log.debug("Unhandled keyup: %s", event.key.keysym.sym)

            if self.CHANGED:
                self.flip()

            time.sleep(self.FPS_TIME)

    def shutdown(self):
        if self.FONT: TTF_CloseFont(self.FONT)
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
        SDL_Quit()
        TTF_Quit()
