import PySimpleGUIWeb as sg
import re
from datetime import datetime, timedelta
import math

#sg.theme('Dark')

def open_window():
    # Appologies for the giant and un-maintainable wall of text that follows.
    # I messed with for loops to draw out the layout for the grid but with
    # needing to change multiple things in each button it was going to be
    # quicker for me to just write it out like this. Please merge a fix!
    layout_grid = [[sg.B('*', size=(3, 1), key=(0,24), pad=((1,0),(1,0))),sg.B('*', size=(3, 1), key=(1,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(2,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(3,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(4,24), pad=((0,1),(1,0))),sg.B('*', size=(3, 1), key=(5,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(6,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(7,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(8,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(9,24), pad=((0,1),(1,0))),sg.B('*', size=(3, 1), key=(10,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(11,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(12,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(13,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(14,24), pad=((0,1),(1,0))),sg.B('*', size=(3, 1), key=(15,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(16,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(17,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(18,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(19,24), pad=((0,1),(1,0))),sg.B('*', size=(3, 1), key=(20,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(21,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(22,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(23,24), pad=((0,0),(1,0))),sg.B('*', size=(3, 1), key=(24,24), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,23), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,23), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,23), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,23), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,23), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,23), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,23), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,22), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,22), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,22), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,22), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,22), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,22), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,22), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,21), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,21), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,21), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,21), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,21), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,21), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,21), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,20), pad=((1,0),(0,1))),sg.B('*', size=(3, 1), key=(1,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(2,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(3,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(4,20), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(5,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(6,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(7,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(8,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(9,20), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(10,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(11,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(12,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(13,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(14,20), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(15,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(16,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(17,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(18,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(19,20), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(20,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(21,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(22,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(23,20), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(24,20), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,19), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,19), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,19), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,19), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,19), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,19), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,19), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,18), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,18), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,18), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,18), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,18), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,18), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,18), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,17), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,17), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,17), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,17), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,17), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,17), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,17), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,16), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,16), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,16), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,16), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,16), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,16), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,16), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,15), pad=((1,0),(0,1))),sg.B('*', size=(3, 1), key=(1,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(2,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(3,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(4,15), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(5,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(6,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(7,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(8,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(9,15), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(10,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(11,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(12,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(13,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(14,15), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(15,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(16,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(17,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(18,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(19,15), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(20,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(21,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(22,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(23,15), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(24,15), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,14), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,14), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,14), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,14), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,14), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,14), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,14), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,13), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,13), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,13), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,13), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,13), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,13), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,13), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,12), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,12), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,12), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,12), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,12), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,12), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,12), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,11), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,11), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,11), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,11), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,11), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,11), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,11), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,10), pad=((1,0),(0,1))),sg.B('*', size=(3, 1), key=(1,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(2,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(3,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(4,10), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(5,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(6,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(7,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(8,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(9,10), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(10,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(11,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(12,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(13,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(14,10), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(15,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(16,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(17,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(18,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(19,10), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(20,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(21,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(22,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(23,10), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(24,10), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,9), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,9), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,9), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,9), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,9), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,9), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,9), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,8), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,8), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,8), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,8), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,8), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,8), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,8), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,7), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,7), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,7), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,7), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,7), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,7), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,7), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,6), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,6), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,6), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,6), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,6), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,6), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,6), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,5), pad=((1,0),(0,1))),sg.B('*', size=(3, 1), key=(1,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(2,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(3,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(4,5), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(5,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(6,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(7,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(8,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(9,5), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(10,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(11,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(12,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(13,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(14,5), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(15,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(16,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(17,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(18,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(19,5), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(20,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(21,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(22,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(23,5), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(24,5), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,4), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,4), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,4), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,4), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,4), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,4), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,4), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,3), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,3), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,3), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,3), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,3), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,3), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,3), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,2), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,2), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,2), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,2), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,2), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,2), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,2), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,1), pad=((1,0),(0,0))),sg.B('*', size=(3, 1), key=(1,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(2,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(3,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(4,1), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(5,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(6,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(7,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(8,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(9,1), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(10,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(11,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(12,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(13,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(14,1), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(15,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(16,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(17,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(18,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(19,1), pad=((0,1),(0,0))),sg.B('*', size=(3, 1), key=(20,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(21,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(22,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(23,1), pad=((0,0),(0,0))),sg.B('*', size=(3, 1), key=(24,1), pad=((0,1),(0,0)))],
        [sg.B('*', size=(3, 1), key=(0,0), pad=((1,0),(0,1))),sg.B('*', size=(3, 1), key=(1,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(2,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(3,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(4,0), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(5,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(6,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(7,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(8,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(9,0), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(10,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(11,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(12,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(13,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(14,0), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(15,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(16,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(17,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(18,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(19,0), pad=((0,1),(0,1))),sg.B('*', size=(3, 1), key=(20,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(21,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(22,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(23,0), pad=((0,0),(0,1))),sg.B('*', size=(3, 1), key=(24,0), pad=((0,1),(0,1)))],
        [sg.Text('Currently Selected Space: '), sg.Text(' ', key=('-pushed-'), size=(10,1)), sg.Text('Is a grid square? '), sg.Text(' ', key=('-is_grid-'))]
        ]

    layout_options = [
        [sg.Input(size=(5,1), key='-r1_heading-'), sg.Combo(['radians', 'degrees'], size=(10,1), key=('-r1_units_heading-')), sg.Text('Current heading for Robot 1. 0 for directly up', size=(35,1))],
        [sg.Input(size=(5,1), key='-r2_heading-'), sg.Combo(['radians', 'degrees'], size=(10,1), key=('-r2_units_heading-')), sg.Text('Current heading for Robot 2. 0 for directly up', size=(35,1))],
        [sg.Input(size=(5,1), key='-r1_linear_velocity-'), sg.Text('Linear velocity for Robot 1 in meters/second', size=(45,1))],
        [sg.Input(size=(5,1), key='-r2_linear_velocity-'), sg.Text('Linear velocity for Robot 2 in meters/second', size=(45,1))],
        [sg.Input(size=(5,1), key='-r1_angular_velocity-'), sg.Text('Angular velocity for Robot 1 in radians/second', size=(45,1))],
        [sg.Input(size=(5,1), key='-r2_angular_velocity-'), sg.Text('Angular velocity for Robot 2 in radians/second', size=(45,1))],
        [sg.Input(size=(10,1), key='-start_day-'), sg.Text('Weekday for movement: (1-7) or blank for today (1 = Sunday)', size=(40,1))],
        [sg.Input(size=(10,1), key='-start_time-'), sg.Text('Time for movement: HH:MM:SS or blank for T+10 seconds', size=(40,1))],
        [sg.Text('Robot 1 starting location (Select grid location first)', size=(40,1)), sg.Button('Select', size=(10,1), key=('R1_0'), visible=True)],
        [sg.Text('Robot 1 first location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R1_1'), visible=False)],
        [sg.Text('Robot 1 second location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R1_2'), visible=False)],
        [sg.Text('Robot 1 third location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R1_3'), visible=False)],
        [sg.Text('Robot 2 starting location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R2_0'), visible=False)],
        [sg.Text('Robot 2 first location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R2_1'), visible=False)],
        [sg.Text('Robot 2 second location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R2_2'), visible=False)],
        [sg.Text('Robot 2 third location', size=(40,1)), sg.Button('Select', size=(10,1), key=('R2_3'), visible=False)],
        [sg.Text('Selected for Robot 2: '), sg.Text(' ', key=('-r2_location-'))],
        [sg.Button('Submit', size=(10,1)), sg.Button('Clear', size=(10,1)), sg.Button('Exit', size=(10,1)), sg.Button('Debug Fill', size=(10,1))],
        [sg.Text(' ', size=(50,10), key='-debug-')]
        ]

    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 38', size=(125,2))],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', size=(125,1))],
              #[sg.Text('')],
              [sg.Frame('Inputs',[[
                  sg.Column(layout_grid, pad=((50,15),(15,15))),
                  sg.Text(' '),
                  sg.Column(layout_options, pad=(15,15))
                  ]],
                  title_location='TITLE_LOCATION_TOP',
                  pad=((25,25),(25,25)),
              )]
              ]
    window = sg.Window("RobotGUI Main", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    location = []
    id = []
    robot_id = []
    command_id = []
    day_set = []
    time_start = []
    time_end = []
    linear_velocity = []
    angular_velocity = []
    #Main Event Loop
    while True:
        event, values = window.read()

        # Print event to command line
        #print('event: ', event)
        # Check if event is a grid button being pressed
        if re.match('\([0-9]*\,\ *[0-9]*\)', str(event)):
            window['-is_grid-'].update('Yes')
            grid = event
            window['-pushed-'].update(str(grid))
        else:
            window['-is_grid-'].update('No')
        
        # Button Checking
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        elif event == "Clear":
            main()
        elif event == "Debug Fill": # Fills location list with pre-determined grid coordinates as if selecting manually
            location.insert(0, '(2, 2)')
            location.insert(1, '(7, 2)')
            location.insert(2, '(12, 2)')
            location.insert(3, '(12, 7)')
            location.insert(4, '(2, 22)')
            location.insert(5, '(7, 17)')
            location.insert(6, '(12, 12)')
            location.insert(7, '(17, 12)')
            window[2,2].update('S', button_color=('white', 'blue'))
            window[7,2].update('1', button_color=('white', 'blue'))
            window[12,2].update('2', button_color=('white', 'blue'))
            window[12,7].update('3', button_color=('white', 'blue'))
            window[2,22].update('S', button_color=('white', 'red'))
            window[7,17].update('1', button_color=('white', 'red'))
            window[12,12].update('2', button_color=('white', 'red'))
            window[17,12].update('3', button_color=('white', 'red'))
            window['R1_0'].update(visible=False)
            window['-r1_heading-'].update('0')
            window['-r2_heading-'].update('0')

        elif event in ('R1_0', 'R1_1', 'R1_2', 'R1_3', 'R2_0', 'R2_1', 'R2_2', 'R2_3') and 'grid' in locals():
            if event == "R1_0":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('S', button_color=('white', 'blue'))
                window['R1_0'].update(visible=False)
                window['R1_1'].update(visible=True)
            elif event == "R1_1":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('1', button_color=('white', 'blue'))
                window['R1_1'].update(visible=False)
                window['R1_2'].update(visible=True)
            elif event == "R1_2":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('2', button_color=('white', 'blue'))
                window['R1_2'].update(visible=False)
                window['R1_3'].update(visible=True)
            elif event == "R1_3":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('3', button_color=('white', 'blue'))
                window['R1_3'].update(visible=False)
                window['R2_0'].update(visible=True)
            elif event == "R2_0":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('S', button_color=('white', 'red'))
                window['R2_0'].update(visible=False)
                window['R2_1'].update(visible=True)
            elif event == "R2_1":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('1', button_color=('white', 'red'))
                window['R2_1'].update(visible=False)
                window['R2_2'].update(visible=True)
            elif event == "R2_2":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('2', button_color=('white', 'red'))
                window['R2_2'].update(visible=False)
                window['R2_3'].update(visible=True)
            elif event == "R2_3":
                # Make sure the grid selected is not selected by another location
                location.append(grid)
                window[grid].update('3', button_color=('white', 'red'))
                window['R2_3'].update(visible=False)
            
        elif event == "Submit" and len(location) != 8:
            # Making sure the location list is filled else show error
            window['-debug-'].update('Error: Please select all locations before submitting.')
        elif event == "Submit" and len(location) == 8:
            # Input validation for the following inputs:
            # -r1_heading-
            #print('r1_heading: ' + values['-r1_heading-'])
            # -r2_heading-
            #print('r1_heading: ' + values['-r2_heading-'])
            # -r1_linear_velocity-
            #print('r1_linear_velocity: ' + values['-r1_linear_velocity-'])
            # -r2_linear_velocity-
            #print('r2_linear_velocity: ' + values['-r2_linear_velocity-'])
            # -r1_angular_velocity-
            #print('r1_angular_velocity: ' + values['-r1_angular_velocity-'])
            # -r2_angular_velocity-
            #print('r2_angular_velocity: ' + values['-r2_angular_velocity-'])
            # -start_date-
            #print('start_date: ' + values['-start_date-'])
            # -start_time-
            #print('start_time: ' + values['-start_time-'])

            # Grabbing values from input
            #last_command = GET LAST COMMAND IN DB
            last_command = 0

            # Calculate rx_last_angle and convert if necissary
            if values['-r1_units_heading-'] == "degrees":
                r1_last_angle = ( float(values['-r1_heading-']) * ( math.pi / 180 )) #convert degrees to radians
            else:
                r1_last_angle = float(values['-r1_heading-'])
            if values['-r2_units_heading-'] == "degrees":
                r2_last_angle = ( float(values['-r2_heading-']) * ( math.pi / 180 )) #convert degrees to radians
            else:
                r2_last_angle = float(values['-r2_heading-'])

            # Calculate weekday if non given
            if values['-start_day-']:
                start_day = values['-start_day-']
            else:
                start_day = datetime.today().weekday() # 0 (Monday) through 6 (Sunday)
                # The following translates weeday from 0-6 (Monday-Sunday) to 1-7 (Sunday-Saturday)
                start_day += 2
                if start_day == 8:
                    start_day = 1

            # Calculate time if none given
            if values['-start_time-']:
                start_time = values['-start_time-']
            else:
                time = datetime.now() + timedelta(seconds=10)
                r1_time = time
                r2_time = time
            x = 0

            # first robot. runs 6 times, 3 for turns and 3 for movements: 0,1,2,3,4,5
            while x < ( len(location) - 2 ):
                last_command += 1
                # id
                id.insert(x, last_command)
                
                # robot_id
                robot_id.insert(x, 'r1d1')
                x += 1

                # day_set
                day_set.insert(x, str(start_day))

                #Calculate duration of rotation/movement. This will allow us to find time_end
                if (x % 2) == 0: #even = rotation movement
                    #calculate new_angle given coordinates
                    coordinate0 = location[int(((x+2)/2)-1)] #translates coordinates in location[] array with position in current array
                    coordinate1 = location[int(coordinate0+1)]
                    opp = ( coordinate0[1] - coordinate1[1] )
                    print('opp: ', opp)
                    adj = ( coordinate0[0] - coordinate1[0] )
                    print('adj: ', adj)
                    new_angle = math.atan(opp/adj)
                    print('new_angle: ', new_angle)
                    #calculate turn_angle given last_angle and new_angle
                else: #odd = forward movement
                    command_id.insert(x, 'C01')
                

                # time_start
                time_start.insert(x, str(r1_time.strftime("%H:%M:%S")))
                minutes_to_add = 0
                seconds_to_add = 30
                r1_time += timedelta(minutes = minutes_to_add, seconds = seconds_to_add)
                # time_end
                time_end.insert(x, str(r1_time.strftime("%H:%M:%S")))
            
            # second robot. runs 6 times, 3 for turns and 3 for movements: 6,7,8,9,10,11
            while x < (( len(location) - 2 ) * 2 ):
                last_command += 1
                # id
                id.insert(x, last_command)
                
                # robot_id
                robot_id.insert(x, 'r2d2')
                x += 1

                # day_set
                day_set.insert(x, str(start_day))

                #calculate duration of rotation/movement. This will allow us to find time_end

                # time_start
                time_start.insert(x, str(r2_time.strftime("%H:%M:%S")))
                minutes_to_add = 0
                seconds_to_add = 30
                r2_time += timedelta(minutes = minutes_to_add, seconds = seconds_to_add)
                # time_end
                time_end.insert(x, str(r2_time.strftime("%H:%M:%S")))

            # Debug calculated values
            y = 0
            while  y < (( len(location) - 2 ) * 2 ):
                #print('\nPrinting position in lists: ', y)
                #print('id:', id[y])
                #print('robot_id:', robot_id[y])
                #print('command_id:' + str(command_id[y]))
                #print('day_set:', day_set[y])
                #print('time_start:', time_start[y])
                #print('time_end:', time_end[y])
                #print('linear_velocity:' + str(linear_velocity[y]))
                #print('angular_velocity' + str(angular_velocity[y]))
                y += 1

            # Print debug text or SQL command
            window['-debug-'].update('Debug output goes here.')

            #Send commands to MySQL
        
    window.close()

def main():
    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 38', size=(125,2))],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', size=(125,1))],
              [sg.Button("Start Program", size=(35,4), pad=((150,150),(15,15)), key="open")]]
    window = sg.Window("RobotGUI", layout, web_debug=False, web_ip='0.0.0.0', web_port=8080)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED or event is None:
            break
        if event == "open":
            open_window()
            window.close()
        
    window.close()
if __name__ == "__main__":
    main()
