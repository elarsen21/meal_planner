# OUTPUTS DAILY, WEEKLY MEAL PLAN
# USE OBJECTS... MEAL, DAY, ETC.
age = 38
height = 72.5
height_cm = height * 2.54
weight = 175
weight_kg = weight * 0.453592
activity = 1.5
bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5  # MIFFLIN-ST. JEOR FORMULA
tdee = bmr * activity

print(f"BMR: {int(bmr)} calories")
print(f"TDEE: {int(tdee)} calories")
# MINIMUM PROTEIN INTAKE
# MINIMUM CARB INTAKE
# MINIMUM FAT INTAKE

percent_bw = -0.006  # RATE OF GAIN / LOSS PER WEEK
# REFINE THIS
rating = ""
if -0.0075 > percent_bw > 0.00333:
    rating = "EASY"
else:
    rating = "HARD"

weekly_rate = percent_bw * weight
cal_adjust = (weekly_rate * 3500) / 7

print(f"\nGAIN/LOSS RATE: {weekly_rate:.2f} lbs. per week")
print(f"DIFFICULTY RATING: {rating}")  # How easy or hard the given rate will be
print(f"CALORIE ADJUSTMENT: {int(cal_adjust)} calories")

pro_per_lb = 0.9

week = {
        "MONDAY" : "Non-",
        "TUESDAY" : "Light", 
        "WEDNESDAY" : "Light",
        "THURSDAY" : "Non-",
        "FRIDAY" : "Light",
        "SATURDAY" : "Non-",
        "SUNDAY" : "Light",
        }

# "Non-training" / "Light" / "Moderate" / "Heavy"
# SEPARATE DAILY ACTIVITY LEVEL AND DAY_TYPE
# "Mildly active" / "Moderately active" / "Heavily active" / "Very heavily active"

protein = weight * pro_per_lb

# SEE PG. 119, TABLE 10.1
for day, day_type in week.items():
    if day_type == "Non-":
        calories = bmr * 1.2 + cal_adjust
        carbs = weight * 0.5
    elif day_type == "Light":
        calories = bmr * 1.375 + cal_adjust
        carbs = weight
    elif day_type == "Moderate":
        calories = bmr * 1.55 + cal_adjust
        carbs = weight * 1.5
    elif day_type == "Heavy":
        calories = bmr * 1.725 + cal_adjust
        carbs = weight * 2.0
    # OUTPUT

    fat = (calories - protein * 4 - carbs * 4) / 9

    p_prc = int((protein * 4 / calories) * 100)
    c_prc = int((carbs * 4 / calories) * 100)
    f_prc = int((fat * 9 / calories) * 100)

    # for day in week:
    print(f"\n{day}:")
    print(f"{day_type} training day")
    print(f"{int(calories)} calories")
    print(f"{int(protein)}g protein ({p_prc}%)")
    print(f"{int(carbs)}g carbs ({c_prc}%)")
    print(f"{int(fat)}g fat ({f_prc}%)")

    num_meals = 5
    # wake_time
    # workout_time
    meal_cals = calories / num_meals
    meal_pro = protein / num_meals
    meal_carbs = carbs / num_meals
    meal_fat = fat / num_meals

    carbo = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    if num_meals == 4 and day_type != "N":
        carbo[1] = 0.25 * carbs
        carbo[2] = 0.35 * carbs
        carbo[3] = 0.15 * carbs
        carbo[4] = 0.25 * carbs
    elif num_meals == 5:
        carbo[1] = 0.20 * carbs
        carbo[2] = 0.30 * carbs
        carbo[3] = 0.15 * carbs
        carbo[4] = 0.15 * carbs
        carbo[5] = 0.20 * carbs
    elif num_meals == 6:
        carbo[1] = 0.18 * carbs
        carbo[2] = 0.25 * carbs
        carbo[3] = 0.13 * carbs
        carbo[4] = 0.13 * carbs
        carbo[5] = 0.13 * carbs
        carbo[6] = 0.18 * carbs

    fatso = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    if num_meals == 4:
        fatso[1] = 0.1 * fat
        fatso[2] = 0.1 * fat
        fatso[3] = 0.3 * fat
        fatso[4] = 0.5 * fat
    elif num_meals == 5:
        fatso[1] = 0.1 * fat
        fatso[2] = 0.1 * fat
        fatso[3] = 0.2 * fat
        fatso[4] = 0.3 * fat
        fatso[5] = 0.3 * fat
    elif num_meals == 6:
        fatso[1] = 0.1 * fat
        fatso[2] = 0.1 * fat
        fatso[3] = 0.2 * fat
        fatso[4] = 0.2 * fat
        fatso[5] = 0.2 * fat
        fatso[6] = 0.2 * fat

    if day_type == "Non-":
        for i in range(1, num_meals + 1):
            print(f"\nMEAL {str(i)}:")
            print(f"{int(meal_pro)}g protein")
            print(f"{int(meal_carbs)}g carbs")
            print(f"{int(meal_fat)}g fat")
            # print(f"{int(meal_cals)} calories")
    else:
        for i in range(1, num_meals + 1):
            print(f"\nMEAL {str(i)}:")
            print(f"{int(meal_pro)}g protein")
            print(f"{int(carbo[i])}g carbs")
            print(f"{int(fatso[i])}g fat")
            # print(f"{int(meal_pro * 4 + carbo[i] * 4 + fatso[i] * 9)} calories")

# "MEAL 1 (AFTER WORKOUT)"

# SHOW GRAMS OF EACH FOOD FOR MEALS, e.g.
""" 
97g chicken breast
137g brown rice
30g salsa verde
150g brocolli
10g extra virgin olive oil
"""

# DROPDOWN TO CHOOSE FROM A LIST OF MEALS
# ALERT IF ANY MICRONUTRIENTS ARE SIGNIFICANTLY OFF

# FILE IO... output text file with all meals for week
with open("daily_meals.txt", "w") as f:
    pass
    # PUT ALL PRINT STATEMENTS IN HERE, OR IN A FUNCTION


# ADJUST MACROS WEEKLY BASED ON BODYWEIGHT CHANGES... see page 140
# END OF WEEK:
# current_cals = calories
# avg_weight = 0
# prev_weight = 0
# wt_delta = avg_weight - prev_weight
# adjust = weekly_rate - wt_delta
# cal_adjust += adjust

# prev_weight = avg_weight

