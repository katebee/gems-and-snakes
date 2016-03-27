
class Machine
  attr_reader :slots, :play_cost
  attr_accessor :machine_bank

  def initialize(machine_bank, play_cost)
    @machine_bank = machine_bank
    @play_cost = play_cost
  end

  def roll_slots
    colours = ['black', 'white', 'green', 'yellow']
    [colours.sample, colours.sample, colours.sample, colours.sample]
  end
end

# ########### GAME START ########### #

if __FILE__ == $PROGRAM_NAME
  machine = Machine.new(222, 22)
  puts machine.roll_slots
end
