import pygame
import sys
import math

pygame.init()
num_blue=0
limit=7
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Drawing")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

circle_colors = [RED]*10

def check_jmp(clicked_circle, yellow_circle_index, circle_colors):
    if clicked_circle == 0 :
        if yellow_circle_index ==3 and circle_colors[1] == BLUE:
            circle_colors[1] = RED
            return True
        elif yellow_circle_index ==7 and circle_colors[9] == BLUE:
            circle_colors[9] = RED
            return True
    elif clicked_circle == 1 :
        if yellow_circle_index ==4 and circle_colors[3] == BLUE:
            circle_colors[3] = RED
            return True
        elif yellow_circle_index ==8 and circle_colors[9] == BLUE:
            circle_colors[9] = RED
            return True
    elif clicked_circle == 2 :
        if yellow_circle_index ==9 and circle_colors[1] == BLUE:
            circle_colors[1] = RED
            return True
        elif yellow_circle_index ==5 and circle_colors[3] == BLUE:
            circle_colors[3] = RED
            return True
    elif clicked_circle == 3 :
        if yellow_circle_index == 0 and circle_colors[1] == BLUE:
            circle_colors[1] = RED
            return True
        elif yellow_circle_index == 6 and circle_colors[5] == BLUE:
            circle_colors[5] = RED
            return True
    elif clicked_circle == 4 :
        if yellow_circle_index ==1 and circle_colors[3] == BLUE:
            circle_colors[3] = RED
            return True
        elif yellow_circle_index ==7 and circle_colors[5] == BLUE:
            circle_colors[5] = RED
            return True
    elif clicked_circle == 5 :
        if yellow_circle_index ==2 and circle_colors[3] == BLUE:
            circle_colors[3] = RED
            return True
        elif yellow_circle_index ==8 and circle_colors[7] == BLUE:
            circle_colors[7] = RED
            return True
    elif clicked_circle == 6:
        if yellow_circle_index ==3 and circle_colors[5] == BLUE:
            circle_colors[5] = RED
            return True
        elif yellow_circle_index ==9 and circle_colors[7] == BLUE:
            circle_colors[7] = RED
            return True
    elif clicked_circle == 7:
        if yellow_circle_index ==4 and circle_colors[5] == BLUE:
            circle_colors[5] = RED
            return True
        elif yellow_circle_index ==0 and circle_colors[9] == BLUE:
            circle_colors[9] = RED
            return True
    elif clicked_circle == 8 :
        if yellow_circle_index ==5 and circle_colors[7] == BLUE:
            circle_colors[7] = RED
            return True
        elif yellow_circle_index ==1 and circle_colors[9] == BLUE:
            circle_colors[9] = RED
            return True
    elif clicked_circle == 9 :
        if yellow_circle_index ==6 and circle_colors[7] == BLUE:
            circle_colors[7] = RED
            return True
        elif yellow_circle_index ==2 and circle_colors[1] == BLUE:
            circle_colors[1] = RED
            return True
    return False

def blocked(yellow_circle_index, circle_colors):
    if yellow_circle_index==0:
        if circle_colors[1]==BLUE and circle_colors[9]==BLUE and circle_colors[7]==BLUE and circle_colors[3]==BLUE:
            return True
    elif yellow_circle_index==2:
        if circle_colors[1]==BLUE and circle_colors[3]==BLUE and circle_colors[9]==BLUE and circle_colors[5]==BLUE:
            return True
    elif yellow_circle_index==4:
        if circle_colors[3]==BLUE and circle_colors[5]==BLUE and circle_colors[7]==BLUE and circle_colors[1]==BLUE:
            return True
    elif yellow_circle_index==6:
        if circle_colors[5]==BLUE and circle_colors[9]==BLUE and circle_colors[7]==BLUE and circle_colors[3]==BLUE:
            return True
    elif yellow_circle_index==8:
        if circle_colors[1]==BLUE and circle_colors[9]==BLUE and circle_colors[7]==BLUE and circle_colors[5]==BLUE:
            return True
    elif yellow_circle_index==1:
        if circle_colors[0]==BLUE and circle_colors[3]==BLUE and circle_colors[4]==BLUE and circle_colors[2]==BLUE and circle_colors[9]==BLUE and circle_colors[8]==BLUE:
            return True
    elif yellow_circle_index==3:
        if circle_colors[2]==BLUE and circle_colors[5]==BLUE and circle_colors[6]==BLUE and circle_colors[4]==BLUE and circle_colors[1]==BLUE and circle_colors[0]==BLUE:
            return True
    elif yellow_circle_index==5:
        if circle_colors[6]==BLUE and circle_colors[3]==BLUE and circle_colors[2]==BLUE and circle_colors[4]==BLUE and circle_colors[7]==BLUE and circle_colors[8]==BLUE:
            return True
    elif yellow_circle_index==7:
        if circle_colors[6]==BLUE and circle_colors[9]==BLUE and circle_colors[0]==BLUE and circle_colors[8]==BLUE and circle_colors[5]==BLUE and circle_colors[4]==BLUE:
            return True
    elif yellow_circle_index==9:
        if circle_colors[8]==BLUE and circle_colors[1]==BLUE and circle_colors[2]==BLUE and circle_colors[0]==BLUE and circle_colors[7]==BLUE and circle_colors[6]==BLUE:
            return True
    return False

