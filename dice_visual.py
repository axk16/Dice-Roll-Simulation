import pygal
import sys
import time
from die import Die

dice = []
print("This program will create a simulation of how many times"
      " a number is rolled any number of given sides and number of die.")
print("Enter 'q' to quit.")

while True:
    die_sides = input("\nHow many sides does the die have? ")
    if die_sides == 'q':
        break
    dice.append(int(die_sides))

dice.sort()

number_of_rolls = input("\nHow many times do want to roll each die? ")
if number_of_rolls == 'q':
    sys.exit()
number_of_rolls = int(number_of_rolls)

repeat = input("\nHow many times do want to repeat the test? ")
repeat = int(repeat)

completed_rolls = 0
for test in range(1, repeat+1):
    # Make some rolls, and store results in a list.
    results = []
    result = 0
    for roll_num in range(1, number_of_rolls + 1):
        for die in dice:
            die = Die(die)
            result += die.roll()
            completed_rolls += 1
            print(str(round(completed_rolls / (repeat * number_of_rolls * len(dice))*100, 3)) + "% complete")

        results.append(result)
        result = 0

    # Analyse the results.
    frequencies = []
    max_result = 0

    for die in dice:
        max_result += die

    for value in range(len(dice), max_result + 1): 
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    hist = pygal.Bar()

    if len(dice) == 1:
        hist.title = "Results of rolling a D" + str(dice[-1]) + " die " + str(number_of_rolls) + " times."
    else:
        for die in dice:
            hist.title = "Results of rolling various die " + str(number_of_rolls) + " times."

    hist.x_labels = []
    for num in range(len(dice), max_result + 1):
        hist.x_labels.append(num)

    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    key_label = ''.join("D" + str(die) + " + " for die in dice)
    key_label = key_label[:-3]

    hist.add(key_label, frequencies)
    hist.render_to_file('dice_visual' + str(test) + '.svg')