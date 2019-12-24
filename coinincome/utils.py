# -*- coding: utf-8 -*-


def calculate_unit(unit):
    units = ["", "K", "M", "G", "T", "P", "E", "Z", "Y"]
    index = 0
    while True:
        if unit == units[index]:
            break
        index = index + 1
    return pow(1000, index)
