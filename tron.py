"""
Tron, classic arcade game. [Modified]
Name: Ana Karen López Baltazar - A01707750
Date: 17/09/2021
"""

from turtle import setup, title, bgcolor, hideturtle, ontimer
from turtle import tracer, listen, onkey, done, update
from freegames import square, vector
from random import randint

# from threading import Thread
# from playsound import playsound
# from pygame import mixer

# playsound('giorno.mp3')

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200


def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()
    p2xy.move(p2aim)
    p2head = p2xy.copy()

    change = randint(0, 9)
    if change == 0:
        p2aim.rotate(90)
    elif change == 1:
        p2aim.rotate(-90)

    if not inside(p1head) or p1head in p2body:
        print('Player violet wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player gold wins!')
        return

    if not inside(p1head) or p1head in p1body:
        print('Player gold wins!')
        return

    if not inside(p2head) or p2head in p2body:
        print('Player violet wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'violet')
    square(p2xy.x, p2xy.y, 3, 'gold')
    update()
    ontimer(draw, 50)

# Función para abrir archivo de música
# def music_func():
#    playsound('cancion.mp3')

# Definir función que llama audio
# music = Thread(target=music_func)
# music.daemon = True

# mixer.init()
# mixer.music.load("giorno.mp3")
# mixer.music.play()

# music = mixer.music.load('giorno.mp3')
# mixer.music.play(loops=-1)

# Iniciar musica
# music.start()


setup(420, 420, 370, 0)
title("Tron")
bgcolor("black")
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'Left')
onkey(lambda: p1aim.rotate(-90), 'Right')
draw()
done()
