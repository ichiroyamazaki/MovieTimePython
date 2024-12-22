import collections

movies = collections.deque()
snacks = collections.deque()

i = 0
while i < 3:
    movie = input(f"Enter movie {i+1} of 3: ")
    movies.appendleft(movie)
    i += 1

j = 0
while j < 3:
    snack = input(f"Enter snack {j+1} of 3: ")
    snacks.appendleft(snack)
    j += 1
    
print(f"Movies to watch are: {movies}")
print(f"Snacks available are: {snacks}")
print("Press S each time you finish a snack.")
 

while True:
    finish = input()
    if finish == 'S':
        snacks.popleft()
        if not snacks:
            print("No more snacks.")
            break
    print(f"{snacks}")
