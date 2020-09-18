from pico2d import *

open_canvas()
img=load_image('character.png')
gra=load_image('grass.png')

for x in range(0,800,2):
    clear_canvas()
    
    gra.draw(400,30)
    img.draw_now(x,80)
    
    update_canvas()
    get_events()
    delay(0.01)

delay(5)
close_canvas()
