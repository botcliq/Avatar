def move_disk(from_pole, to_pole):
    print("Moving Disk from pole",from_pole," to ",to_pole )

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height-1,from_pole, with_pole, to_pole)
        move_disk(from_pole,to_pole)
        move_tower(height -1, with_pole, to_pole, from_pole)


print move_tower(3, "A", "B", "C")