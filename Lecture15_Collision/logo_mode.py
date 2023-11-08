from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE

import game_framework


def init():
    global image
    image = load_image('gameover.png')
    logo_start_time = get_time()
    pass


def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()
    image.draw(800, 300)
    update_canvas()
    pass


def pause():
    pass


def resume():
    pass