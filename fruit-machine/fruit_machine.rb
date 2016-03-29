
class Player
  attr_accessor :wallet_fund, :play_credit

  def initialize(wallet_fund)
    @wallet_fund = wallet_fund
    @play_credit = 0
  end

  def gamble(machine)
    if (@wallet_fund - machine.play_cost) > 0
      @wallet_fund -= machine.play_cost
      machine.run
    end
  end
end

class Machine
  attr_reader :slots, :play_cost
  attr_accessor :machine_bank

  def initialize(machine_bank, play_cost)
    @machine_bank = machine_bank
    @play_cost = play_cost
  end

  def run
    roll = roll_slots
    puts roll.to_s
  end

  def roll_slots
    colours = ['black', 'white', 'green', 'yellow']
    [colours.sample, colours.sample, colours.sample, colours.sample]
  end

  def unique_set_win?(slots)
    slots.uniq.length == slots.length ? true : false
  end

  def adjacent_win?(slots)
    slots.each_with_index do |slot, index|
      next_slot = slots[index + 1]
      if next_slot.nil?
        return false
      elsif slot == next_slot
        return true
      end
    end
  end
end

# ########### GAME START ########### #

if __FILE__ == $PROGRAM_NAME
  machine = Machine.new(222, 22)
  player = Player.new(100)
  machine.run
end
