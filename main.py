import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_card = Scoreboard()


screen.listen()
screen.onkey(player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars()
    car_manager.move_car()

    #detecting collision of turtle with car
    for car in car_manager.car:
        if car.distance(player) < 20:
            game_is_on = False
            score_card.game_over()


    #detecting if player has reach the other side
    if player.is_at_finishline():
        player.goto_start()
        car_manager.car_level_up()
        score_card.increase_level()






screen.exitonclick()