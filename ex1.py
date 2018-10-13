# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 22:19
# @Author  : seeledu
# @email   : seeledu@bug.moe
# @File    : ex1.py
# @Software: PyCharm
"""
    实验一:画点和线;
    创新点,变换颜色.
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import common
import sys

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotate(1,0,1,0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(0.3,0.3)
    glVertex2f(0.4,0.4)
    glEnd()
    glColor3f(1.0,0.5,0.3)
    glBegin(GL_LINES)
    glVertex2f(-0.1,-0.9)
    glVertex2f(0.8,-0.5)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(400,400)
    glutCreateWindow("ex1")
    glutDisplayFunc(drawFunc)
    # glutIdleFunc(drawFunc())
    glutMainLoop()
if __name__ == '__main__':
    main()
