import pygame
import time
import copy
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# from backtrack import Grid, Cube
from helpers import (
    find_empty,
    valid,
    update_time,
)


def backtrack_gui(bo, start, fast=False):
    # updating model - gui
    bo.update_model()

    # finding empty values
    find = find_empty(bo.model)

    # base case of recursion
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo.model, i, (row, col)):
            bo.model[row][col] = i
            bo.cubes[row][col].set(i)

            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, colour=(0, 255, 0))
            pygame.display.update()
            if not fast:
                pygame.time.delay(100)

            # recursion
            if backtrack_gui(bo, start, fast):
                return True

            bo.model[row][col] = 0
            bo.cubes[row][col].set(0)

            # gui
            update_time(bo.win, time=round(time.time() - start))
            bo.cubes[row][col].draw_change(bo.win, colour=(255, 0, 0))
            pygame.display.update()
            if not fast:
                pygame.time.delay(100)

    return False
