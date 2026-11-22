# Capstone Project: Projectile Game

# Necessary libraries
import math             # To use trigonometry here
import random           # To generate random numbers

# Game settings
gravity = 9.81          # m/s^2
rounds = 5
min_target = 20         # metres
max_target = 150        # metres
max_speed = 60          # m/s
hit_tolerance = 2       # metres

def calculate_range(speed, angle_degrees):
    # Returns how far (in metres) a ball lands on flat ground
    # Formula: range = v^2 * sin(2 * angle) / g
    angle_radians = math.radians(angle_degrees)                     # Convert degrees into radians
    return (speed ** 2) * math.sin(2 * angle_radians) / gravity     # math.sin() only uses radians

def get_number(prompt, minimum, maximum):
    # Keep asking until the user enters a number between min and max
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("That's not a number. Please try again.")
            continue

        if minimum <= value <= maximum:
            return value
        print(f"Please enter a value between {minimum} and {maximum}.")

def get_points(error):
    # Return 0-100 points based on how far the landing was from the target
    if error <= hit_tolerance:
        return 100
    elif error <= 10:
        return 60
    elif error <= 25:
        return 30
    elif error <= 50:
        return 10
    return 0

def get_rating(total):
    # Returns a message depending on the final score
    if total >= 450:
        return "Projectile master!"
    elif total >= 300:
        return "Sharp shooter."
    elif total >= 150:
        return "Getting there."
    return "Keep practising!"

def play_round(round_number):
    # Play 1 round and return a dictionary of results
    target = random.randint(min_target, max_target)         # To generate random target distance
    print(f"\nRound {round_number} of {rounds}")
    print(f"Target distance: {target} m")

    angle = get_number("Launch angle in degrees (1-89): ", 1, 89)
    speed = get_number(f"Launch speed in m/s (1-{max_speed}): ", 1, max_speed)

    landing = calculate_range(speed, angle)
    error = abs(landing - target)                           # abs() prevents negatives; just the magnitude
    points = get_points(error)

    print(f"\nYour ball landed {landing:.1f} m away.")      # 1f is for 1 decimal point
    if error <= hit_tolerance:
        print("Direct hit!")
    elif landing > target:
        print(f"You overshot by {error:.1f} m.")
    else:
        print(f"You fell short by {error:1f} m.")
    print(f"Points this round: {points}")

    return {
        "round": round_number,
        "target": target,
        "landing": landing,
        "error": error,
        "points": points
        }

def show_summary(results):
    # Print a table of every round and return the total score
    print("\nGAME SUMMARY:")
    print(f"{'Round':<7}{'Target':>8}{'Landed':>9}{'Off by':>9}{'Points':>8}")
    # Took some research to make a table. The above has digits to indicate the width of their desired column
    
    total = 0
    best_round = results[0]
    for result in results:
        print(
            f"{result['round']:<7}{result['target']:>8}"
            f"{result['landing']:>9.1f}{result['error']:>9.1f}"
            f"{result['points']:>8}"
            )
        # Learnt that the table only looks right if the print statement encompasses all 3 lines instead of having 3 separate print statements
        total += result["points"]
        if result["error"] < best_round["error"]:
            best_round = result

    print(f"\nTotal score: {total} / {rounds * 100}")
    print(f"Closest shot: round {best_round['round']}")
    print(f"(off by {best_round['error']:.1f} m)")
    print(f"Rating: {get_rating(total)}")
    return total

def ask_play_again():
    # Asks the user whether to play again. Return True or False
    while True:
        answer = input("\nPlay again? (y/n): ".strip().lower())
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please type y or n.")

def main():
    print("Welcome to the Projectile Game!")
    print(f"Hit the target in {rounds} rounds by choosing a launch angle and speed.")
    print("(Air resistance is ignored, and the ground is flat.)")

    high_score = 0
    playing = True

    while playing:
        results = []
        for round_number in range(1, rounds + 1):
            results.append(play_round(round_number))

        total = show_summary(results)
        if total > high_score:
            high_score = total
            print("New high score!")

        playing = ask_play_again()

    print(f"\nThanks for playing! Best score this session: {high_score}")

main()
