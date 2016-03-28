
require_relative '../fruit-machine/fruit_machine'
require 'rspec'

describe Machine do
  it 'should initialize' do
    machine = Machine.new(2222, 50)
    expect(machine.machine_bank).to eq 2222
    expect(machine.play_cost).to eq 50
  end

  it 'can roll four random slots' do
    machine = Machine.new(2222, 50)
    expect(machine.roll_slots.length).to eq(4)
  end

  it 'can check if all slots are unique' do
    machine = Machine.new(2222, 50)
    expect(machine.unique_set_win?(['black', 'white', 'green', 'yellow'])
          ).to be true
    expect(machine.unique_set_win?(['white', 'white', 'green', 'yellow'])
          ).to be false
  end

  it 'can check if two adjacent slots match' do
    machine = Machine.new(2222, 50)
    expect(machine.adjacent_win?(['black', 'white', 'green', 'yellow'])
          ).to be false
    expect(machine.adjacent_win?(['yellow', 'white', 'green', 'white'])
          ).to be false
    expect(machine.adjacent_win?(['white', 'green', 'green', 'yellow'])
          ).to be true
    expect(machine.adjacent_win?(['green', 'yellow', 'white', 'white'])
          ).to be true
  end
end
