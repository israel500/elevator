from seting import *
from bilding import *
from elevator import *
from floobuton import *

class ElevatorSystem:
    def __init__(self, num_of_elevators, num_of_floors):
        self.num_of_floors = num_of_floors #מספר הקומות בבניין.
        self.elevators = [Elevator(i, num_of_floors) for i in range(num_of_elevators)]#רשימה שלהמעליות
        self.queue = [] #תור (רשימה) של קריאות למעליות.
        self.lock = threading.Lock() #מנעול (Lock) מ- threading לנעילה של משאבים בזמן פעולות שמשנות את מצב התור (שימוש בסנכרון).
        #self.quickest_elevator = Floor.quickest_elevator(elevator.elevators)
        self.floor_buttons = [FloorButton(floor, screen_width - 50, screen_height - (floor + 1) * (screen_height // num_of_floors), 50, screen_height // num_of_floors)for floor in range(num_of_floors)]#רשימה של הכפתורים

    def call_elevator(self, to_floor):#מקבלת כפרמטר את הקומה (to_floor) אליה נדרשת המעלית.
        with self.lock:#נעילת המנעול (with self.lock) כדי למנוע מצבים של גישה מקבילה לאותו משאב.
            if to_floor not in self.queue:
                self.queue.append(to_floor)
                self.floor_buttons[to_floor].click()#מגדיר לחיצה על הכפתור
                self.process_queue()#בודקת אם הקומה כבר בתור הקריאות. אם לא, מוסיפה אותה לתור ומפעילה את הפונקציה process_queue.
    


    def calculate_time(self, elevator, target_floor):#חישוב הזמנים של כל מעלית 
        distance = abs(elevator.on_floor - target_floor)

        if elevator.target is not None:
            total_time = distance * ELEVATOR_SPEED + ARRIVAL_DELAY
        else:
            total_time = distance * ELEVATOR_SPEED
        return total_time

    def quickest_elevator(self, to_floor):
        best_time = float('inf')
        best_elevator = None
        for elevator in self.elevators:
            time_to_target = self.calculate_time(elevator, to_floor)
            if time_to_target < best_time:
                best_time = time_to_target
                best_elevator = elevator
        return  best_elevator  , best_time
    

    def process_queue(self):
        if not self.queue:
            return

        to_floor = self.queue[0]
        best_elevator, time_to_arrival = self.quickest_elevator(to_floor)
        best_elevator.target = to_floor
        self.floor_buttons[to_floor].arrival_time = time_to_arrival
        self.queue.pop(0)


    # def process_queue(self):
    #     if not self.queue:#בודקת אם התור ריק. אם כן, חוזרת מייד
    #         return
    #     for elevator in self.elevators:
    #         if elevator.state == 'free':
    #                r = self.quickest_elevator(self, elevator)
    #         if elevator.state == 'open':
    #               r = self.quickest_elevator(self, elevator)

    #     to_floor = self.queue[0]
    #     free_elevators = [elevator for elevator in self.elevators if elevator.state == 'free']#מחפשת את כל המעליות הפנויות (state הוא 'free').
    #     #all_elevetor =[elevator for elevator in self.elevators ]#כל המעליות
    #     #for i in all_elevetor:

    #     if not free_elevators:#אם אין מעליות פנויות, חוזרת מייד        
    #         return 

        
    #     best_choice = min(free_elevators, key=lambda e: abs(e.on_floor - to_floor))
    #     best_choice.target = to_floor# קובעת את הקומה היעד של המעלית שבחרה ומסירה את הקריאה מהתור
    #     self.queue.pop(0)

    def update(self):#מעדכנת את מצב כל המעליות על ידי קריאה לפונקציה move של כל מעלית.
        for elevator in self.elevators:
            elevator.move()
            if elevator.state == 'open' and elevator.target is None:
                button.arrival_time += ARRIVAL_DELAY
            if elevator.state == 'free' and elevator.target is None:
                for button in self.floor_buttons:
                    if button.color == BUTTON_ACTIVE_COLOR and elevator.on_floor == button.floor_number:
                        button.reset()
                        button.arrival_time = 0

        for button in self.floor_buttons:#הורדת מיספר השניות
            if button.color == BUTTON_ACTIVE_COLOR and button.arrival_time > 0:
                button.arrival_time -= 1 / 60  # Assuming 60 FPS




    def draw(self, screen):#מציירת את כל המעליות על המסך על ידי קריאה לפונקציה draw של כל מעלית.
        for elevator in self.elevators:
            elevator.draw(screen)
        for button in self.floor_buttons:
            button.draw(screen)
