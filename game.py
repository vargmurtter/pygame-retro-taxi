import sys
import pygame
import time
import random as rnd

def show_text(screen, text_to_show, coords, size, color = (255,255,255)):
	font = pygame.font.Font('data/fonts/ARCADECLASSIC.TTF', size)
	text = font.render(text_to_show, True, color)
	screen.blit(text, coords)

def show_start_screen(screen):
	show_text(screen, "TAXI", (100, 60), 50, color=(255,255,100))
	show_text(screen, "game by", (100, 170), 30)
	show_text(screen, "varg   murtter", (40, 190), 35)
	show_text(screen, "press SPACE to start", (40, 300), 21)

if __name__ == '__main__':
	pygame.init()

	SCREEN_SIZE = (300, 640)
	WHITE = (255,255,255)
	PAUSE = False
	START = False

	screen = pygame.display.set_mode(SCREEN_SIZE)

	pygame.display.set_caption("TAXI")

	speed = 3
	score = 0
	x = 140
	y = 320

	car_speed = 3
	cars = []

	current_time = 0
	last_time = 0


	clock = pygame.time.Clock()
	while True:
		clock.tick(50) 

		current_time = time.time()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill((0, 0, 0))

		if START:
			keys = pygame.key.get_pressed()
			
			if keys[ord("w")]: 
				y -= speed
			if keys[ord("s")]:
				y += speed
			if keys[ord("a")]:
				x -= speed
			if keys[ord("d")]:
				x += speed

			if x >= 280:
				x = 280
			if x <= 0:
				x = 0

			if y >= 600:
				y = 600
			if y <= 0:
				y = 0


			bound_left = pygame.draw.rect(screen, WHITE, (0,0,20,640))
			bound_right = pygame.draw.rect(screen, WHITE, (280,0,20,640))

			player = None
			if PAUSE != True:
				pygame.draw.rect(screen, WHITE, (150, 0, 2, 640))
				
				player = pygame.draw.rect(screen, (255,255,100), (x, y, 20, 40))

				score += 1
				show_text(screen, "Score   " + str(score), (25, 5), 16, color=(142,142,142))

				i = 0
				while i < len(cars):
					car = pygame.draw.rect(screen, WHITE, (cars[i][0],cars[i][1],20,30))

					if player.colliderect(car) or player.colliderect(bound_right) or player.colliderect(bound_left):
						PAUSE = True

					cars[i][1] += car_speed
					i += 1
				
				if current_time > (last_time + 0.3):
					cars.append([rnd.randint(20, 260), 0])
					last_time = time.time()
			else:
				show_text(screen, "THE END", (65, 250), 50)
				show_text(screen, "your score is", (80, 330), 21)
				show_text(screen, str(score), (130, 350), 30)
				show_text(screen, "press SPACE to reload", (40, 420), 21)
				if keys[pygame.K_SPACE]:
					x = 150
					y = 320
					cars = []
					score = 0
					PAUSE = False
		else:
			show_start_screen(screen)
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]: 
				START = True

		pygame.display.flip()