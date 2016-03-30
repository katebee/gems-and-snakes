
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
  attr_reader :slots, :play_cost, :play_credit
  attr_accessor :machine_bank

  def initialize(machine_bank, play_cost)
    @machine_bank = machine_bank
    @play_cost = play_cost
    @play_credit = 0
  end

  def run
    roll = roll_slots
    puts roll.to_s
    prize = determine_prize(roll)
    puts "WINNINGS: #{prize}"
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

  def determine_prize(result)
    if unique_set_win?(result)
      prize = @machine_bank / 2
      @machine_bank -= prize
      return prize
    elsif adjacent_win?(result)
      if @machine_bank < @play_cost * 5
        provide_play_credit(@play_cost * 5)
        prize = @machine_bank
        @machine_bank = 0
        return prize
      else
        @machine_bank -= @play_cost * 5
        return @play_cost * 5
      end
    else
      return 0
    end
  end

  def provide_play_credit(target_payout)
    credit = (target_payout - @machine_bank) / @play_cost
    @play_credit += credit
  end
end

# ########### GAME START ########### #

if __FILE__ == $PROGRAM_NAME
  machine = Machine.new(2222, 50)
  player = Player.new(100)

  player.gamble(machine)
end
