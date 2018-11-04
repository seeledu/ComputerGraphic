# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 10:03
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : ex4.py
# @Software: PyCharm
"""
掌握Bezier样条曲面生成思想、复习基本图元绘制、交互操作相关内容.
"""
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

x1 = -40.0
y1 = 40.0
z1 = 0.0
x2 = -10.0
y2 = 200.0
z2 = 0.0
x3 = 10.0
y3 = -200.0
z3 = 0.0
x4 = 40.0
y4 = 40.0
z4 = 0.0
ctrlPts = [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4]]


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(10.0)
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINE_STRIP)
    for k in range(50):
        glEvalCoord1f(1.0*k/50.0)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(400,400)
    glMap1f(GL_MAP1_VERTEX_3,0.0,1.0,ctrlPts)
    glEnable(GL_MAP1_VERTEX_3)
    glutCreateWindow("ex1")
    glutDisplayFunc(drawFunc)
    # glutIdleFunc(drawFunc())
    glutMainLoop()
if __name__ == '__main__':
    main()


