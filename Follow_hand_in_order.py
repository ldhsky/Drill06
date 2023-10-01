from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

moving = True

HandPos = list()

frame = 0

dir = True

prevframe = False

def handle_events():
    global moving
    global mouse_x, mouse_y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            moving = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            HandPos.append((event.x, TUK_HEIGHT - 1 - event.y))

mouse_x, mouse_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

player_x, player_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

hide_cursor()

while moving:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if HandPos:
        if abs(HandPos[0][0] - player_x) < 1 and abs(HandPos[0][1] == player_y) < 1:
            HandPos.pop(0)

    hand_arrow.draw(mouse_x, mouse_y)

    if HandPos:
        for pos in HandPos:
            hand_x, hand_y = pos
            hand_arrow.draw(hand_x, hand_y)

        first_hand_pos_x, first_hand_pos_y = HandPos[0]
        if first_hand_pos_x < player_x:
            dir = False
        elif first_hand_pos_x > player_x:
            dir = True

    if dir:
        if prevframe:
            prevframe = False
            frame = 0
        character.clip_draw(frame % 8 * 100, 100, 100, 100, player_x, player_y)
    else:
        if not prevframe:
            prevframe = True
            frame = 0
        character.clip_draw(frame % 8 * 100, 0, 100, 100, player_x, player_y)

    update_canvas()
    handle_events()

    t = 0.07

    if HandPos:
        player_x = (1-t) * player_x + t * HandPos[0][0]
        player_y = (1-t) * player_y + t * HandPos[0][1]

    frame += 1

    delay(0.02)

close_canvas()