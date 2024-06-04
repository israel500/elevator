import pygame
import random
import threading
import time

# הגדרות ראשוניות
NUM_OF_ELEVATORS = 6
NUM_OF_FLOORS = 15
ELEVATOR_SPEED = 0.5  # מהירות תנועה בקומה
ARRIVAL_DELAY = 2  # עיכוב בהגעה לקומה
