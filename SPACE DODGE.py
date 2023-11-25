import pygame 
import time 
import random 
pygame.font.init() 

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Space Dodge") 

bg = pygame.transform.scale(pygame.image.load("BG.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40 
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20

FONT = pygame.font.SysFont("comicsans", 30)
def main(): 
    run = True 
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                        PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock() 
    start_time = time.time()
    elapsed_time =  0

    star_add_increment = 2000
    star_count = 0
    star_vel = 5
    i = 3

    stars = [] 
    hit = False

    while run: 
        # Number of time you want the while loop to run(60 times p/s)fps
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if star_count > star_add_increment: 
            for _ in range(i): 
                star_x = random.randint(0, WIDTH - STAR_WIDTH) 
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) 
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            star_vel += 0.25
            i += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False 
                break 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0: 
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH: 
            player.x += PLAYER_VEL

        # copy of list
        for star in stars[:]: 
            star.y += star_vel
            if star.y + star.height > HEIGHT: 
                stars.remove(star)
            elif star.y >= player.y and star.colliderect(player): 
                stars.remove(star) 
                hit = True 
                break
        
        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, 
                     HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update() 
            pygame.time.delay(4000) 
            break
        
        draw(player, elapsed_time, stars)
    pygame.quit()

def draw(player, elapsed_time, stars): 
    WIN.blit(bg, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))
    pygame.draw.rect(WIN, "red", player)
    for star in stars: 
        pygame.draw.rect(WIN, "white", star)
    pygame.display.update() 


if __name__ == "__main__": 
    main() 

