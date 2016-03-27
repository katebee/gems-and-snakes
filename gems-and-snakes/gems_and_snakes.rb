
class GemsAndSnakes
  attr_reader :player_box, :boxes, :player_choice

  def initialize
    @boxes = [:gems, :snakes, :snakes]
  end

  def run_game
    puts 'Welcome to Gems and Snakes!'
    wait_and_space(1)
    puts 'I have three boxes, one contains gems, the others are full of snakes:'
    puts '|Snakes| |Snakes| |Gems|'
    @boxes.shuffle!
    puts 'The boxes have been shuffled, which one will you pick? (1,2,3)'
    # listen for single key press and check valid
    @player_choice = input_check - 1
    puts "You have chosen box #{@player_choice + 1}"
    remove_a_box
    puts 'I have removed one of the other boxes... it was full of snakes'
    puts 'Would you like to swap you box with the remaining box? (y / N)'
    swap_or_not
    wait_and_space(1)
    win_lose
  end

  def wait_and_space(secs = 1)
    puts '...'
    sleep(secs)
  end

  def input_check
    player_input = gets.to_i
    if player_input.between?(1, 3)
      return player_input
    else
      puts 'Please enter 1, 2 or 3'
      input_check
    end
  end

  def remove_a_box(player_choice)
    @player_box = boxes.delete_at(player_choice - 1)
    index_to_discard = @boxes.index(:snakes)
    @boxes.delete_at(index_to_discard)
  end

  def swap_choice?
    to_swap = gets.chomp.upcase
    to_swap == 'Y' ? true : false
  end

  def swap_or_not
    if swap_choice?
      @player_box = @boxes[0]
      puts 'The boxes have been swapped!'
    else
      puts 'You will keep your first choice then!'
    end
  end

  def win_lose
    if @player_box == :snakes
      puts "Oh no! you open your box and find #{@player_box}!"
    else
      puts "Hooray! You recieved a box of #{@player_box}!"
    end
  end
end

# ########### GAME START ########### #

if __FILE__ == $PROGRAM_NAME
  game = GemsAndSnakes.new
  game.run_game
end
