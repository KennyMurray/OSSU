#Lecture 6 finger exercise

count = 0
answer = 700
guess = 1000
max_guess = 1000
min_guess = 0
while guess != answer:
    count += 1
    if guess < answer:
        min_guess = guess
    elif guess > answer:
        max_guess = guess
    guess = int((max_guess + min_guess) / 2)

print(f"count: {count}")
print(f"answer: {answer}")