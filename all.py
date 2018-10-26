#!/usr/bin/env python3
#xd
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, SpeedRPM
import time

def X(brazo, n): # n movimientos
        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        for x in range(0, n):
                brazo.on_for_seconds(35, 0.305)
                brazo.on_for_seconds(-35, 0.305)
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def Xprima(brazo): # 3 movimientos
        X(brazo, 3)

def Yprima(base, n): # n movimientos
        for x in range(0, n):
                base.on_for_degrees(SpeedPercent(-40), 261.5)
                base.stop()
    
def Y(base, n): # n movimientos
        for x in range(0, n):
                base.on_for_degrees(SpeedPercent(40), 261.5)
                base.stop()

def Z(base, brazo, n): #4 + n movimientos
    X(brazo, 1)
    Y(base, n)
    Xprima(brazo)

def Zprima(base, brazo, n): #4 + n movimientos
    X(brazo, 1)
    Y(base, n)
    Xprima(brazo)


def D(brazo, base, n): # n movimientos

        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        Yprima(base, n)
        base.on_for_degrees(SpeedPercent(-50), 73)
        base.stop
        base.on_for_degrees(SpeedPercent(50), 73)
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def Dprima(brazo, base, n): # n movimientos 

        brazo.on_for_seconds(35, 0.28)
        brazo.stop()
        Y(base, n)
        base.on_for_degrees(SpeedPercent(50), 73)
        base.stop()
        base.on_for_degrees(SpeedPercent(-50), 73)
        base.stop()
        brazo.on_for_seconds(-35, 0.3)
        brazo.stop()

def U(brazo, base, n): #4 + n movimientos
        X(brazo, 2)
        D(brazo, base, n)
        X(brazo, 2)

def Uprima(brazo, base, n): #4 + n movimientos
        X(brazo, 2)
        Dprima(brazo, base, n)
        X(brazo, 2)

def L(brazo, base, n): #6 + n movimientos
    Y(base, 1)
    X(brazo, 1)
    D(brazo, base, n)
    Xprima(brazo)
    Yprima(brazo, 1)

def Lprima(brazo, base, n): #6 + n movimientos
    Y(base, 1)
    X(brazo, 1)
    Dprima(brazo, base, n)
    Xprima(brazo)
    Yprima(brazo, 1)

def F(brazo, base, n): #4 + n movimientos
    Xprima(brazo)
    D(brazo, base, n)
    X(brazo, 1)

def Fprima(brazo, base, n): #4 + n movimientos
    Xprima(brazo)
    D(brazo, base, n)
    X(brazo, 1)

def R(brazo, base, n): #6 + n movimientos
    Yprima(base, 1)
    X(brazo, 1)
    D(brazo, base, n)
    Xprima(brazo)
    Y(base, 1)

def Rprima(brazo, base, n): #6 + n movimientos
    Yprima(base, 1)
    X(brazo, 1)
    Dprima(brazo, base, n)
    Xprima(brazo)
    Y(base, 1)

def B(brazo, base, n): #4 + n movimientos
    X(brazo, 1)
    D(brazo, base, n)
    Xprima(brazo)

def Bprima(brazo, base, n): #4 + n movimientos
    X(brazo, 1)
    Dprima(brazo, base, n)
    Xprima(brazo)


def M(brazo, base):
    Y(base, 1)
    X(brazo, 1)
    Dprima(brazo, base, n)
    X(brazo, 2)
    D(brazo, base, n)
    X(brazo, 1)
    Yprima(base, 1)
    X(brazo, 3)

def Mprima(brazo, base):
    Y(base, 1)
    X(brazo, 1)
    D(brazo, base, 1)
    X(brazo, 2)
    Dprima(brazo, base, n)
    X(brazo, 1)
    Yprima(base, 1)
    X(brazo, 1)

#faltan revisar
def Eprima(brazo, base):
    Dprima(brazo, base,1)
    X(brazo, 2)
    Dprima(brazo, base,1)
    X(brazo, 2)
    Y(base, 1)

def S(brazo, base):
    X(brazo, 1)
    Dprima(brazo, base, 1)
    X(brazo, 2)
    D(brazo, base, 1)
    X(brazo, 1)
    Y(base, 1)
    X(brazo, 1)
    Yprima(base, 1)
