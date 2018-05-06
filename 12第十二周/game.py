#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/2/15

from tkinter import *
import random


class block:

    def __init__(self, matrix):
        self.matrix = matrix
        self.wait_time = 500
        self.msg = []

        self.block_type = random.randrange(1, 8)
        if self.block_type == 1:
            self.array = [[4, -1], [5, -1], [6, -1], [5, -2]]
        elif self.block_type == 2:
            self.array = [[4, -1], [4, -2], [4, -3], [4, -4]]
        elif self.block_type == 3:
            self.array = [[4, -2], [5, -2], [5, -1], [6, -1]]
        elif self.block_type == 4:
            self.array = [[6, -2], [5, -2], [5, -1], [4, -1]]
        elif self.block_type == 5:
            self.array = [[4, -1], [5, -1], [4, -2], [5, -2]]  # Square
        elif self.block_type == 6:
            self.array = [[4, -1], [5, -1], [5, -2], [5, -3]]
        elif self.block_type == 7:
            self.array = [[5, -1], [4, -1], [4, -2], [4, -3]]

    def run(self):
        reach_buttom = False
        while (reach_buttom == False):
            reach_buttom = (self.down() == False)
            while len(self.msg) > 0:
                instruction = self.msg[0]
                del self.msg[0]

                if instruction == 1:
                    self.run_rotate()
                elif instruction == 2:
                    self.run_left()
                elif instruction == 3:
                    self.run_right()

            self.matrix.canvas.after(self.wait_time)
        else:
            while len(self.msg) > 0:
                del self.msg[0]
            self.matrix.refresh_map()

        if self.matrix.reach_top() == True:
            return False
        else:
            return True

    def chang_time(self):
        self.wait_time = 50

    def rotate(self):
        self.msg.append(1)

    def left(self):
        self.msg.append(2)

    def right(self):
        self.msg.append(3)

    def check_map(self, next_array):
        for i in range(0, 4):
            if False == self.matrix.ckeck_map(next_array[i][0], next_array[i][1]):
                return False
        else:
            return True

    def clear_block(self):
        for i in range(0, 4):
            self.matrix.clear_unit(self.array[i][0], self.array[i][1])

    def draw_block(self):
        for i in range(0, 4):
            self.matrix.draw_unit(self.array[i][0], self.array[i][1])

    def run_left(self):
        next_array = [[0, 0], [0, 0], [0, 0], [0, 0]]

        for i in range(0, 4):
            next_array[i][0] = self.array[i][0] - 1
            next_array[i][1] = self.array[i][1]

        if self.check_map(next_array):
            self.clear_block()
            for i in range(0, 4):
                self.array[i][0] = next_array[i][0]
                self.array[i][1] = next_array[i][1]
            self.draw_block()

    def run_right(self):
        next_array = [[0, 0], [0, 0], [0, 0], [0, 0]]

        for i in range(0, 4):
            next_array[i][0] = self.array[i][0] + 1
            next_array[i][1] = self.array[i][1]

        if self.check_map(next_array):
            self.clear_block()
            for i in range(0, 4):
                self.array[i][0] = next_array[i][0]
                self.array[i][1] = next_array[i][1]
            self.draw_block()

    def run_rotate(self):
        if self.block_type == 5:  # Square, do not rotate
            return

        next_array = [[0, 0], [0, 0], [0, 0], [0, 0]]

        for i in range(0, 4):
            next_array[i][0] = self.array[1][0] + (self.array[1][1] - self.array[i][1])
            next_array[i][1] = self.array[1][1] - (self.array[1][0] - self.array[i][0])

        if self.check_map(next_array):
            self.clear_block()
            for i in range(0, 4):
                self.array[i][0] = next_array[i][0]
                self.array[i][1] = next_array[i][1]
            self.draw_block()

    def down(self):

        next_array = [[0, 0], [0, 0], [0, 0], [0, 0]]

        for i in range(0, 4):
            next_array[i][0] = self.array[i][0]
            next_array[i][1] = self.array[i][1] + 1

        if self.check_map(next_array):
            self.clear_block()
            for i in range(0, 4):
                self.array[i][0] = self.array[i][0]
                self.array[i][1] = self.array[i][1] + 1
            self.draw_block()
            return True
        else:
            for i in range(0, 4):
                self.matrix.map[self.array[i][0]][self.array[i][1]] = True
            return False


