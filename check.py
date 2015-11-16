#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import time
from tp4000zc import Dmm

try:
    port = '/dev/ttyUSB0'
    stop_loop = False
    loop_limit = 100

    dmm = Dmm(port)

    while not stop_loop:
        accum = 0
        # read a value
        val = dmm.read()

        print val.text       # print the text representation of the value
                             # something like: -4.9 millivolts DC
        print val.numericVal # and the numeric value
                             # ie: -0.0048
        time.sleep(2)
        accum += 1
        if accum > loop_limit:
            stop_loop = True

finally:
    # recycle the serial port
    dmm.close()
