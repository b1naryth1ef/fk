from .interface import DrawInterface
from .fonts import FontDB

import ctypes, time, logging
from sdl2 import *
from sdl2.sdlttf import *

class GUI(DrawInterface):
    SIZE = (500, 500)

    DEFAULT_COLOR = SDL_Color(0, 0, 0, 255)

    CHANGED = True

    def __init__(self):
        DrawInterface.__init__(self)
        self.log = logging.getLogger(__name__)

        SDL_Init(SDL_INIT_EVERYTHING)
        TTF_Init()

        self.size = (500, 500)

        # FPS
        self.fps = 60
        self.fps_time = 1.0 / self.fps

        # Fonts
        self.fontdb = FontDB()
        q = self.fontdb.search("ubuntu mono", "regular")  # TODO: config
        if not len(q) == 1:
            raise Exception("Could not find font: %s" % q)
        self.font = q[0]
        self.font_size = 20

        self.font.open_size(self.font_size)

    def get_max_chars(self):
        font_bounds = self.font.get_bounds(self.font_size)
        x = self.size[0] / font_bounds[0]
        y = self.size[1] / font_bounds[1]

        return x, y

    def flip(self):
        self.CHANGED = False
        SDL_RenderPresent(self.renderer)

    def text_draw(self, x, y, text, style={}):
        print text, x, y
        color = self.DEFAULT_COLOR
        if 'color' in style:
            color = SDL_Color(*style['color'])

        font = self.font.get_size(self.font_size)
        surf = TTF_RenderText_Solid(font, text, color)
        rect = SDL_Rect()
        SDL_GetClipRect(surf, rect)
        rect.x = x
        rect.y = y
        textu = SDL_CreateTextureFromSurface(self.renderer, surf)

        SDL_RenderCopy(self.renderer, textu, None, rect)
        self.CHANGED = True

        # WTF?
        self.flip()

    def clear(self):
        self.CHANGED = True
        SDL_RenderClear(self.renderer)

    def setup(self, parent):
        self.parent = parent

        self.window = SDL_CreateWindow(self.parent.name,
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            self.SIZE[0], self.SIZE[1], SDL_WINDOW_SHOWN)

        self.renderer = SDL_CreateRenderer(self.window, 0, SDL_RENDERER_ACCELERATED)

        SDL_SetRenderDrawColor(self.renderer, 255, 0, 0, 255)
        self.clear()
        self.flip()

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
                elif event.type == SDL_WINDOWEVENT: pass
                    # self.flip()
                    # self.flip()

            if self.CHANGED:
                self.flip()

            time.sleep(self.fps_time)

    def shutdown(self):
        self.font.close()
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
        SDL_Quit()
        TTF_Quit()
