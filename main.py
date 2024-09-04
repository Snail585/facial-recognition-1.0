import pandas as pd
from pathlib import Path
from deepface import DeepFace
import cv2
import pygame
import pygame.camera
import sys

pygame.init() # Initialize Pygame
pygame.camera.init()
#window sizing and caption
window_size = (1000, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Treasure hunt!')

# font controls
title = pygame.font.SysFont('Courier New Regular', 40)
emotifont = pygame.font.SysFont('Courier New Regular', 50)
font = pygame.font.SysFont('Courier New Regular', 21)

def angerInfo():
    angerScreen = pygame.display.set_mode(1000,600)
    pygame.display.set_caption("All About Anger")
    titleA_surface = title.render("Let's Learn More About Anger!", False, (100, 182, 172))
cam_port = 0
cam = cv2.VideoCapture(cam_port)
def pic():
    result, image = cam.read()
    results_surface = None
    if result:
        cv2.imshow("photo", image)  # shows results
        cv2.imwrite("photo.png", image)  # saves img
        objs = DeepFace.analyze(
            enforce_detection=False,
            img_path="photo.png",
            actions=['emotion'],
        )
        high = 0
        for x in objs[0]["emotion"].values():
            if x > high:
                high = x
        high = round(high, 1)
        resu = ("We are " + str(high) + "% sure that you are feeling " +objs[0]["dominant_emotion"] + "!")
        results_surface = font.render(resu, False, (0,0,0))
        print(objs[0]["emotion"].values())
        print(objs[0]["emotion"])
        cv2.waitKey(0)
    else:
        print("No image detected")
    return results_surface
#cam preview setup
previewCam = pygame.camera.Camera(0, (375,400),) #0 used to be cam
previewCam.start()

#words setup
welcome_surface = title.render('Welcome to Treasure Hunt!', False, (100, 182, 172))
instructions_surface1 = font.render('Pressing THIS button will take a picture using your camera!'
                                   ' Try aiming at your face to', False, (0,0,0))
instructions_surface2 = font.render(' allow maximum efficiency in emotion detection. Try to find and unlock 7 emotions to win!'
                                   , False, (0, 0, 0))

# button setup
button_surface = pygame.Surface((150, 50)) # button surface
text = font.render("Say Click, take a pic!", True, (0, 0, 0))
text_centering = text.get_rect(center=(button_surface.get_width() / 2,
                                  button_surface.get_height() / 2))
button_rect = pygame.Rect(55, 250, 100, 50) # first two moves button and last two is how big
#anger button setup
anger_surface = pygame.Surface((75, 75))
anger_text = emotifont.render(">:(", True, (102, 0, 0))
anger_centering = anger_text.get_rect(center=(anger_surface.get_width() / 2,anger_surface.get_height() / 2))
anger_rect = pygame.Rect(163.5, 500, 75, 75) # first two moves sensing button and last two is how big
#surprise button setup
surprise_surface = pygame.Surface((75, 75))
surprise_text = emotifont.render(":0", True, (102, 51, 0))
surprise_centering = surprise_text.get_rect(center=(surprise_surface.get_width() / 2,surprise_surface.get_height() / 2))
surprise_rect = pygame.Rect(263.5, 500, 75, 75) # first two moves sensing button and last two is how big
#happy button setup
happy_surface = pygame.Surface((75, 75))
happy_text = emotifont.render(":D", True, (102, 102, 0))
happy_centering = happy_text.get_rect(center=(happy_surface.get_width() / 2,happy_surface.get_height() / 2))
happy_rect = pygame.Rect(363.5, 500, 75, 75) # first two moves sensing button and last two is how big
#disgust button setup
disgust_surface = pygame.Surface((75, 75))
disgust_text = emotifont.render(">:P", True, (0, 102, 0))
disgust_centering = disgust_text.get_rect(center=(disgust_surface.get_width() / 2,disgust_surface.get_height() / 2))
disgust_rect = pygame.Rect(462.5, 500, 75, 75) # first two moves sensing button and last two is how big
#sad button setup
sad_surface = pygame.Surface((75, 75))
sad_text = emotifont.render(":(", True, (0, 76, 153))
sad_centering = sad_text.get_rect(center=(sad_surface.get_width() / 2,sad_surface.get_height() / 2))
sad_rect = pygame.Rect(562.5, 500, 75, 75) # first two moves sensing button and last two is how big
#fear button setup
fear_surface = pygame.Surface((75, 75))
fear_text = emotifont.render("<:0", True, (51, 0, 102))
fear_centering = fear_text.get_rect(center=(fear_surface.get_width() / 2,fear_surface.get_height() / 2))
fear_rect = pygame.Rect(662.5, 500, 75, 75) # first two moves sensing button and last two is how big
#neutral button setup
neutral_surface = pygame.Surface((75, 75))
neutral_text = emotifont.render(":|", True, (32,32,32))
neutral_centering = neutral_text.get_rect(center=(neutral_surface.get_width() / 2,neutral_surface.get_height() / 2))
neutral_rect = pygame.Rect(762.5, 500, 75, 75) # first two moves sensing button and last two is how big
taken = False
results_surface = None
while True:
    screen.fill((255,255,255)) #fills screen with rgb colour
    for event in pygame.event.get(): #Get events from the event queue
        if event.type == pygame.QUIT: #Check for the quit event
            pygame.quit()
            sys.exit()
        #take picture button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                taken = True
                results_surface = pic()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if anger_rect.collidepoint(event.pos):
                angerInfo()
    if taken:
        screen.blit(results_surface, (562.5, 300))
    # button colours
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (231, 189, 255), (1, 1, 148, 48)) #hover
    else:
        pygame.draw.rect(button_surface, (199, 0, 146), (0, 0, 150, 50)) #outline
        pygame.draw.rect(button_surface, (255, 195, 252), (1, 1, 148, 48)) #normal fill
    #anger colours
    if anger_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(anger_surface, (255, 102, 102), (1, 1, 73, 73))#hover
    else:
        pygame.draw.rect(anger_surface, (204, 0, 0), (0, 0, 75, 75))  # outline
        pygame.draw.rect(anger_surface, (255, 153, 153), (1, 1, 73, 73))  # normal fill
    # surprise colours
        if surprise_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surprise_surface, (255, 178, 102), (1, 1, 73, 73))  # hover
        else:
            pygame.draw.rect(surprise_surface, (204, 102, 0), (0, 0, 75, 75))  # outline
            pygame.draw.rect(surprise_surface, (255, 204, 153), (1, 1, 73, 73))  # normal fill
    # happy colours
        if happy_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(happy_surface, (255, 255, 102), (1, 1, 73, 73))  # hover
        else:
            pygame.draw.rect(happy_surface, (204, 204, 0), (0, 0, 75, 75))  # outline
            pygame.draw.rect(happy_surface, (255, 255, 153), (1, 1, 73, 73))  # normal fill
    # disgust colours
    if disgust_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(disgust_surface, (102, 255, 102), (1, 1, 73, 73))  # hover
    else:
        pygame.draw.rect(disgust_surface, (0, 204, 0), (0, 0, 75, 75))  # outline
        pygame.draw.rect(disgust_surface, (153, 255, 153), (1, 1, 73, 73))  # normal fill
    # sad colours
    if sad_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(sad_surface, (102, 178, 255), (1, 1, 73, 73))  # hover
    else:
        pygame.draw.rect(sad_surface, (0, 128, 255), (0, 0, 75, 75))  # outline
        pygame.draw.rect(sad_surface, (153, 204, 255), (1, 1, 73, 73))  # normal fill
    # fear colours
    if fear_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(fear_surface, (178, 102, 255), (1, 1, 73, 73))  # hover
    else:
        pygame.draw.rect(fear_surface, (102, 0, 204), (0, 0, 75, 75))  # outline
        pygame.draw.rect(fear_surface, (204, 153, 255), (1, 1, 73, 73))  # normal fill
    # neutral colours
    if neutral_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(neutral_surface, (192, 192, 192), (1, 1, 73, 73))  # hover
    else:
        pygame.draw.rect(neutral_surface, (96,96,96), (0, 0, 75, 75))  # outline
        pygame.draw.rect(neutral_surface, (224, 224, 224), (1, 1, 73, 73))  # normal fill
    #showing all parts
    screen.blit(welcome_surface, (315, 0))
    screen.blit(instructions_surface1, (200, 40))
    screen.blit(instructions_surface2, (185, 60))
    #picture button
    button_surface.blit(text, text_centering)
    screen.blit(button_surface, (button_rect.x, button_rect.y))
    #anger button
    anger_surface.blit(anger_text, anger_centering)
    screen.blit(anger_surface, (anger_rect.x, anger_rect.y))
    # surprise button
    surprise_surface.blit(surprise_text, surprise_centering)
    screen.blit(surprise_surface, (surprise_rect.x, surprise_rect.y))
    # happy button
    happy_surface.blit(happy_text, happy_centering)
    screen.blit(happy_surface, (happy_rect.x, happy_rect.y))
    # disgust button
    disgust_surface.blit(disgust_text, disgust_centering)
    screen.blit(disgust_surface, (disgust_rect.x, disgust_rect.y))
    # sad button
    sad_surface.blit(sad_text, sad_centering)
    screen.blit(sad_surface, (sad_rect.x, sad_rect.y))
    # fear button
    fear_surface.blit(fear_text, fear_centering)
    screen.blit(fear_surface, (fear_rect.x, fear_rect.y))
    # neutral button
    neutral_surface.blit(neutral_text, neutral_centering)
    screen.blit(neutral_surface, (neutral_rect.x, neutral_rect.y))
    # camera preview
    image = previewCam.get_image()
    screen.blit(image, (230, 100))
    pygame.display.update()# Update the game state
#ending the program
cv2.destroyAllWindows()
