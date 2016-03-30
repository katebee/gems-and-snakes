
require_relative '../fruit-machine/fruit_machine'
require 'rspec'

describe Player do
  it 'should initialize' do
    player = Player.new(100)
    expect(player.wallet_fund).to eq 100
    expect(player.play_credit).to eq 0
  end
end

describe Machine do
  it 'should initialize' do
    machine = Machine.new(2222, 50)
    expect(machine.machine_bank).to eq 2222
    expect(machine.play_cost).to eq 50
  end

  it 'can run a game' do
    machine = Machine.new(2222, 50)
    expect { machine.run }.to output.to_stdout
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

  context 'with a jackpot win condition' do
    it 'can calculate the jackpot when the bank is even' do
      machine = Machine.new(2222, 50)
      result = ['black', 'white', 'green', 'yellow']
      expect(machine.unique_set_win?(result)).to be true
      expect(machine.determine_prize(result)).to eq 1111
      expect(machine.machine_bank).to eq 1111
    end

    it 'can calculate the jackpot when the bank is odd' do
      machine = Machine.new(1111, 50)
      result = ['black', 'white', 'green', 'yellow']
      expect(machine.unique_set_win?(result)).to be true
      expect(machine.determine_prize(result)).to be 555
      expect(machine.machine_bank).to eq 556
    end
  end

  context 'with an adjacent win condition' do
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

  context 'winning with a low machine bank' do
    it 'will credit free plays' do
      machine = Machine.new(110, 50)
      result = ['green', 'yellow', 'white', 'white']
      expect(machine.adjacent_win?(result)).to be true
      expect(machine.determine_prize(result)).to eq 110
      expect(machine.machine_bank).to eq 0
      expect(machine.play_credit).to eq 2
    end
  end

  context 'with a losing combination' do
    it 'will not fufill a win condition or give a prize' do
      machine = Machine.new(2222, 50)
      result = ['black', 'green', 'black', 'green']
      expect(machine.unique_set_win?(result)).to be false
      expect(machine.adjacent_win?(result)).to be false
      expect(machine.determine_prize(result)).to eq 0
      expect(machine.machine_bank).to eq 2222
    end
  end
end
