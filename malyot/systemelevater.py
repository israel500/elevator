from seting import *
from bilding import *
from elevator import *
from floobuton import *

class ElevatorSystem:
    def __init__(self, num_of_elevators, num_of_floors):

        self.num_of_floors = num_of_floors #מספר הקומות בבניין.
        self.elevators = [Elevator(i, num_of_floors, screen_height, elevator_image, ding_sound) for i in range(num_of_elevators)]#רשימה שלהמעליות
        self.floor_buttons = [FloorButton(floor, screen_width - 50, screen_height - (floor + 1) * (screen_height // num_of_floors), 50, screen_height // num_of_floors) for floor in range(num_of_floors)]#שימה של הכפתורים
        self.t =0
        self.last_time = time.time()


    


    def call_elevator(self, to_floor):#מקבלת כפרמטר את הקומה (to_floor) אליה נדרשת המעלית.
        for el in self.elevators:
            if to_floor in el.target:
                return
            if to_floor == el.on_floor:
                return

        self.floor_buttons[to_floor].click()#מגדיר לחיצה על הכפתור
        elevator = min(self.elevators, key=lambda x: x.time_to_floor(to_floor))
        elevator.new_call(to_floor)
        self.floor_buttons[to_floor].arrival_time = elevator.new_call(to_floor)
        
    #
    # def calculate_time(self, elevator, target_floor):#חישוב הזמנים של כל מעלית 
    #     distance = abs(elevator.on_floor - target_floor)
    #     if elevator.state == 'free' and elevator.target is not None:
    #         total_time = distance * ELEVATOR_SPEED
    #     if elevator.state == 'open' and elevator.target is not None:
    #          total_time = distance * ELEVATOR_SPEED + ARRIVAL_DELAY
    #     if elevator.state == 'goingDown' and elevator.target is not None:
    #          total_time = distance * ELEVATOR_SPEED + ARRIVAL_DELAY  + 100
    #     if elevator.state == 'goingUp' and elevator.target is not None:
    #        total_time = abs(elevator.on_floor - target_floor)+distance * ELEVATOR_SPEED + ARRIVAL_DELAY + 100
    #     return total_time
    


        
    # def y(self, to_floor):
    #     elevator = self.quickest_elevator(to_floor)

    def update(self):
        for elevator in self.elevators:
            elevator.move()
            # השגת הכפתור המתאים למעלית
            for button in self.floor_buttons:
                if button.floor_number == elevator.on_floor:
                    # if elevator.state == 'goingUp' and elevator.target :
                    #     button.arrival_time += self.time_to_floor(elevator.targe)
                    # if elevator.state ==  'goingUp' and elevator.target :
                    #     button.arrival_time += self.time_to_finish - ARRIVAL_DELAY
                    # if elevator.state ==  'goingUp' and elevator.target :
                    #      button.arrival_time -= self.time_to_finish - ARRIVAL_DELAY
                    # בדיקה האם המעלית פתוחה ואין לה מטרה
                    if elevator.state == 'open' and elevator.target: # is None:
                        # button.arrival_time -= ARRIVAL_DELAY
                        pass
                         
                    # בדיקה האם המעלית פנויה ואין לה מטרה
                    if elevator.state == 'free' and elevator.target :#is None:
                        if button.color == BUTTON_ACTIVE_COLOR:
                            button.reset()
                            button.arrival_time = 0

        # הורדת מיספר השניות
        for button in self.floor_buttons:
            if button.color == BUTTON_ACTIVE_COLOR and button.arrival_time > 0:
                button.arrival_time -= (time.time()- self.last_time)
        self.last_time = time.time()



    def draw(self, screen):#מציירת את כל המעליות על המסך על ידי קריאה לפונקציה draw של כל מעלית.
        for elevator in self.elevators:
            elevator.draw(screen)
        for button in self.floor_buttons:
            button.draw(screen)
