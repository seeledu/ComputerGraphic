# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 9:55
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : drawer.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 12:45
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : ex2.py
# @Software: PyCharm
"""
 exercise2:利用鼠标、键盘，菜单等方式对图元进行交互操作
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import common
import sys
x1 = 0
y1 = 0
x2 = 0
y2 = 0
left_button_state = 0
def myInit():#初始化函数
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.5,0.4,0.9)
    glPointSize(10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.0, 640, 0.0, 480)
def mouseMotionFunc(x,y):
    if (0==left_button_state):
        return
    global x1
    global y1
    global x2
    global y2
    x2 = x
    y2 = y
    drawFunc()
    x1 = x2
    y1 = y2


def drawFunc():#画线函数
    #glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2i(x1,480-y1)
    glVertex2i(x2,480-y2)
    glEnd()
    glFlush()
# def mouseButton(button, mode, x, y):
#     if button == GLUT_RIGHT_BUTTON:
#         camera.mouselocation = [x, y]
#
def mouseEvent(button,state,x,y):#捕捉鼠标坐标的函数
    global x1
    global y1
    global left_button_state
    left_button_state = 0
    if (button == GLUT_LEFT_BUTTON):#拖动的时候
        if state == GLUT_DOWN:
            x1 = x
            y1 = y
            left_button_state = 1 #更新左键的状态
    elif (button == GLUT_RIGHT_BUTTON):#右键清除全部东西
        glClear(GL_COLOR_BUFFER_BIT)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("ex2")
    myInit()
    glutDisplayFunc(drawFunc)
    glutMouseFunc(mouseEvent)
    glutMotionFunc(mouseMotionFunc)
    glutMainLoop()
if __name__ == '__main__':
    main()
