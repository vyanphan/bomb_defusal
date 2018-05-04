#!/usr/bin/env python3
serial_num    = None
last_digit    = None
batteries     = None
indicator     = None
strikes       = 0
parallel_port = None

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
    global strikes
    return strikes

def set_strikes(i):
    global strikes
    strikes = i

def get_parallel_port():
    global parallel_port
    if parallel_port==None:
        user_input = input("    {0:16}".format("Parallel port:")).strip().lower()
        if user_input=='y' or user_input=='yes' or user_input=='t' or user_input=='true':
            parallel_port = True
        elif user_input=='n' or user_input=='no' or user_input=='f' or user_input=='false':
            parallel_port = False
        else:
            parallel_port = None
            print("  Input must be yes or no!")
    return parallel_port

def set_parallel_port(i):
    global parallel_port
    parallel_port = i

def reset_all():
    for var in all_vars:
        var = None
    global strikes
    strikes = 0
        