# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 12:45
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : ex2.py
# @Software: PyCharm
"""
 exercise2:利用鼠标、键盘，菜单等方式对图元进行交互操作
"""
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
1、用鼠标拖动画直线，线段终点始终跟随鼠标移动； 
2、使用菜单界面修改直线的颜色；
3、利用键盘控制直线在屏幕上移动；
"""
# 点1为起点,点2为终点
x1 = 0
y1 = 0
x2 = 0
y2 = 0
left_button_state = 0
clearFlag = 0  # 清屏标志


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
    #  x1 = x2
    # y1 = y2


def drawFunc():  # 画线函数
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2i(x1, 480 - y1)
    glVertex2i(x2, 480 - y2)
    glEnd()
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
        elif (button):  # 右键清除全部东西
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
    # if option == 123:
    #     clearFlag = 1
    #     drawFunc()


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
    glutCreateWindow("ex2")
    myInit()
    glutDisplayFunc(drawFunc)
    glutMouseFunc(mouseEvent)
    glutMotionFunc(mouseMotionFunc)
    glutKeyboardFunc(keyBoardEvent)
    glutCreateMenus()
    glutMainLoop()


if __name__ == '__main__':
    main()
