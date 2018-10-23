# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 10:09
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : ex3.py
# @Software: PyCharm
"""
用Bresenham画线算法实现水平、垂直、斜率大于1、斜率小于1、斜率为正、
斜率为负等各种情况（不能直接调用OpenGL画线函数）。
"""
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 点1为起点,点2为终点
x1 = 0
y1 = 0
x2 = 1
y2 = 5
left_button_state = 0  # 是否拖动的标志
clearFlag = 0  # 清屏标志

def plotLineLow(sx,sy,tx,ty):
    """
    Bresenham的画线方法,这是以x为锚点
    :param sx:源点的x值
    :param sy: 源点的y值
    :param tx: 终点的x值
    :param ty: 终点的y值
    """
    dx = tx - sx
    dy = ty - sy
    yi = 1
    if dy <0:
        yi = -1
        dy = -dy
    D = 2*dy-dx
    y = sy
    glPointSize(4)
    glBegin(GL_POINTS)
    for x in range(sx,tx):
        print(x,y)
        glVertex2i(int(x),int(y))
        if D>0:
            y+=yi
            D-=2*dx
        D +=2*dy
    glEnd()
def plotLineHigh(sx,sy,tx,ty):
    """
    Bresenham的画线方法,这是以y为锚点
    :param sx:源点的x值
    :param sy: 源点的y值
    :param tx: 终点的x值
    :param ty: 终点的y值
    """
    dx = tx - sx
    dy = ty - sy
    xi = 1
    if dx <0:
        xi = -1
        dx = -dx
    D = 2*dx-dy
    x = sx
    glPointSize(4)
    glBegin(GL_POINTS)
    for y in range(sy,ty):
        print(x,y)
        glVertex2i(int(x),int(y))
        if D>0:
            x+=xi
            D-=2*dy
        D +=2*dx
    glEnd()
def Bresenham(sx,sy,tx,ty):
    """
    利用Bresenham的画线方法,替代原来的openGL的GL_LINES函数,要根据斜率的正负选择不同的画线策略
    :param sx:源点的x值
    :param sy: 源点的y值
    :param tx: 终点的x值
    :param ty: 终点的y值
    """
    if abs(ty-sy)<abs(tx-sx):
        if (sx>tx):
            plotLineLow(tx,ty,sx,sy)
        else:
            plotLineLow(sx,sy,tx,ty)
    else:
        if (sy>ty):
            plotLineHigh(tx,ty,sx,sy)
        else:
            plotLineHigh(sx,sy,tx,ty)


def myInit():  # 初始化函数
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.5, 0.4, 0.9)
    glPointSize(10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.0, 640, 0.0, 480)


def mouseMotionFunc(x, y):
    if (0 == left_button_state):
        return
    global x1
    global y1
    global x2
    global y2
    x2 = x
    y2 = y
    drawFunc()


def drawFunc():  # 画线函数
    glClear(GL_COLOR_BUFFER_BIT)
    Bresenham(x1,480-y1,x2,480-y2)
    # glBegin(GL_LINES)
    # glVertex2i(x1, 480 - y1)
    # glVertex2i(x2, 480 - y2)
    # glEnd()
    glFlush()


# def mouseButton(button, mode, x, y):
#     if button == GLUT_RIGHT_BUTTON:
#         camera.mouselocation = [x, y]
#
def mouseEvent(button, state, x, y):  # 捕捉鼠标坐标的函数
    global x1
    global y1
    global left_button_state
    global clearFlag
    left_button_state = 0
    if (button == GLUT_LEFT_BUTTON):  # 拖动的时候
        if state == GLUT_DOWN:
            x1 = x
            y1 = y
            left_button_state = 1  # 更新左键的状态
    elif (button == GLUT_MIDDLE_BUTTON):  # 右键清除全部东西
        glClear(GL_COLOR_BUFFER_BIT)


def processMenuEvents(option):
    global clearFlag
    if option == GL_RED:
        glColor3f(1.0, 0, 0)
        drawFunc()
    if option == GL_BLUE:
        glColor3f(0, 0, 1)
        drawFunc()
    if option == GL_GREEN:
        glColor3f(0, 1.0, 0)
        drawFunc()



def keyBoardEvent(key, x, y):
    global x1, x2, y1, y2
    if key == b'w':
        y1 -= 1
        y2 -= 1
    if key == b's':
        y1 += 1
        y2 += 1
    if key == b'a':
        x1 -= 1
        x2 -= 1
    if key == b'd':
        x1 += 1
        x2 += 1
    print(key)
    drawFunc()


def glutCreateMenus():
    menu = glutCreateMenu(processMenuEvents)

    glutAddMenuEntry("Red", GL_RED)
    glutAddMenuEntry("Blue", GL_BLUE)
    glutAddMenuEntry("Green", GL_GREEN)
    # glutAddMenuEntry("Clear",123)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("ex3")
    myInit()
    glutDisplayFunc(drawFunc)
    glutMouseFunc(mouseEvent)
    glutMotionFunc(mouseMotionFunc)
    glutKeyboardFunc(keyBoardEvent)
    glutCreateMenus()
    glutMainLoop()

if __name__ == '__main__':
    main()