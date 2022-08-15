# Needed to randomize food locations
import random
# Needed to access the screen
import curses

# Curses is used to initialize the screen
s = curses.initscr()
# Set the cursor to 0, so it does not show on the screen
curses.curs_set(0)
# Get the height and width from getmax
sh, sw = s.getmaxyx()
# Create a new window using the height, width and starting at top left corner of the screen
w = curses.newwin(sh, sw, 0, 0)
# We allow keyboard inputs
w.keypad(1)
# Refresh the screen every 100 milliseconds
w.timeout(100)

# Snakes initial position and body
snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Food Size and Logic
# Adding the food to the center of the screen
food = [sh/2, sw/2]
# Selecting Pi as the food
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Direction the snake moves when the game starts
key = curses.KEY_RIGHT

# Start an infinite loop for every movement of the snake
while True:
    # Check for what the next key is
    next_key = w.getch()
    # set the next key based on what was entered
    key = key if next_key == -1 else next_key

    # Check if the person has lost the game
    # If the snake touches the top/height of the screen, left/right of the screen or if it touches itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
    # Kill the window and quit the game
        curses.endwin()
        quit()

    # Determine what the new head of the snake will be
    new_head = [snake[0][0], snake[0][1]]

    # Translates the key movements into growing the snake
    if key ==curses.KEY_DOWN:
        new_head[0] += 1
    if key ==curses.KEY_UP:
        new_head[0] -= 1
    if key ==curses.KEY_LEFT:
        new_head[1] -= 1
    if key ==curses.KEY_RIGHT:
        new_head[1] += 1

    # Inserting the new head on the snake body
    snake.insert(0, new_head)

    # Check to see if snake is at the location of the food
    if snake[0] == food:
        # Remove the eaten food
        food = None
        # Whenever there is no food, run the following
        while food is None:
            # Create the new food and set its location randomly
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            # Checks to see if the new food has been added
            food = nf if nf not in snake else None
        # Add the new food once the old food has been eaten
        w.addch(food[0], food[1], curses.ACS_PI)
    # If the snake did not eat the food...
    else:
        # Tail of the snake will come off
        tail = snake.pop()
        # Add a space in place of where the old tail was
        w.addch(int(tail[0]), int(tail[1]), ' ')
    # Add the head of the snake to the screen
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
