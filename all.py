#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, SpeedRPM
import time
def flip(brazo, vueltas):
        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        for x in range(0, vueltas):
                brazo.on_for_seconds(35, 0.305)
                brazo.on_for_seconds(-35, 0.305)
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def girar_derecha(base, vueltas):
        for x in range(0, vueltas):
                base.on_for_degrees(SpeedPercent(-40), 261.5)
                base.stop()
    
def girar_izquierda(base, vueltas):
        for x in range(0, vueltas):
                base.on_for_degrees(SpeedPercent(40), 261.5)
                base.stop()

def rotate_right(brazo, base, vueltas):

        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        girar_izquierda(base, vueltas)
        base.on_for_degrees(SpeedPercent(50), 73)
        base.stop()
        base.on_for_degrees(SpeedPercent(-50), 73)
        base.stop()
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def rotate_left(brazo, base, vueltas):

        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        girar_derecha(base, vueltas)
        base.on_for_degrees(SpeedPercent(-50), 73)
        base.stop
        base.on_for_degrees(SpeedPercent(50), 73)
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def U(brazo, base):
        flip(brazo, 2)
        rotate_left(brazo, base, 1)
        flip(brazo, 2)

def Uprima(brazo, base):
        flip(brazo, 2)
        rotate_right(brazo, base, 1)
        flip(brazo, 2)

def L(brazo, base):
    girar_izquierda(base, 1)
    flip(brazo, 1)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)
    girar_derecha(base, 1)
    flip(brazo, 2)
    girar_derecha(base, 2)

def Lprima(brazo, base):
    girar_izquierda(base, 1)
    flip(brazo, 1)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)
    girar_derecha(base, 1)
    flip(brazo, 2)
    girar_derecha(base, 2)

def F(brazo, base):
    flip(brazo, 3)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)

def Fprima(brazo, base):
    flip(brazo, 3)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)

def R(brazo, base):
    girar_derecha(base, 1)
    flip(brazo, 1)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)
    girar_izquierda(base, 1)
    flip(brazo, 2)
    girar_derecha(base, 2)

def Rprima(brazo, base):
    girar_derecha(base, 1)
    flip(brazo, 1)
    rotate_right(brazo, base, 1)
    flip(brazo, 1)
    girar_izquierda(base, 1)
    flip(brazo, 2)
    girar_derecha(base, 2)

def B(brazo, base):
    flip(brazo, 1)
    rotate_left(brazo, base, 1)
    flip(brazo, 3)

def Bprima(brazo, base):
    flip(brazo, 1)
    rotate_right(brazo, base, 1)
    flip(brazo, 3)

def D(brazo, base):
        rotate_left(brazo, base, 1)

def Dprima(brazo, base):
        rotate_right(brazo, base, 1)

def M(brazo, base):
    girar_izquierda(base, 1)
    flip(brazo, 1)
    rotate_right(brazo, base, 1)
    flip(brazo, 2)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)
    girar_derecha(base, 1)
    flip(brazo, 3)

def Mprima(brazo, base):
    girar_izquierda(base, 1)
    flip(brazo, 1)
    rotate_left(brazo, base, 1)
    flip(brazo, 2)
    rotate_right(brazo, base, 1)
    flip(brazo, 1)
    girar_derecha(base, 1)
    flip(brazo, 1)

#faltan revisar
def Eprima(brazo, base):
    rotate_right(brazo, base,1)
    flip(brazo, 2)
    rotate_right(brazo, base,1)
    flip(brazo, 2)
    girar_izquierda(base, 1)

def S(brazo, base):
    flip(brazo, 1)
    rotate_right(brazo, base, 1)
    flip(brazo, 2)
    rotate_left(brazo, base, 1)
    flip(brazo, 1)
    girar_izquierda(base, 1)
    flip(brazo, 1)
    girar_derecha(base, 1)

