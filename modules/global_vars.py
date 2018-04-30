serial_num = None
last_digit = None
batteries  = None
indicator  = None

all_vars = [serial_num, last_digit, batteries, indicator]

def get_serial_num():
    return serial_num

def set_serial_num(sn):
    global serial_num
    serial_num = sn

def get_last_digit():
    return last_digit

def set_last_digit(ld):
    global last_digit
    last_digit = ld

def get_batteries():
    return batteries

def set_batteries(b):
    global batteries
    batteries = b

def get_indicator():
    return indicator

def set_indicator(i)
    global indicator
    indicator = i

def reset_all():
    for var in all_vars:
        var = None
        