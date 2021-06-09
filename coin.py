import pgzrun
import random


WIDTH = 600
HEIGHT = 600

NUM_COINS = 3
NUM_HEDGEHOGS = 5

fox_starting_position = (int(WIDTH / 2), int(HEIGHT / 2))


def draw():
    global coins
    global fox_dead
    global hedgehogs

    screen.fill("dark green")
    fox.draw()
    for coin in coins:
        coin.draw()
    for hedgehog in hedgehogs:
        hedgehog.draw()
    screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))

    if game_over == True:
        screen.fill("pink")
        msg = None
        if fox_dead:
            msg = f"You died! Final Score: {score}"
        else:
            msg = f"Final Score: {score}"
        screen.draw.text(msg, topleft=(10, 10), fontsize=60)


def place_actor_randomly(actor):
    actor.x = random.randint(20, WIDTH - 20)
    actor.y = random.randint(20, HEIGHT - 20)


def time_up():
    global game_over
    game_over = True


def update():
    global score
    global fox_dead
    global game_over

    if keyboard.left:
        fox.x  -= 4
    elif keyboard.right:
        fox.x  += 4
    elif keyboard.up:
        fox.y  -= 4
    elif keyboard.down:
        fox.y  += 4

    for coin in coins:
        coin_collected = fox.colliderect(coin)
        if coin_collected:
            score += 10
            place_actor_randomly(coin)

    for hedgehog in hedgehogs:
        hit_hedgehog = fox.colliderect(hedgehog)
        if hit_hedgehog:
            game_over = True
            fox_dead = True
            break


def place_coins():
    for coin in coins:
        place_actor_randomly(coin)


def place_hedgehog(hedgehog):
    w = random.randint(0, 1)
    dx = random.randint(50, int(WIDTH / 2 - 20))
    hedgehog.x = fox_starting_position[0] + (w * dx - (1 - w) * dx)
    w = random.randint(0, 1)
    dy = random.randint(50, int(HEIGHT / 2 - 20))
    hedgehog.y = fox_starting_position[1] + (w * dy - (1 - w) * dy)


def place_hedgehogs():
    for hedgehog in hedgehogs:
        place_hedgehog(hedgehog)


score = 0
game_over = False

fox = Actor("fox")
fox.pos = fox_starting_position
fox_dead = False

coins = [ Actor("coin") for i in range(NUM_COINS) ]
place_coins()

hedgehogs = [ Actor("hedgehog") for i in range(NUM_HEDGEHOGS) ]
place_hedgehogs()

clock.schedule(time_up, 20.0)

pgzrun.go()
