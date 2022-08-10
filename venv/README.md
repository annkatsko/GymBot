# Telegram bot `FitGymProgram`

![](venv/FitGym.jpg)

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Hello! This projects aims to make a Telegram bot that generates a program with exercises for gym! 

## It hosts on Telegram ---> [http://t.me/Fit_Gym_Bot](http://t.me/Fit_Gym_Bot)

## ✨ Features

#### 1. You can choose a target muscle.

#### 2. You can text a number of exercises you want to get.

#### 3. Bot generates exercise list and sends it. The response includes the name of exercise, an equipment, reps and GIF-image of each excercise. 

## Commands
#### 1. "Tap a body part you want to target":
``Glutes`` ``ABS`` ``Full Body`` ``Arms`` 
``Legs`` ``Delts`` ``Chest`` ``Back``
#### You should tap a target muscle
#### 2. "Text the number of exercises you want to get"
#### You should text a number of exercises

## Used packages and APIs:
* telebot
* requests
* ExerciseDB API (A database API containing 1300+ exercises with body part, target muscle equipment necessary, and a form and follow-through animation.)

    
    

## How to run?

1. clone this thing
2. fill config.py. You need to get Token from Telegram [@BotFather](https://t.me/BotFather) (To set up your own Telegram Bot for FitGymProgram, please check out the ```INSTALLATION_TELEGRAM.md```). You also need API-KEY from [ExerciseDB API](https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/).
3. (optional) create your virtualenv, activate it, etc, e.g.:
    ```
    virtualenv -p python3 venv
    . venv/bin/activate
    ```
4. `pip install -r requirements.txt`
5. run it! `python main.py`
6. Go to Telegram and check out Telegram bot FitGymProgram!