require 'set'
require './utility.rb'

module HoursesTour
  class Solver
    ALL_POSITIONS = (1..9).map{|i| (1..9).map{|j| [i, j]} }.flatten(1)
    
    def initialize(grid)
      @grid = String.new(grid)
    end

    def can_move?(x1, y1, x2, y2)
      return false if x1 == x2 and y1 == y2
      return true if (x2 - x1).abs <= 1 and (y2 - y1).abs <= 1
      return (x2 - x1).abs == (y2 - y1).abs
    end

    def movable_positions(x, y)
      return ALL_POSITIONS.select{|pos| can_move?(x, y, pos[0], pos[1])}.sort
    end

    def solve_with_backtracking(x, y, k)
      @path << [x, y]
      if k == 9
        @solutions << @path.clone if can_move?(x, y, @path[0][0], @path[0][1])
      else
        movable_positions(x, y).each{|nx, ny|
          if @grid.cell(nx, ny).to_i == k+1
            solve_with_backtracking(nx, ny, k+1)
          end
        }
      end
      @path.pop
    end

    def solve(x, y)
      @path = []
      @solutions = []
      solve_with_backtracking(x, y, 1)
      return @solutions
    end
  end
end