def draw_star(surface, color, center, size, points, circle_colors):
    angle = math.pi / points
    half_angle = math.pi / 2
    star_points = []
    circle_font = pygame.font.SysFont(None, 24)  
    
    for i in range(points * 2):
        if i % 2 == 0:
            x = center[0] + math.cos(angle * i - half_angle) * size
            y = center[1] - math.sin(angle * i - half_angle) * size
        else:
            x = center[0] + (math.cos(angle * i - half_angle) * size / 2)
            y = center[1] - (math.sin(angle * i - half_angle) * size / 2)
        star_points.append((x, y))
    
    pygame.draw.polygon(surface, color, star_points)
    
    for i, point in enumerate(star_points):
        circle_color = circle_colors[i]
        pygame.draw.circle(surface, circle_color, (int(point[0]), int(point[1])), 10)
        
        text_surface = circle_font.render(str(i + 1), True, BLACK)
        text_rect = text_surface.get_rect(center=(point[0], point[1]))
        surface.blit(text_surface, text_rect)

    return star_points, circle_colors

def main():
    running = True
    global num_blue
    global limit
    star_points = None
    yellow_circle_index = None 
    num_blue_circles = 0 
    player_turn = True 
    first_click = True  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if player_turn: 
                    if star_points:
                        clicked_circle = None
                        for i, point in enumerate(star_points):
                            if math.sqrt((pos[0] - point[0]) ** 2 + (pos[1] - point[1]) ** 2) <= 10:
                                clicked_circle = i
                                print(i)
                                break

                        if yellow_circle_index is None:
                            if clicked_circle is not None and circle_colors[clicked_circle] != BLUE:
                                if first_click:  
                                    circle_colors[clicked_circle] = BLUE
                                    first_click = False
                                    num_blue=num_blue+1
                                else:
                                    circle_colors[clicked_circle] = YELLOW
                                    yellow_circle_index = clicked_circle
                                    player_turn = False  
                        else:
                            if clicked_circle is not None:
                                if circle_colors[clicked_circle] == RED:
                                    if abs(clicked_circle - yellow_circle_index) == 1 or abs(clicked_circle - yellow_circle_index) == 2 or (abs(clicked_circle - yellow_circle_index) == 8 and (yellow_circle_index==1 or yellow_circle_index==9) or (clicked_circle==9 and yellow_circle_index==0) or (clicked_circle==0 and yellow_circle_index==9)):
                                        circle_colors[yellow_circle_index] = RED
                                        circle_colors[clicked_circle] = YELLOW
                                        yellow_circle_index = clicked_circle
                                        
                                        player_turn = False 
                                    elif check_jmp(clicked_circle, yellow_circle_index, circle_colors):
                                        num_blue=num_blue-1
                                        limit=limit-1
                                        
                                        circle_colors[yellow_circle_index] = RED
                                        circle_colors[clicked_circle] = YELLOW
                                        yellow_circle_index = clicked_circle
                                        player_turn = False
                    if limit==3:
                        print("vulture wins")
                        pygame.quit()
                    elif blocked(yellow_circle_index,circle_colors):
                        print("crows wins")

                else:  
                    # print("enterin not")
                    if star_points:
                        clicked_circle = None
                        for i, point in enumerate(star_points):
                            if math.sqrt((pos[0] - point[0]) ** 2 + (pos[1] - point[1]) ** 2) <= 10:
                                clicked_circle = i
                                print(i)
                                break
                    if num_blue<limit:
                        if circle_colors[clicked_circle] == RED:
                            circle_colors[clicked_circle] = BLUE
                            num_blue=num_blue+1
                            player_turn = True
                    elif num_blue==limit:

                        if circle_colors[clicked_circle] == BLUE or circle_colors[clicked_circle] == RED :
                            if 'old' not in locals() and circle_colors[clicked_circle] == BLUE:
                                old=clicked_circle
                                # print("edc and old-",old)
                            elif 'old' in locals() and circle_colors[clicked_circle] == RED:
                                # print("old-",old)
                                # print("ccf",clicked_circle)
                                if abs(clicked_circle - old) == 1 or abs(clicked_circle - old) == 2 or (abs(clicked_circle - old) == 8 and (old==1 or old==9)) or (clicked_circle==9 and old==0) or (clicked_circle==0 and old==9):
                                    # print("entered")
                                    circle_colors[old]=RED
                                    circle_colors[clicked_circle]=BLUE
                                    player_turn = True

                                del old
                    if limit==3:
                        print("vulture wins")
                        pygame.quit()
                    elif blocked(yellow_circle_index,circle_colors):
                        print("crows wins")
                        pygame.quit()
                                

        screen.fill(BLACK)

        star_center = (width // 2, height // 2)
        star_points, cc = draw_star(screen, WHITE, star_center, 100, 5, circle_colors)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
