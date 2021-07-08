# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from PCA9685_wrapper import PWM


if __name__ == "__main__":
    ch0 = PWM(0)

    ch0.setPWM(500)
    time.sleep(1)

    ch0.setPWM(5000)
    time.sleep(1)

    ch0.setPWM(4095)
    time.sleep(1)

    ch0.setPWM(-1)
    time.sleep(1)

    ch0.setPWM("a")
    time.sleep(1)
