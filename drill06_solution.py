import os
from pico2d import *
import random
os.chdir(os.path.dirname(__file__))
TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resource():
    global TUK_ground,character
    global arrow
    arrow=load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    global mx,my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_MOUSEMOTION:
            mx,my=event.x,TUK_HEIGHT-1-event.y
        elif event.type ==SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            points.append((event.x,TUK_HEIGHT-1-event.y)) #클릭된 점 리스트에 추가
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running,cx,cy,frame
    global t
    global action
    global mx,my
    global points

    mx,my=0,0
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action =3
    points=[]
    set_new_target_arrow()


def set_new_target_arrow():
    global sx,sy,hx,hy,t
    global action
    global frame 
    global target_exists
    
    if points: #목표가 남아있으면
        sx,sy=cx,cy # p1 : 시작점
        #hx,hy=50,50
        hx,hy=points[0] # p2 : 끝점
        t=0.0
        action = 1 if sx<hx else 0
        frame=0
        target_exists =True
    else:
        action=3 if action==1 else 2 #이전 이동방향을 고정
        frame =0
        target_exists=False


def rander_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for p in points:
        arrow.draw(p[0],p[1])
    arrow.draw(mx,my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global cx,cy
    global t
    global action

    frame = (frame + 1) % 8
    if target_exists:
        if t<=1.0:
            cx=(1-t)*sx+t*hx # c : current, s : start, h : end
            cy=(1-t)*sy+t*hy
            t+=0.001
        else: #목표에 도달하면
            cx,cy=hx,hy #위치 강제 일치
            del points[0] # 도착했던 점 삭제
            set_new_target_arrow()
    elif points: #목표 지점이 없는 상황에서 새 목표 지점이 추가되면
        set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resource()
reset_world()

while running:
    rander_world() #필드의 현재 내용 그림 
    handle_events() # 사용자 입력
    update_world() # 필드 내의 객체들의 상호작용 계산, update

close_canvas()




