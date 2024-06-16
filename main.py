global grid
grid = []
mines = 10
size = 10

def initialize():
    global grid
    grid = [["_" for _ in range(size)] for _ in range(size)]
    
def populate_mines():
    def place_mine():
        import random
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        
        if grid[x][y] == "X":
            place_mine()
        else:
            grid[x][y] = "X"
    
    for _ in range(mines):
        place_mine()

def populate_numbers():
    for x in range(size):
        for y in range(size):
            if grid[x][y] == "X":
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if x + dx < 0 or x + dx >= size or y + dy < 0 or y + dy >= size:
                        continue
                    if grid[x + dx][y + dy] == "X":
                        count += 1
            grid[x][y] = count

def print_grid():
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def main():
    global grid
    initialize()
    populate_mines()
    populate_numbers()
    flags = 0
    # While flags < mines, take input
    while flags < mines:
        print_grid()
        cmd = input("Enter your command (<x> <y> [f]): ")
        cmd = cmd.split()
        if len(cmd) < 2 or len(cmd) > 3:
            print("Invalid command")
        elif not cmd[0].isdigit() or not cmd[1].isdigit():
            print("Invalid command")
        elif int(cmd[0]) < 0 or int(cmd[0]) >= size or int(cmd[1]) < 0 or int(cmd[1]) >= size:
            print("Invalid command")
        else:
            y = int(cmd[0])
            x = int(cmd[1])
            print(x,y)
            print(grid[x][y])
            if len(cmd) == 3 and cmd[2] == "f":
                if grid[x][y] == "F":
                    grid[x][y] = "_"
                    flags -= 1
                else:
                    grid[x][y] = "F"
                    flags += 1
            else:
                if grid[x][y] == "X":
                    print("Game Over")
                    break
                else:
                    print("You are safe")
                    
            
    
    print_grid()
    
    
    
main()