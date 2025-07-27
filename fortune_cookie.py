import random

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 10)
fortune_text = ''

if fortune_number == 1:
    fortune_text = "You will have a great day!"
elif fortune_number == 2:
    fortune_text = "Today will be tough... but worth it."
elif fortune_number == 3:
    fortune_text = "An unexpected opportunity will come your way."
elif fortune_number == 4:
    fortune_text = "Take a break — your mind needs rest."
elif fortune_number == 5:
    fortune_text = "Someone will appreciate your kindness today."
elif fortune_number == 6:
    fortune_text = "Keep pushing — success is closer than it seems."
elif fortune_number == 7:
    fortune_text = "Trust your instincts; they won’t fail you today."
elif fortune_number == 8:
    fortune_text = "A small risk will lead to a big reward."
elif fortune_number == 9:
    fortune_text = "Avoid drama — peace is your power today."
else:
    fortune_text = "Not your lucky day, keep it together."

print(f'{fortune_text} Your lucky number is: {lucky_number}')
