from pygame import *
import sys
from pygame.locals import QUIT
import random


lista1 = [random.randint(100,200) for _ in range(50)]

num_categ = 5
num_min = min(lista1)
num_max = max(lista1)
tam_categ = (num_max - num_min)/num_categ

lista1_final = [0] * num_categ

def organizarCateg(lista1, lista1_final):
    for i in range(len(lista1)):
        if lista1[i] == num_max:
            lista1_final[-1] += 1
            continue
        
        for i_categ in range(num_categ):
            lim_inf = num_min + i_categ*tam_categ
            lim_sup = lim_inf + tam_categ

            if lim_inf <= lista1[i] < lim_sup:
                lista1_final[i_categ] += 1
                break
    return lista1_final

print(organizarCateg(lista1, lista1_final))


lista2 = [1,2,3,4,5,6,7,8,9,10]

num_categ = 4
tam_categ = random.randint(1, len(lista2))

lista2_final = [0] * num_categ

def contaCateg(lista2, lista2_final,):
    for i in range(len(lista2)):

        for i_categ in range(num_categ):
            escolha = random.sample(lista2, tam_categ)
            soma = 0
            for i_escolha in range(len(escolha)):
                soma += escolha[i_escolha]
                if soma < len(lista2):
                    lista2_final[i_categ] += 1
                    break
    return lista2_final

print(contaCateg(lista2, lista2_final,))


escolha_lista = input('Digite todos números da lista: ')
lista3 = [int(item) for item in escolha_lista.split()]


num_categ = 3
num_min = min(lista3)
num_max = max(lista3)
tam_categ = (num_max - num_min)/num_categ

lista3_final = [0] * num_categ

def organizaCateg(lista3, lista3_final):
    for i in range(len(lista3)):
        if lista3[i] == num_max:
            lista3_final[-1] += 1
            continue
        
        for i_categ in range(num_categ):
            lim_inf = num_min + i_categ*tam_categ
            lim_sup = lim_inf + tam_categ

            if lim_inf <= lista3[i] < lim_sup:
                lista3_final[i_categ] += 1
                break
    return lista3_final

print(organizaCateg(lista3, lista3_final))


def cor_aleatoria():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

cor_coluna = [cor_aleatoria(), cor_aleatoria(), cor_aleatoria(), cor_aleatoria(), cor_aleatoria()]

def draw1(window):
    window_altura = window.get_height()
    for i in range(len(lista1_final)):
        x = 400 + i * 50
        h = 20 * lista1_final[i]
        draw.rect(window, (cor_coluna[i]), (x, window_altura - h - 220, 25, h))

def draw2(window):
    window_altura = window.get_height()
    for i in range(len(lista2_final)):
        x = 400 + i * 50
        h = 20 * lista2_final[i]
        draw.rect(window, (cor_coluna[i]), (x, window_altura - h - 220, 25, h))

def draw3(screen):
    screen_altura = screen.get_height()
    for i in range(len(lista3_final)):
        x = 400 + i * 50
        h = 20 * lista3_final[i]
        draw.rect(screen, (cor_coluna[i]), (x, screen_altura - h - 220, 25, h))

init()
window = display.set_mode((1100,700))
fonts = font.SysFont(None, 25)
running = True


modo_hist = '1'

while running:
    for ev in event.get():
        if ev.type == QUIT:
            running == False
            sys.exit()
        if ev.type == KEYDOWN:
            if ev.key == K_1:
                modo_hist = '1'
            elif ev.key == K_2:
                modo_hist = '2'
            elif ev.key == K_3:
                modo_hist = '3'
                       

    
    window.fill((255, 255, 255))

    draw.line(window, (0,0,0), (325,480),(325,100),(3))
    draw.line(window, (0,0,0), (325,480),(750,480),(3))
    draw.line(window, (0,0,0), (315,460),(335,460),(3))
    draw.line(window, (0,0,0), (315,440),(335,440),(3))
    draw.line(window, (0,0,0), (315,420),(335,420),(3))
    draw.line(window, (0,0,0), (315,400),(335,400),(3))
    draw.line(window, (0,0,0), (315,380),(335,380),(3))
    draw.line(window, (0,0,0), (315,360),(335,360),(3))
    draw.line(window, (0,0,0), (315,340),(335,340),(3))
    draw.line(window, (0,0,0), (315,320),(335,320),(3))
    draw.line(window, (0,0,0), (315,300),(335,300),(3))
    draw.line(window, (0,0,0), (315,280),(335,280),(3))
    draw.line(window, (0,0,0), (315,260),(335,260),(3))
    draw.line(window, (0,0,0), (315,240),(335,240),(3))
    draw.line(window, (0,0,0), (315,220),(335,220),(3))
    draw.line(window, (0,0,0), (315,200),(335,200),(3))
    draw.line(window, (0,0,0), (315,180),(335,180),(3))
    draw.line(window, (0,0,0), (315,160),(335,160),(3))
    draw.line(window, (0,0,0), (315,140),(335,140),(3))
    draw.line(window, (0,0,0), (315,120),(335,120),(3))


    numero1 = fonts.render('1', True, (0,0,0))
    window.blit(numero1, (305,455))

    numero2 = fonts.render('2', True, (0,0,0))
    window.blit(numero2, (305,435))

    numero3 = fonts.render('3', True, (0,0,0))
    window.blit(numero3, (305,415))

    numero4 = fonts.render('4', True, (0,0,0))
    window.blit(numero4, (305,395))

    numero5 = fonts.render('5', True, (0,0,0))
    window.blit(numero5, (305,375))

    numero6 = fonts.render('6', True, (0,0,0))
    window.blit(numero6, (305,355))

    numero7 = fonts.render('7', True, (0,0,0))
    window.blit(numero7, (305,335))

    numero8 = fonts.render('8', True, (0,0,0))
    window.blit(numero8, (305,315))

    numero9 = fonts.render('9', True, (0,0,0))
    window.blit(numero9, (305,295))

    numero10 = fonts.render('10', True, (0,0,0))
    window.blit(numero10, (295,275))

    numero11 = fonts.render('11', True, (0,0,0))
    window.blit(numero11, (295,255))

    numero12 = fonts.render('12', True, (0,0,0))
    window.blit(numero12, (295,235))

    numero13 = fonts.render('13', True, (0,0,0))
    window.blit(numero13, (295,215))

    numero14 = fonts.render('14', True, (0,0,0))
    window.blit(numero14, (295,195))

    numero15 = fonts.render('15', True, (0,0,0))
    window.blit(numero15, (295,175))

    numero16 = fonts.render('16', True, (0,0,0))
    window.blit(numero16, (295,155))

    numero17 = fonts.render('17', True, (0,0,0))
    window.blit(numero17, (295,135))

    numero18 = fonts.render('18', True, (0,0,0))
    window.blit(numero18, (295,115))

    if modo_hist == '1':
        draw1(window)
    elif modo_hist == '2':
        draw2(window)
    elif modo_hist == '3':
        draw3(window)

    display.update()