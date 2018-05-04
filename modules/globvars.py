#!/usr/bin/env python3
serial_num = None
last_digit = None
batteries  = None
indicator  = None
strikes    = 0

all_vars = [serial_num, last_digit, batteries, indicator]

def get_serial_num():
    global serial_num
    if serial_num==None:
        serial_num = input("    {0:16}".format("Serial#:")).strip().lower()
    return serial_num

def set_serial_num(sn):
    global serial_num
    serial_num = sn

def get_last_digit():
    global serial_num
    global last_digit
    if last_digit==None:
        try:
            last_digit = int(get_serial_num()[-1:])
        except BaseException:
            serial_num = None
            last_digit = None
            return -1
    return last_digit

def set_last_digit(ld):
    global last_digit
    last_digit = ld

def get_batteries():
    global batteries
    if batteries==None:
        try:
            batteries = int(input("    {0:16}".format("#Batteries:")).strip().lower())
        except:
            batteries = None
            return -1
    return batteries

def set_batteries(b):
    global batteries
    batteries = b

def get_indicator():
    global indicator
    if indicator==None:
        indicator = input("    {0:16}".format("Indicator:")).strip().upper().split(' ')
    return indicator

def set_indicator(i):
    global indicator
    indicator = i

def get_strikes():
    return strikes

def set_strikes(i):
    global strikes
    strikes = i

def reset_all():
    for var in all_vars:
        var = None
    global strikes
    strikes = 0
        