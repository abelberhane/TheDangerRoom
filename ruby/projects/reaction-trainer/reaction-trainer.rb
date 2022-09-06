# Implement the ruby GUI
require 'ruby2d'

# Setting Game Background and Game Title
set background: 'green'
set title: 'Ruby - Reaction Game'

# Setting the Game Starting Point. Everything is set to wait to 0 and the game has not yet started. 
message = Text.new('Test your might! Click to begin!')
game_started = false
square = nil
start_time = nil
duration = nil

# Game Logic
# On the press down of the mouse
on :mouse_down do |event|
  # Logic if the game has already started
  if game_started
    # If the mouse hit the location of where the target is
    if square.contains?(event.x, event.y)
      # Record the time to duration
      duration = ((Time.now - start_time) * 1000).round
      # generate the message with how long it took
      message = Text.new("Well done! It took you: #{duration} milliseconds. Try again!")
      # Remove the target
      square.remove
      # Set the game to its starting position
      game_started = false
    end
  else
    # Remove the start the game message
    message.remove
    
    # Target Logic
    # Generate the target randomly, set its size and color
    square = Square.new(
      x: rand(get(:width) - 25), y: rand(get(:height) -25),
      size:25,
      color: 'black'
    )

    # Start the timer and game
    start_time = Time.now
    game_started = true
  end
end

show
