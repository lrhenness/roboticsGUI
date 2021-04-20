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
        [sg.Input(size=(10,1), focus=True, default_text='0', key='-r1_heading-'), sg.Combo(['radians', 'degrees'], size=(8,1), key=('-r1_units_heading-')), sg.Text('Current heading for Robot 1. 90 for directly up', size=(35,1))],
        [sg.Input(size=(10,1), default_text='0', key='-r2_heading-'), sg.Combo(['radians', 'degrees'], size=(8,1), key=('-r2_units_heading-')), sg.Text('Current heading for Robot 2. 90 for directly up', size=(35,1))],
        [sg.Input(size=(10,1), default_text='1', key='-r1_linear_velocity-'), sg.Text('Linear velocity for Robot 1 in meters/second', size=(45,1))],
        [sg.Input(size=(10,1), default_text='1', key='-r2_linear_velocity-'), sg.Text('Linear velocity for Robot 2 in meters/second', size=(45,1))],
        [sg.Input(size=(10,1), default_text='10', key='-r1_angular_velocity-'), sg.Combo(['radians', 'degrees'], size=(8,1), key=('-r1_units_angular-')), sg.Text('Angular velocity for Robot 1 (per second)', size=(35,1))],
        [sg.Input(size=(10,1), default_text='10', key='-r2_angular_velocity-'), sg.Combo(['radians', 'degrees'], size=(8,1), key=('-r2_units_angular-')), sg.Text('Angular velocity for Robot 2 (per second)', size=(35,1))],
        [sg.Input(size=(10,1), key='-start_day-'), sg.Text('Weekday for movement: (1-7) or blank for today (1 = Sunday)', size=(45,1))],
        [sg.Input(size=(10,1), key='-start_time-'), sg.Text('Time for movement: HH:MM:SS or blank for T+10 seconds', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R1_0')), sg.Text('Robot 1 starting location (Select grid location first)', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R1_1')), sg.Text('Robot 1 first location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R1_2')), sg.Text('Robot 1 second location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R1_3')), sg.Text('Robot 1 third location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R2_0')), sg.Text('Robot 2 starting location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R2_1')), sg.Text('Robot 2 first location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R2_2')), sg.Text('Robot 2 second location', size=(40,1))],
        [sg.Button('Select', size=(10,1), key=('R2_3')), sg.Text('Robot 2 third location', size=(40,1))],
        [sg.Text(' ')],
        [sg.Button('Submit', size=(10,1)), sg.Button('Clear', size=(10,1)), sg.Button('Exit', size=(10,1)), sg.Button('Debug Fill', size=(10,1))],
        [sg.Text(' ', size=(50,10), key='-debug-')]
        ]

    layout = [[sg.Text("Robotics GUI Capstone Project", justification="center", font='Any 38', size=(125,2))],
              [sg.Text('Made by Luken Henness', justification="center", font='Any 16', size=(125,1))],
              #[sg.Text('')],
              [sg.Frame('Inputs',[[
                  sg.Column(layout_grid, pad=((65,15),(15,15))),
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
            location.insert(0, (2, 2))
            location.insert(1, (7, 7))
            location.insert(2, (12, 2))
            location.insert(3, (12, 7))
            location.insert(4, (2, 22))
            location.insert(5, (7, 17))
            location.insert(6, (12, 12))
            location.insert(7, (17, 12))
            window[2,2].update('S', button_color=('white', 'blue'))
            window[7,7].update('1', button_color=('white', 'blue'))
            window[12,2].update('2', button_color=('white', 'blue'))
            window[12,7].update('3', button_color=('white', 'blue'))
            window[2,22].update('S', button_color=('white', 'red'))
            window[7,17].update('1', button_color=('white', 'red'))
            window[12,12].update('2', button_color=('white', 'red'))
            window[17,12].update('3', button_color=('white', 'red'))
            window['R1_0'].update(button_color=('white', 'green'))
            window['-r1_heading-'].update('0')
            window['-r2_heading-'].update('0')
            window['-r1_linear_velocity-'].update('1')
            window['-r2_linear_velocity-'].update('1')
            window['-r1_angular_velocity-'].update('0.1745329252')
            window['-r2_angular_velocity-'].update('0.1745329252')

        elif event in ('R1_0', 'R1_1', 'R1_2', 'R1_3', 'R2_0', 'R2_1', 'R2_2', 'R2_3') and 'grid' in locals():
            if event == "R1_0" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[0]
                except IndexError:
                    location.insert(0, grid)
                else:
                    window[location[0]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[0] = grid
                    window[grid].update('S', button_color=('white', 'blue'))
                    window['R1_0'].update(button_color=('white', 'green'))
            elif event == "R1_1" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[1]
                except IndexError:
                    location.insert(1, grid)
                else:
                    window[location[1]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[1] = grid
                    window[grid].update('1', button_color=('white', 'blue'))
                    window['R1_1'].update(button_color=('white', 'green'))
            elif event == "R1_2" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[2]
                except IndexError:
                    location.insert(2, grid)
                else:
                    window[location[2]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[2] = grid
                    window[grid].update('2', button_color=('white', 'blue'))
                    window['R1_2'].update(button_color=('white', 'green'))
            elif event == "R1_3" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[3]
                except IndexError:
                    location.insert(3, grid)
                else:
                    window[location[3]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[3] = grid
                    window[grid].update('3', button_color=('white', 'blue'))
                    window['R1_3'].update(button_color=('white', 'green'))
            elif event == "R2_0" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[4]
                except IndexError:
                    location.insert(4, grid)
                else:
                    window[location[4]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[4] = grid
                    window[grid].update('S', button_color=('white', 'red'))
                    window['R2_0'].update(button_color=('white', 'green'))
            elif event == "R2_1" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[5]
                except IndexError:
                    location.insert(5, grid)
                else:
                    window[location[5]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[5] = grid
                    window[grid].update('1', button_color=('white', 'red'))
                    window['R2_1'].update(button_color=('white', 'green'))
            elif event == "R2_2" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[6]
                except IndexError:
                    location.insert(6, grid)
                else:
                    window[location[6]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[6] = grid
                    window[grid].update('2', button_color=('white', 'red'))
                    window['R2_2'].update(button_color=('white', 'green'))
            elif event == "R2_3" and grid not in location: # Make sure the grid selected is not selected by another location
                try:
                    location[7]
                except IndexError:
                    location.insert(7, grid)
                else:
                    window[location[7]].update('*', button_color=(sg.theme_button_color()))
                finally:
                    location[7] = grid
                    window[grid].update('3', button_color=('white', 'red'))
                    window['R2_3'].update(button_color=('white', 'green'))
            
        elif event == "Submit":
            # Input validation time!!!
            if len(location) != 8:
                window['-debug-'].update('Error: Please select all locations before submitting.')
                continue

            # -r1_heading-
            if values['-r1_heading-']:
                if values['-r1_units_heading-'] == "degrees":
                    try:
                        if int(values['-r1_heading-']) >= 0 and int(values['-r1_heading-']) < 360:
                            r1_last_angle = ( float(values['-r1_heading-']) * ( math.pi / 180 )) #convert degrees to radians
                        else:
                            window['-debug-'].update('Degrees Error: Please enter a valid heading for robot 1 between 0 and 360.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Integer Error: Please enter a valid integer heading for robot 1 between 0 and 360.')
                        continue
                else:
                    try:
                        if float(values['-r1_heading-']) >= 0 and float(values['-r1_heading-']) < 6.2831853072:
                            r1_last_angle = float(values['-r1_heading-'])
                        else:
                            window['-debug-'].update('Radians Error: Please enter a valid heading for robot 1 between 0 and 6.2831853072')
                            continue
                    except ValueError:
                        window['-debug-'].update('Float Error: Please enter a valid float heading for robot 1 between 0 and 6.2831853072')
                        continue
            else:
                window['-debug-'].update('Error: Please enter an heading for robot 1.')
                continue

            # -r2_heading-
            if values['-r2_heading-']:
                if values['-r2_units_heading-'] == "degrees":
                    try:
                        if int(values['-r2_heading-']) >= 0 and int(values['-r2_heading-']) < 360:
                            r2_last_angle = ( float(values['-r2_heading-']) * ( math.pi / 180 )) #convert degrees to radians
                        else:
                            window['-debug-'].update('Degrees Error: Please enter a valid heading for robot 2 between 0 and 360.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Integer Error: Please enter a valid integer heading for robot 2 between 0 and 360.')
                        continue
                else:
                    try:
                        if float(values['-r2_heading-']) >= 0 and float(values['-r2_heading-']) < 6.2831853072:
                            r2_last_angle = float(values['-r2_heading-'])
                        else:
                            window['-debug-'].update('Radians Error: Please enter a valid heading for robot 2 between 0 and 6.2831853072')
                            continue
                    except ValueError:
                        window['-debug-'].update('Float Error: Please enter a valid float heading for robot 2 between 0 and 6.2831853072')
                        continue
            else:
                window['-debug-'].update('Error: Please enter an heading for robot 2.')
                continue

            # -r1_linear_velocity-
            if values['-r1_linear_velocity-']:
                try:
                    if float(values['-r1_linear_velocity-']) > 0: # UPDATE WITH BETTER VALIDATION
                        r1_linear_velocity = float(values['-r1_linear_velocity-'])
                    else:
                        window['-debug-'].update('Error: Please enter a valid linear velocity for robot 1.')
                        continue
                except ValueError:
                    window['-debug-'].update('Float Error: Please enter a valid floating point number linear velocity for robot 1.')
                    continue
            else:
                window['-debug-'].update('Error: Please enter a linear velocity for robot 1.')
                continue

            # -r2_linear_velocity-
            if values['-r2_linear_velocity-']:
                try:
                    if float(values['-r2_linear_velocity-']) > 0: # UPDATE WITH BETTER VALIDATION
                        r2_linear_velocity = float(values['-r2_linear_velocity-'])
                    else:
                        window['-debug-'].update('Error: Please enter a valid linear velocity for robot 2.')
                        continue
                except ValueError:
                    window['-debug-'].update('Float Error: Please enter a valid floating point number linear velocity for robot 2.')
                    continue
            else:
                window['-debug-'].update('Error: Please enter a linear velocity for robot 2.')
                continue

            # -r1_angular_velocity-
            if values['-r1_angular_velocity-']:
                if values['-r1_units_angular-'] == "degrees":
                    try:
                        if int(values['-r1_angular_velocity-']) > 0 and int(values['-r1_angular_velocity-']) < 360:
                            r1_angular_velocity = ( float(values['-r1_angular_velocity-']) * ( math.pi / 180 )) #convert degrees to radians
                        else:
                            window['-debug-'].update('Degrees Error: Please enter a valid angular velocity for robot 1 between 0 and 360 degrees per second.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Integer Error: Please enter a valid integer angular velocity for robot 1 between 0 and 360 degrees per second.')
                        continue
                else:
                    try:
                        if float(values['-r1_angular_velocity-']) > 0: # UPDATE WITH BETTER VALIDATION
                            r1_angular_velocity = float(values['-r1_angular_velocity-'])
                        else:
                            window['-debug-'].update('Radians Error: Please enter a valid angular velocity for robot 1 between 0 and ??? radians per second.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Float Error: Please enter a valid floating point angular velocity for robot 1 between 0 and ??? radians per second.')
                        continue
            else:
                window['-debug-'].update('Error: Please enter an angular velocity for robot 1.')
                continue

            # -r2_angular_velocity-
            if values['-r2_angular_velocity-']:
                if values['-r2_units_angular-'] == "degrees":
                    try:
                        if int(values['-r2_angular_velocity-']) > 0 and int(values['-r2_angular_velocity-']) < 360:
                            r2_angular_velocity = ( float(values['-r2_angular_velocity-']) * ( math.pi / 180 )) #convert degrees to radians
                        else:
                            window['-debug-'].update('Degrees Error: Please enter a valid angular velocity for robot 2 between 0 and 360 degrees per second.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Integer Error: Please enter a valid integer angular velocity for robot 2 between 0 and 360 degrees per second.')
                        continue
                else:
                    try:
                        if float(values['-r2_angular_velocity-']) > 0: # UPDATE WITH BETTER VALIDATION
                            r2_angular_velocity = float(values['-r2_angular_velocity-'])
                        else:
                            window['-debug-'].update('Radians Error: Please enter a valid angular velocity for robot 2 between 0 and ??? radians per second.')
                            continue
                    except ValueError:
                        window['-debug-'].update('Float Error: Please enter a valid floating point angular velocity for robot 2 between 0 and ??? radians per second.')
                        continue
            else:
                window['-debug-'].update('Error: Please enter an angular velocity for robot 2.')
                continue

            # -start_day-
            if values['-start_day-']:
                if int(values['-start_day-']) >= 1 and int(values['-start_day-']) <= 7: # UPDATE WITH BETTER VALIDATION
                    start_day = values['-start_day-']
                else:
                    window['-debug-'].update('Error: Please enter a valid start day between 1 and 7.')
                    continue
            else:
                start_day = datetime.today().weekday() # 0 (Monday) through 6 (Sunday)
                # The following translates weeday from 0-6 (Monday-Sunday) to 1-7 (Sunday-Saturday)
                start_day += 1
                if start_day == 7:
                    start_day = 0

            # -start_time-
            if values['-start_time-']:
                try: 
                    r1_time, r2_time = datetime.strptime(values['-start_time-'], '%H:%M:%S').time()
                except ValueError:
                    window['-debug-'].update('Error: Please enter a valid start time in the format HH:MM:SS (24-hour time) or leave blank')
                    continue
            else:
                r1_time, r2_time = datetime.now() + timedelta(seconds=10)

            #last_command = GET LAST COMMAND IN DB
            last_command = 0
            x = 0
            # first robot. runs 6 times, 3 for turns and 3 for movements: 0,1,2,3,4,5
            while x < ( len(location) - 2 ):
                last_command += 1
                # id
                id.insert(x, last_command)
                
                # robot_id
                robot_id.insert(x, 'r1d1')

                # day_set
                day_set.insert(x, str(start_day))

                #Calculate duration of rotation/movement. This will allow us to find time_end
                if (x % 2) == 0: #even = rotation movement
                    #calculate new_angle given coordinates
                    l = int(((x+2)/2)-1) #translates coordinates in location[] array with position in current array
                    coordinate0 = location[l]
                    coordinate1 = location[(l+1)]
                    #finding opposite and adjacent sides of the triange to calculate angle of turn
                    opp = ( coordinate1[1] - coordinate0[1] )
                    adj = ( coordinate1[0] - coordinate0[0] )
                    print('Turn. \topposite:', opp, '\tadjacent:', adj)
                    if opp == 0 and adj >= 0:
                        new_angle = 0 #0 degrees (right)
                    elif opp == 0 and adj < 0:
                        new_angle = 3.1415926536 #180 degrees (left)
                    elif adj == 0 and opp >= 0:
                        new_angle = 1.5707963268 #90 degrees (up)
                    elif adj == 0 and opp < 0:
                        new_angle = 4.7123889804 #270 degrees (down)
                    else:
                        if opp < 1 and adj < 1:
                            new_angle = (math.atan(opp/adj) + 3.1415926536) #to account for horseplay in the way degrees/radians relate to grid locations
                        elif opp < 1 and adj > 1:
                            new_angle = (math.atan(opp/adj) + 6.2831853072)
                        elif opp > 1 and adj < 1:
                            new_angle = (math.atan(opp/adj) + 3.1415926536)
                        else:
                            new_angle = math.atan(opp/adj)
                    #calculate turn_angle given last_angle and new_angle
                    turn_angle = float(new_angle) - float(r1_last_angle)
                    if turn_angle < -3.1415926536:
                        turn_angle += 6.2831853072
                        #left turn
                        command_id.insert(x, 'C03')
                    elif turn_angle > 3.1415926536:
                        turn_angle = abs(turn_angle - 6.2831853072)
                        #right turn
                        command_id.insert(x, 'C04')
                    elif turn_angle < 0 and turn_angle > -3.1415926536:
                        turn_angle = abs(turn_angle)
                        #right turn
                        command_id.insert(x, 'C04')
                    elif turn_angle > 0 and turn_angle < 3.1415926536:
                        #left turn
                        command_id.insert(x, 'C03')
                    else: #turn_angle should be exactly 180 degrees
                        #turn right 180 degrees
                        command_id.insert(x, 'C04')
                    #calculate duration given turn_angle and r1_angular_velocity
                    duration = (float(turn_angle) / float(r1_angular_velocity))
                    #change angular_velocity to positive or negative depending on the direction of turn needed
                    #and add result to the list
                    if command_id[x] == 'C03':
                        #left turn, make angular velocity negative
                        angular_velocity.insert(x, (0 - r1_angular_velocity))
                    elif command_id[x] == 'C04':
                        #right turn, keep angular velocity positive
                        angular_velocity.insert(x, r1_angular_velocity)
                    linear_velocity.insert(x, '0')

                    #set last_angle for next iteration
                    r1_last_angle = new_angle
                    
                else: #odd = forward movement
                    command_id.insert(x, 'C01') 
                    angular_velocity.insert(x, '0')
                    linear_velocity.insert(x, r1_linear_velocity)
                    #calculate distance given pythagorean theorem
                    l = int(((x+1)/2)-1) #translates coordinates in location[] array with position in current array
                    coordinate0 = location[l]
                    coordinate1 = location[(l+1)]
                    #finding opposite and adjacent sides of the triange to calculate distance
                    opp = abs( coordinate1[1] - coordinate0[1] )
                    adj = abs( coordinate1[0] - coordinate0[0] )
                    print('Move. \topposite:', opp, '\tadjacent:', adj)
                    #pythagorean theorem to find missing side's length using math.hypot
                    if opp == 0 and adj > 1:
                        hyp = adj
                    elif adj == 0 and opp > 1:
                        hyp = opp
                    else:
                        hyp = math.hypot(opp,adj)
                    #calculate duration given distance and linear_velocity
                    duration = (float(hyp) / float(r1_linear_velocity))

                # time_start
                time_start.insert(x, str(r1_time.strftime("%H:%M:%S.%f")))
                # time_end
                print('duration for r1 itteration ', x, ' is:', duration)
                r1_time += timedelta(seconds = duration)
                time_end.insert(x, str(r1_time.strftime("%H:%M:%S.%f")))
            
                x += 1

            # second robot. runs 6 times, 3 for turns and 3 for movements: 6,7,8,9,10,11
            while x < (( len(location) - 2 ) * 2 ):
                last_command += 1
                # id
                id.insert(x, last_command)
                
                # robot_id
                robot_id.insert(x, 'r2d2')

                # day_set
                day_set.insert(x, str(start_day))

                #Calculate duration of rotation/movement. This will allow us to find time_end
                if (x % 2) == 0: #even = rotation movement
                    #calculate new_angle given coordinates
                    l = int((x+2)/2) #translates coordinates in location[] array with position in current array
                    coordinate0 = location[l]
                    coordinate1 = location[(l+1)]
                    #finding opposite and adjacent sides of the triange to calculate angle of turn
                    opp = ( coordinate1[1] - coordinate0[1] )
                    adj = ( coordinate1[0] - coordinate0[0] )
                    print('Turn. \topposite:', opp, '\tadjacent:', adj)
                    if opp == 0 and adj >= 0:
                        new_angle = 0 #0 degrees (right)
                    elif opp == 0 and adj < 0:
                        new_angle = 3.1415926536 #180 degrees (left)
                    elif adj == 0 and opp >= 0:
                        new_angle = 1.5707963268 #90 degrees (up)
                    elif adj == 0 and opp < 0:
                        new_angle = 4.7123889804 #270 degrees (down)
                    else:
                        if opp < 1 and adj < 1:
                            new_angle = (math.atan(opp/adj) + 3.1415926536) #to account for horseplay in the way degrees/radians relate to grid locations
                        elif opp < 1 and adj > 1:
                            new_angle = (math.atan(opp/adj) + 6.2831853072)
                        elif opp > 1 and adj < 1:
                            new_angle = (math.atan(opp/adj) + 3.1415926536)
                        else:
                            new_angle = math.atan(opp/adj)
                    #calculate turn_angle given last_angle and new_angle
                    turn_angle = float(new_angle) - float(r2_last_angle)
                    if turn_angle < -3.1415926536:
                        turn_angle += 6.2831853072
                        #left turn
                        command_id.insert(x, 'C03')
                    elif turn_angle > 3.1415926536:
                        turn_angle = abs(turn_angle - 6.2831853072)
                        #right turn
                        command_id.insert(x, 'C04')
                    elif turn_angle < 0 and turn_angle > -3.1415926536:
                        turn_angle = abs(turn_angle)
                        #right turn
                        command_id.insert(x, 'C04')
                    elif turn_angle > 0 and turn_angle < 3.1415926536:
                        #left turn
                        command_id.insert(x, 'C03')
                    else: #turn_angle should be exactly 180 degrees
                        #turn right 180 degrees
                        command_id.insert(x, 'C04')
                    #calculate duration given turn_angle and r2_angular_velocity
                    duration = (float(turn_angle) / float(r2_angular_velocity))
                    #change angular_velocity to positive or negative depending on the direction of turn needed
                    #and add result to the list
                    if command_id[x] == 'C03':
                        #left turn, make angular velocity negative
                        angular_velocity.insert(x, (0 - r2_angular_velocity))
                    elif command_id[x] == 'C04':
                        #right turn, keep angular velocity positive
                        angular_velocity.insert(x, r2_angular_velocity)
                    linear_velocity.insert(x, '0')

                    #set last_angle for next iteration
                    r2_last_angle = new_angle
                    
                else: #odd = forward movement
                    command_id.insert(x, 'C01') 
                    angular_velocity.insert(x, '0')
                    linear_velocity.insert(x, r2_linear_velocity)
                    #calculate distance given pythagorean theorem
                    l = int((x+1)/2) #translates coordinates in location[] array with position in current array
                    coordinate0 = location[l]
                    coordinate1 = location[(l+1)]
                    #finding opposite and adjacent sides of the triange to calculate distance
                    opp = abs( coordinate1[1] - coordinate0[1] )
                    adj = abs( coordinate1[0] - coordinate0[0] )
                    print('Move. \topposite:', opp, '\tadjacent:', adj)
                    #pythagorean theorem to find missing side's length using math.hypot
                    if opp == 0 and adj > 1:
                        hyp = adj
                    elif adj == 0 and opp > 1:
                        hyp = opp
                    else:
                        hyp = math.hypot(opp,adj)
                    #calculate duration given distance and linear_velocity
                    duration = (float(hyp) / float(r2_linear_velocity))

                # time_start
                time_start.insert(x, str(r2_time.strftime("%H:%M:%S.%f")))
                # time_end
                print('duration for r2 itteration ', x, ' is:', duration)
                r2_time += timedelta(seconds = duration)
                time_end.insert(x, str(r2_time.strftime("%H:%M:%S.%f")))

                x += 1

            # Debug calculated values that will be sent to database
            y = 0
            while  y < (( len(location) - 2 ) * 2 ):
                print('\nPrinting position in lists: ', y)
                print('id:', id[y])
                print('robot_id:', robot_id[y])
                print('command_id:', command_id[y])
                print('angular_velocity:', angular_velocity[y])
                print('linear_velocity:', linear_velocity[y])
                print('day_set:', day_set[y])
                print('time_start:', time_start[y])
                print('time_end:', time_end[y])
                y += 1

            # Print debug text or SQL command
            window['-debug-'].update('Sending to database...')

            #Format commands to send
            """ z = 0
            while  z < (( len(location) - 2 ) * 2 ):
                if time_start[z] == time_end[z]:
                    id.pop(z)
                    robot_id.pop(z)
                    command_id.pop(z)
                    day_set.pop(z)
                    time_start.pop(z)
                    time_end.pop(z)
                    linear_velocity.pop(z)
                    angular_velocity.pop(z)
                z += 1
                #Round time_start and time_end to milliseconds """

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
