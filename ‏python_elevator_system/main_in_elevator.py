from seting import *
from bilding import *
from elevator import *
from systemelevater import *
from floobuton import *
def main():
    clock = pygame.time.Clock()
    elevator_system = ElevatorSystem(NUM_OF_ELEVATORS, NUM_OF_FLOORS)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                floor_height = screen_height // NUM_OF_FLOORS
                clicked_floor = NUM_OF_FLOORS - mouse_y // floor_height - 1
                elevator_system.call_elevator(clicked_floor)

                for button in elevator_system.floor_buttons:
                                if button.rect.collidepoint(mouse_x, mouse_y):
                                    button.click()
                                    elevator_system.call_elevator(button.floor_number)



        elevator_system.update()

        screen.fill(BACKGROUND_COLOR)
        draw_building(screen)
        elevator_system.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()
