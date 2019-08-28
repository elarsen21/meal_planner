# TODO: Use objects... 
# Meal, Day, Week (output day files, weekly review), Plan (average weight vs. desired gain rate) etc.
# Check against template spreadsheets

# TODO: Take inputs from the command line
age = 38
height = 72.5
height_cm = height * 2.54
weight = 175
weight_kg = weight * 0.453592
activity = 1.5
# Mifflin-St. Jeor formula:
bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5  
tdee = bmr * activity

plan_out = ""

plan_out += "WEEKLY PLAN:"
plan_out += f"\n\nBMR: {int(bmr)} calories"
plan_out += f"\nTDEE: {int(tdee)} calories"
# Show minimum protein intake?
# Show minimum carb intake?
# Show minimum fat intake?

percent_bw = -0.006  # Rate of gain / loss per week
# Refine rating with explanation
rating = ""
if -0.0075 > percent_bw > 0.00333:
    rating = "EASY"
else:
    rating = "HARD"

weekly_rate = percent_bw * weight
cal_adjust = (weekly_rate * 3500) / 7

plan_out += f"\n\nGAIN/LOSS RATE: {weekly_rate:.2f} lbs. per week"
plan_out += f"\nDIFFICULTY RATING: {rating}"  
plan_out += f"\nCALORIE ADJUSTMENT: {int(cal_adjust)} calories"

# see pg. 29
pro_per_lb = 0.9

proteins = {
    "chicken breast": 3.24,
    "casein powder": 1.2,
    "Greek yogurt": 10.32,
    "ground beef": 0.593}
carbos = {"brown rice": 3.91, "sweet potato": 4.83}
sauce = ["salsa verde", "hot salsa", "buffalo sauce"]
vegs = ["spinach", "brocolli", "green beans", "bell peppers"]
fats = {
    "avocado": 6.49,
    "almond butter": 1.8,
    "almonds": 2,
    "walnuts": 1.43,
    "extra virgin olive oil": 1}
seasoning = ["chile lime", "curry powder", "lemon pepper", "chipotle", "bagel", "onion salt"]

# Same meals each day:
meals = [["chicken breast", "sweet potato", "no", "spinach", "almond butter", "curry powder"],
        ["chicken breast", "brown rice", "salsa verde", "brocolli", "extra virgin olive oil", "lemon pepper"],
        ["chicken breast", "sweet potato", "hot salsa", "green beans", "walnuts", "onion salt"],
        ["chicken breast", "brown rice", "no", "bell peppers", "extra virgin olive oil", "chile lime"],
        ["casein powder", "brown rice", "no", "no", "almond butter", "bagel"]]

week = {
    "MONDAY": "Non-",
    "TUESDAY": "Light",
    "WEDNESDAY": "Light",
    "THURSDAY": "Non-",
    "FRIDAY": "Light",
    "SATURDAY": "Non-",
    "SUNDAY": "Light",
}

# TODO: Add daily activity level
# "Mildly active" / "Moderately active" / "Heavily active" / "Very heavily active"

protein = weight * pro_per_lb

# see pg. 119, Table 10.1
for day, day_type in week.items():

    output = ""

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

    fat = (calories - protein * 4 - carbs * 4) / 9

    p_prc = int((protein * 4 / calories) * 100)
    c_prc = int((carbs * 4 / calories) * 100)
    f_prc = int((fat * 9 / calories) * 100)

    plan_out += f"\n\n{day}:"
    plan_out += f"\n{day_type} lifting day"
    # output += f"\n{act_level} activity level"
    # output += f"\n{int(calories)} calories"
    plan_out += f"\n{int(protein)}g protein ({p_prc}%)"
    plan_out += f"\n{int(carbs)}g carbs ({c_prc}%)"
    plan_out += f"\n{int(fat)}g fat ({f_prc}%)"

    num_meals = 5
    # wake_time
    # sleep_time
    # workout_time
    meal_cals = calories / num_meals
    meal_pro = protein / num_meals
    meal_carbs = carbs / num_meals
    meal_fat = fat / num_meals

    carbo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # TODO: Add workout time scenarios
    if num_meals == 4 and day_type != "N":
        carbo[1] = 0.35 * carbs
        carbo[2] = 0.25 * carbs
        carbo[3] = 0.15 * carbs
        carbo[4] = 0.25 * carbs
    elif num_meals == 5:
        carbo[1] = 0.30 * carbs
        carbo[2] = 0.20 * carbs
        carbo[3] = 0.15 * carbs
        carbo[4] = 0.15 * carbs
        carbo[5] = 0.20 * carbs
    elif num_meals == 6:
        carbo[1] = 0.25 * carbs
        carbo[2] = 0.18 * carbs
        carbo[3] = 0.13 * carbs
        carbo[4] = 0.13 * carbs
        carbo[5] = 0.13 * carbs
        carbo[6] = 0.18 * carbs

    fatso = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

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

    output += f"{day}:"

    if day_type == "Non-":
        for i in range(num_meals):
            plan_out += f"\n\nMEAL {str(i + 1)}:"
            plan_out += f"\n{int(meal_pro)}g protein"
            plan_out += f"\n{int(meal_carbs)}g carbs"
            plan_out += f"\n{int(meal_fat)}g fat"
            # print(f"{int(meal_cals)} calories")

            output += f"\n\nMEAL {str(i + 1)}:"
            output += f"\n\n{int(meal_pro * proteins[meals[i][0]])}g {meals[i][0]}"
            output += f"\n{int(meal_carbs * carbos[meals[i][1]])}g {meals[i][1]}"
            output += f"\n{int(meal_fat * fats[meals[i][-2]])}g {meals[i][-2]}"

    else:
        for i in range(num_meals):
            plan_out += f"\n\nMEAL {str(i + 1)}:"
            plan_out += f"\n{int(meal_pro)}g protein"
            plan_out += f"\n{int(carbo[i + 1])}g carbs"
            plan_out += f"\n{int(fatso[i + 1])}g fat"
            # print(f"{int(meal_pro * 4 + carbo[i] * 4 + fatso[i] * 9)} calories")

            output += f"\n\nMEAL {str(i + 1)}:"
            output += f"\n\n{int(meal_pro * proteins[meals[i][0]])}g {meals[i][0]}"
            output += f"\n{int(carbo[i + 1] * carbos[meals[i][1]])}g {meals[i][1]}"
            output += f"\n{int(fatso[i + 1] * fats[meals[i][-2]])}g {meals[i][-2]}"

    with open(f"{day}.txt", "w") as f:
        f.write(output)

# "MEAL 1 (AFTER WORKOUT)"

# https://realpython.com/pdf-python/
with open("weekly_plan.txt", "w") as f:
    f.write(plan_out)

endOfWeek = False

# TODO: Weekly update
# Adjust macros weekly based on bodyweight changes... see page 140
if endOfWeek:
    avg_weight = input("Average weight this week: ")
    wt_delta = avg_weight - prev_weight
    adjust = weekly_rate - wt_delta
    cal_adjust += adjust
    prev_weight = avg_weight
    # new_week()

# TODO: Menu option to end plan

# Webapp: dropdowns to select options

