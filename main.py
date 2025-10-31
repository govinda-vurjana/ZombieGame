from game import ZombieShooter
import pygame
import sys
import numpy as np
import torch
import cv2

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
WORLD_WIDTH, WORLD_HEIGHT = 1800, 1200
FPS = 60

game = ZombieShooter(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                     world_height=WORLD_HEIGHT, world_width=WORLD_WIDTH,
                     fps=FPS, sound=False, human=True)

# Game loop
observation, info = game.reset()


while True:

    action = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                action = 5
            elif event.key == pygame.K_SPACE:
                action = 6
            elif event.key == pygame.K_ESCAPE:
                action = 7

    keys = pygame.key.get_pressed()

    if action == 0:
        if keys[pygame.K_w]:
            action = 1
        if keys[pygame.K_s]:
            action = 2
        if keys[pygame.K_a]:
            action = 3
        if keys[pygame.K_d]:
            action = 4

    observation, reward, done, truncated, info = game.step(action=action)

    # print("Observation: ", observation)

    if reward != 0:
        print("Reward: ", reward)
        print("Done: ", done)

        img_array = torch.clip(observation.squeeze(0), 0, 255).numpy().astype(np.uint8)

        result = cv2.imwrite("temp/screen.jpg", img_array)