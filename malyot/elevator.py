from seting import *
from bilding import *
import pygame
import time

class Elevator:
    def __init__(self, num, num_of_floors, screen_height, elevator_image, ding_sound):
        self.num = num #מספר המעלית
        self.num_of_floors = num_of_floors#מספר הקומות
        self.screen_height = screen_height#גודל המסך
        self.elevator_image = elevator_image#תמונה של המעלית
        self.ding_sound = ding_sound#צליל עצירה 
        self.on_floor = 0#הקומה שהמעלית מאותחלת
        self.target = []#None    קומת היעד 
        self.current_target = None
        self.time_to_finish = 0
        self.whatch = None
        self.state = 'free'  # Possible states: 'free', 'goingUp', 'goingDown', 'open', 'waiting'מצב המעלית
        self.y = self.floor_to_y(self.on_floor)
        self.stop_time = 2  # זמן עצירה בקומה
        self.timer_text = None
        self.new_target = None
        self.sum_of_elvator = 0
        self.sum_time = 0

    def floor_to_y(self, floor):# על המסך Y המרה של מספר קומה לערך 
        floor_height = self.screen_height // self.num_of_floors
        return self.screen_height - (floor + 1) * floor_height

    def move(self):
        if self.state == 'free' and self.target:
            self.current_target = self.target.pop(0)
            target_y = self.floor_to_y(self.current_target)
            if self.y > target_y:
                self.state = 'goingDown'
            elif self.y < target_y:
                self.state = 'goingUp'
            else:
                self.state = 'open'
                self.on_floor = self.current_target
                self.current_target = None
                self.ding_sound.play()
                self.stop_timer = time.time()

        elif self.state in ['goingDown', 'goingUp']:#בדיקה אם המעלית בתנועה לכייון יעד
            target_y = self.floor_to_y(self.current_target)
            if self.y > target_y:
                self.y -= 1
            elif self.y < target_y:
                self.y += 1
            else:
                self.state = 'open'
                self.on_floor = self.current_target
                self.current_target = None
                self.ding_sound.play()
                self.stop_timer = time.time()

        elif self.state == 'open':
            elapsed_time = time.time() - self.stop_timer
            if elapsed_time >= self.stop_time:
                self.state = 'free'
                self.stop_timer = None
                self.timer_text = None
            else:
                self.timer_text = f'{self.stop_time - elapsed_time:.1f}s'


        
    def time_to_floor(self, floor):#זמן שלוקח לכל קומה 
        if self.time_to_finish:
            time_elapsed = time.time() - self.whatch
            total_time = self.time_to_finish - time_elapsed
        else:
            total_time = 0
        last_floor = self.target[-1] if self.target else self.on_floor
        distance = abs(floor - last_floor)
        return total_time + distance * ELEVATOR_SPEED + ARRIVAL_DELAY
 
    def new_call(self, floor):#מחזיר את הזמן של הקומה 
        self.time_to_finish = self.time_to_floor(floor)
        self.whatch = time.time()
        self.target.append(floor)
        assert self.time_to_finish >= 0
        return self.time_to_finish - ARRIVAL_DELAY

    def taime(self):
       self.m = self.time_to_finish - ARRIVAL_DELAY
       return self.m

    def draw(self, screen):
        screen.blit(self.elevator_image, (self.num * (self.elevator_image.get_width() + 20), self.y))
        if self.timer_text:
            font = pygame.font.Font(None, 36)
            text = font.render(self.timer_text, True, (255, 0, 0))
            screen.blit(text, (self.num * (self.elevator_image.get_width() + 20) + 10, self.y - 30))
