
require_relative '../gems-and-snakes/gems_and_snakes'
require 'rspec'

describe GemsAndSnakes do
  it 'should initialize and have three boxes' do
    game = GemsAndSnakes.new
    expect(game.boxes).to match_array([:gems, :snakes, :snakes])
    expect(game.player_box).to be nil
  end

  it 'can remove a box' do
    game = GemsAndSnakes.new
    expect(game.boxes).to match_array([:gems, :snakes, :snakes])
    game.remove_a_box(1)
    expect(game.player_box).to be :gems
    expect(game.boxes).to match_array([:snakes])
  end
end
