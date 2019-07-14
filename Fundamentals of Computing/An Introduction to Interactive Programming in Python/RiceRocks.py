#########################################################################################
#########################################################################################
# Mini-project description - RiceRocks (Asteroids)
######################################################################################### 

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
ROCK = 12
score = 0
lives = 3
time = 0
started = False
friction = 0.01

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

#########################################################################################
#########################################################################################
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
######################################################################################### 

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")


#########################################################################################
#########################################################################################
# helper functions to handle transformations
#########################################################################################

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

#########################################################################################
#########################################################################################
# Ship class
#########################################################################################

class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):  
        if self.thrust:
            canvas.draw_image(ship_image, [135,45], ship_info.get_size(), 
                              self.pos, ship_info.get_size(), self.angle)            
        else:
            canvas.draw_image(ship_image, ship_info.get_center(), ship_info.get_size(),
                              self.pos, ship_info.get_size(), self.angle)     
            
    def key_down(self,key):
        if key == simplegui.KEY_MAP['space']:
            self.shoot()
        elif key == simplegui.KEY_MAP['up']:
            self.thrust = True
            ship_thrust_sound.play()
        elif key == simplegui.KEY_MAP['right']:
            self.angle_vel = 0.1
        elif key == simplegui.KEY_MAP['left']:
            self.angle_vel = -0.1
        else:
            self.angle_vel = 0

    def key_up(self,key):
        if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['left']:
            self.angle_vel = 0
        elif key == simplegui.KEY_MAP['up']:
            self.thrust = False
            ship_thrust_sound.rewind()
            
    def shoot(self):
        global missile_group
        pos = [self.pos[0] + self.radius * angle_to_vector(self.angle)[0],
               self.pos[1] + self.radius * angle_to_vector(self.angle)[1]]
        vel = [self.vel[0] + 4 * angle_to_vector(self.angle)[0],
               self.vel[1] + 4 * angle_to_vector(self.angle)[1]]
        a_missile = Sprite(pos, vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
    
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius          
    
    def update(self):
        self.angle += self.angle_vel
        if self.thrust:
            self.vel[0] += 0.15 * angle_to_vector(self.angle)[0]
            self.vel[1] += 0.15 * angle_to_vector(self.angle)[1]
        self.vel[0] -= self.vel[0] * friction 
        self.vel[1] -= self.vel[1] * friction 
        if self.pos[0] - self.radius> WIDTH:
            self.pos[0] -= WIDTH
        elif self.pos[0] + self.radius < 0:
            self.pos[0] += WIDTH
        elif self.pos[1] - self.radius > HEIGHT:
            self.pos[1] -= HEIGHT
        elif self.pos[1] + self.radius < 0:
            self.pos[1] += HEIGHT
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

#########################################################################################
#########################################################################################
# Sprite class
#########################################################################################       

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, 
                              [self.image_center[0] + self.image_size[0] * self.age, 
                               self.image_center[1]], 
                              self.image_size, self.pos, 
                              self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center,
                              self.image_size, self.pos,
                              self.image_size, self.angle)
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius  
                
    def collide(self,other_object):
        return dist(self.pos, other_object.get_position()) < (self.radius + other_object.get_radius())           
        
    def update(self):
        self.angle += self.angle_vel
        if self.pos[0] - self.radius> WIDTH:
            self.pos[0] -= WIDTH
        elif self.pos[0] + self.radius < 0:
            self.pos[0] += WIDTH
        elif self.pos[1] - self.radius > HEIGHT:
            self.pos[1] -= HEIGHT
        elif self.pos[1] + self.radius < 0:
            self.pos[1] += HEIGHT
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.age += 1
        return self.age >= self.lifespan

        
#########################################################################################
#########################################################################################
# control
#########################################################################################    
# mouseclick handlers that reset UI and conditions whether splash image is drawn

def click(pos):
    global started, score, lives
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.play()
        lives = 3
        score = 0
        
# key        
def key_down(key):
    my_ship.key_down(key)
    
def key_up(key):
    my_ship.key_up(key)       

#########################################################################################
#########################################################################################
# collisions
#########################################################################################
def group_collide(group,other_object):
    global explosion_group
    for i in list(group):
        if i.collide(other_object):
            group.discard(i) 
            an_explosion = Sprite(i.pos,[0,0],0,0,explosion_image,explosion_info,explosion_sound)
            explosion_group.add(an_explosion)
            return True
    else:
        return False
    
def group_group_collide(first_group,second_group):
    collisions = 0
    for i in list(first_group):
        if group_collide(second_group,i):
            collisions += 1
            first_group.discard(i)
    return collisions
            
#########################################################################################
#########################################################################################
# draw
#########################################################################################

# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    pos = [random.random() * WIDTH,random.random() * HEIGHT]
    vel = [2 * random.random() * random.randrange(-1,2,2),3 * random.random() * random.randrange(-1,2,2)]
    ang = random.random() * math.pi
    ang_vel = random.random() * 0.1
    a_rock = Sprite(pos, vel, ang, ang_vel, asteroid_image, asteroid_info)
    if len(rock_group) <= ROCK and started:
        rock_group.add(a_rock)        
        
def process_sprite_group(group,canvas):
    for i in list(group):
        if i.update():
            group.remove(i)
        else:
            i.draw(canvas) 
            i.update()        
    
def draw(canvas):
    global time,lives,score,rock_group,started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group,canvas)
    process_sprite_group(missile_group,canvas)
    process_sprite_group(explosion_group,canvas)
    
    # update ship and sprites
    my_ship.update()
    
    # UI
    if group_collide(rock_group, my_ship):
        lives -= 1
    score += int(500 * random.random() * group_group_collide(missile_group,rock_group))
    canvas.draw_text("Score: %d" % score, (600, 50), 30, 'White')
    canvas.draw_text("Lives: %d" % lives, (40, 50), 30, 'White')    
    
    # Not started
    if lives == 0:
        started = False
        rock_group = set([])
        soundtrack.rewind()
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], splash_info.get_size())

    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
