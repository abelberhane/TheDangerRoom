require 'ruby2d'

set background: 'green'
set title: 'Ruby - Reaction Game'

message = Text.new('Test your might! Click to begin!')
game_started = false
square = nil
start_time = nil
duration = nil

on :mouse_down do |event|
  if game_started
    if square.contains?(event.x, event.y)
      duration = ((Time.now - start_time) * 1000).round
      message = Text.new("Well done! It took you: #{duration} milliseconds. Try again!")
      square.remove
      game_started = false
    end
  else
    message.remove
    
    square = Square.new(
      x: rand(get(:width) - 25), y: rand(get(:height) -25),
      size:25,
      color: 'black'
    )

    start_time = Time.now
    game_started = true
  end
end

show