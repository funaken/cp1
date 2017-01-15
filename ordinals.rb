require 'prime'

def analyze_ordinals
  Prime.each.take(23).to_a
end

$ordinals = analyze_ordinals

