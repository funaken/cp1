require 'set'
require './utility.rb'

module NumberPlace
  class Solver
    ALL_NUMBERS = Set.new(1..9)
    
    def initialize(grid)
      @grid = String.new(grid)
    end

    def list_candidates_column(x)
      ALL_NUMBERS - (1..9).map{|i| @grid.cell(x, i).to_i}
    end

    def list_candidates_row(y)
      ALL_NUMBERS - (1..9).map{|i| @grid.cell(i, y).to_i}
    end

    def list_candidates_box(x, y)
      box_pos_x = ((x - 1) / 3) * 3 + 1
      box_pos_y = ((y - 1) / 3) * 3 + 1
      box_pos = (0..2).map{|i| (0..2).map{|j| [box_pos_x + i, box_pos_y + j]} }.flatten(1)
      ALL_NUMBERS - box_pos.map{|pos| @grid.cell(pos[0], pos[1]).to_i}
    end

    def list_candidates(x, y)
      list_candidates_column(x) & list_candidates_row(y) & list_candidates_box(x, y)
    end

    def solve_simple
      # 候補となる数字が1つしかないコマは確定
      # 各行, 列, ブロックについて、ある数字が入りうるマスが1カ所だけなら確定
    end

    def solve_with_backtracking
      solve_simple()                  # まず、答が確定するところは解き進めます

      next_zero = @grid.index("0")
      return true if next_zero.nil?   # もう0が残っていない＝解答発見

      # 0 のマスに対して、候補を一つずつ仮置きしてみます
      x, y = @grid.index2pos(next_zero)
      list_candidates(x, y).each{|k|
        saved_grid = @grid.clone      # 盤面を保存しておく
        @grid.set_cell(x, y, k)       # 数字を仮置きする

        if solve_with_backtracking()
          return true                 # 答が見つかったら盤面を @grid に残したままで終了
        end

        @grid = saved_grid            # 汚れた盤面を保存した状態に戻す
      }

      return false                    # 答が見つからなかった
    end

    def solve
      solve_with_backtracking()
      return @grid
    end
  end
end
