from seting import *
from bilding import *
class Elevator:
    def __init__(self, num, num_of_floors):
        self.num = num
        self.on_floor = 0 #random.randint(0, num_of_floors - 1)
        self.target = None
        self.state = 'free'  # 'goingUp', 'goingDown', 'open', 'waiting'
        self.y = self.floor_to_y(self.on_floor)
       # self.screen_width = screen_width
        self.arrival_time = 0
    def floor_to_y(self, floor):
        floor_height = screen_height // NUM_OF_FLOORS
        return screen_height - (floor + 1) * floor_height
    def thesfloor(self, floor):
        pass

    def move(self):
        if self.target is not None:
            target_y = self.floor_to_y(self.target)  # מחשבת את מיקום ה-Y של הקומה היעד.
            if self.y > target_y:
                self.state = 'goingDown'  # משנה את המצב ל-"יורדת".
                self.y -= 1  # מזיזה את המעלית כלפי מטה.
                self.arrival_time +=ELEVATOR_SPEED 
            elif self.y < target_y:
                self.state = 'goingUp'  # משנה את המצב ל-"עולה".
                self.y += 1  # מזיזה את המעלית כלפי מעלה.
                self.arrival_time +=ELEVATOR_SPEED 
            else:
                self.on_floor = self.target  # המעלית הגיעה לקומה היעד.
                self.state = 'open'  # משנה את המצב ל-"פתוחה".
                ding_sound.play()  # מנגנת צליל הגעה.
                self.arrival_time += ARRIVAL_DELAY

                
                #time.sleep(ARRIVAL_DELAY)  # משהה את הפעולה למשך זמן מוגדר.
                self.target = None  # מאפסת את היעד.
                self.state = 'free'  # משנה את המצב ל-"פנויה".
                #if self.state == 'free':
                   # for i in range(target_y,-1,-1):
                     #   self.state = 'goingDown'  # משנה את המצב ל-"יורדת".
                       # self.y -= 1
                        
                       

    def draw(self, screen):
        screen.blit(elevator_image, (self.num * (elevator_image.get_width() + 10), self.y))
       #screen.blit(elevator_image, (self.num * (screen_width // NUM_OF_ELEVATORS, self.y))
