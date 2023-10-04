import os
from pico2d import *
os.chdir(os.path.dirname(__file__))
TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resource():
    global TUK_ground,character
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world(TUK_WIDTH, TUK_HEIGHT):
    global running,x,y,frame
    running = True
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0


def rand_world(TUK_WIDTH, TUK_HEIGHT, TUK_ground, character, x, y, frame):
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()


def update_world(frame):
    frame = (frame + 1) % 8


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resource()
reset_world(TUK_WIDTH, TUK_HEIGHT)

while running:
    rand_world(TUK_WIDTH, TUK_HEIGHT, TUK_ground, character, x, y, frame) #필드의 현재 내용 그림 
    handle_events() # 사용자 입력
    update_world(frame) # 필드 내의 객체들의 상호작용 계산, update

close_canvas()




