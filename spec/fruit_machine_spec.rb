
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
end