class matrix:

    def __init__(self, width, height, element_size, line_size):
        self.width = width
        self.height = height
        self.element_size = element_size  # the size(in pixel) of the square, which is the minimum unit to greate a block.
        self.map = [[0 for i in range(height)] for i in range(
            width)]  # The 2-D array which records the which position of the playground is filled, which is not.

        window_width_pixel = element_size * width
        window_height_pixel = element_size * height

        self.tk = Tk(className='Tetris')

        self.canvas = Canvas(self.tk, width=window_width_pixel, height=window_height_pixel, bg='white')
        self.canvas.bind('<Any-KeyPress>', self.event_callback)
        self.canvas.pack()

        self.canvas.focus_set()

        while True:
            self.replay_game()

    def draw_unit(self, x, y):
        if x >= 0 and y >= 0:
            top = self.element_size * y
            left = self.element_size * x
            self.canvas.create_rectangle(left + 1, top + 1, self.element_size + left - 1, self.element_size + top - 1,
                                         outline='grey', fill='grey')
            self.canvas.update()

    def clear_unit(self, x, y):
        if x >= 0 and y >= 0:
            top = self.element_size * y
            left = self.element_size * x
            self.canvas.create_rectangle(left + 1, top + 1, self.element_size + left - 1, self.element_size + top - 1,
                                         outline='white', fill='white')
            self.canvas.update()

    def replay_game(self):
        for x in range(self.width):
            for y in range(self.height):
                self.map[x][y] = False

        self.game_over = False
        self.canvas.delete("all")

        while False == self.game_over:
            self.block = block(self)
            if self.block.run() == False:
                self.game_over = True
        else:
            print("Game Over")

    def re_draw(self):
        y = self.height - 1
        while y >= 0:

            empty_line_num = 0
            line_empty = True
            for x in range(0, self.width):
                if self.map[x][y]:
                    line_empty = False
                    self.draw_unit(x, y)
                else:
                    self.clear_unit(x, y)
            if line_empty:
                empty_line_num = empty_line_num + 1
                if empty_line_num == 5:
                    break
            y = y - 1

    def remove_line(self, line_num):

        for x in range(0, self.width):
            self.clear_unit(x, line_num)

        while line_num > 0:
            for i in range(0, self.width):
                self.map[i][line_num] = self.map[i][line_num - 1]
            line_num = line_num - 1

    def refresh_map(self):
        need_re_draw = False
        line = self.height - 1
        while line >= 0:
            line_full = True
            for i in range(0, self.width):
                if self.map[i][line] == False:
                    line_full = False
                    break
            if line_full:
                need_re_draw = True
                self.remove_line(line)
            else:
                line = line - 1

        if need_re_draw:
            self.re_draw()

    def reach_top(self):
        top_reached = False
        for i in range(0, self.width):
            if self.map[i][0] == True:
                top_reached = True
                break
        return top_reached

    def ckeck_map(self, x, y):

        return_val = True

        if y < 0:
            return_val = True
        elif x < 0 or x >= self.width or y >= self.height:
            return_val = False
        else:
            return_val = self.map[x][y] == False

        return return_val

    def event_callback(self, event):
        if event.keycode == 37:
            self.block.left()
        elif event.keycode == 39:
            self.block.right()
        elif event.keycode == 32:
            self.block.rotate()
        elif event.keycode == 40:
            self.block.chang_time()


matrix(10, 20, 30, 2)


