def repeat_stuff(stuff, num_repeats=10):
  return stuff * num_repeats

# create a variable that repeats row, three times and adds your boat
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

# create song variable that repeats lyrics 10 times because no second arguement is give and the number of repeats defaults to 10
song = repeat_stuff(lyrics)

print(song)