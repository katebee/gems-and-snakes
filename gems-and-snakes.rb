

def wait_and_space(secs=1)
	puts "..."
	sleep(secs)
end

def input_check()
  player_input = gets.to_i
  if player_input.between?(1, 3)
    return player_input
  else
    puts "Please enter 1, 2 or 3"
    input_check()
  end
end

puts "Welcome to Gems and Snakes!"
cards = [:gems, :snakes, :snakes]

wait_and_space(secs=2)

puts "I have three boxes, one contains gems, the others are full of snakes:"

puts "|Snakes| |Snakes| |Gems|"

cards.shuffle!
puts "The boxes have been shuffled, which one will you pick? (1,2,3)"
 # listen for single key press and check valid

player_choice = input_check() - 1

player_card = cards.delete_at(player_choice)
index_to_discard = cards.index(:snakes)
puts "You have chosen box #{player_choice + 1}"
puts "I have removed one of the other boxes... it was full of snakes"
puts "Would you like to swap you box with the remaining box? (y / N)"

to_swap = gets.chomp.upcase

if (to_swap == "Y")
	player_card = cards[0]
	puts "The boxes have been swapped!"
else
	puts "You will keep your first choice then!"
end

wait_and_space(secs=2)

if (player_card == :snakes)
	puts "Oh no! you open your box and find #{player_card}!"
else
	puts "Hooray! You recieved a box of #{player_card}!"
end
