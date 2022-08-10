import requests
import random
from config import X_RapidAPI_Key

# url of Exercises DataBase
url = "https://exercisedb.p.rapidapi.com/exercises"
headers = {"X-RapidAPI-Key": X_RapidAPI_Key,
           "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
           }
response = requests.request("GET", url, headers=headers)

# dict of body parts and its muscles
muscles = {'Glutes': ('glutes', 'adductors'),
           'Abs': 'abs',
           'Arms': ('forearms', 'triceps', 'biceps'),
           'Legs': ('hamstrings', 'calves', 'adductors', 'quads'),
           'Delts': 'delts',
           'Chest': 'pectorals',
           'Back': ('traps', 'spine', 'upper back', 'lats')}


# random choice of the number of reps
def generate_exercise_reps():
    set_numbers = [3, 4, 5]
    reps_number = [12, 15, 20, 25]
    sign = "\N{vector or cross product}"
    return f'{random.choice(set_numbers)} {sign} {random.choice(reps_number)}'


# filtering exercises for target body part
def filter_exercises(target_body_part):
    all_exercises = {}
    for item in response.json():
        if target_body_part == 'Full body':
            all_exercises[item['name']] = item["gifUrl"], item['equipment']
        else:
            if item['target'] in muscles[target_body_part]:
                all_exercises[item['name']] = item["gifUrl"], item['equipment']
    return all_exercises


# generate general workout plan
def generate_workout(target_body_part, exercise_number=6):
    workout_dict = {}
    for n in range(int(exercise_number)):
        random_exercise = random.choice(list(filter_exercises(target_body_part)))
        workout_dict[random_exercise] = filter_exercises(target_body_part)[random_exercise]

    workout = [f'*EXERCISE NAME: * {i[0].capitalize()} \n' \
               f'*GIF: * {i[1][0]}\n' \
               f'*Volume: * {generate_exercise_reps()} \n' \
               f'*EQUIPMENT: * {i[1][1]}'for i in workout_dict.items()]
    return workout




