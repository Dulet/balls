import pygame



def update():
    global circle_velocity
    global circle_position
    
    if circle_follow_mouse:
        mouse_pos_vec = pygame.Vector2(mouse_position[0], mouse_position[1])
        diff_vec = mouse_pos_vec - circle_position
        normalized_direction = pygame.Vector2.normalize(diff_vec)
        circle_velocity += normalized_direction * 1000 * delta_time
        
    circle_position += circle_velocity * delta_time
    
def draw():
    screen.fill((50, 50, 50))
    pygame.draw.circle(screen, (100, 200, 100), circle_position, 10)

pygame.init()

screen = pygame.display.set_mode((640, 460))

game_running = True
delta_time = 0.0
clock = pygame.time.Clock()

circle_position = pygame.Vector2(0, 0)
circle_velocity = pygame.Vector2(0, 0)
circle_follow_mouse = False

mouse_position = (0, 0)
while game_running:
    mouse_position = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            elif event.key == pygame.K_SPACE:
                circle_follow_mouse = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                circle_follow_mouse = False
                
    update()
    draw()
    
    pygame.display.flip()
    
    print("loop" + str(delta_time))

    delta_time = 0.001 * clock.tick(60)
    
    pygame.quit
