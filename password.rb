require './vigenere.rb'

$oracles = ["block", "means"]

def check_sum(s)
  sum = s.bytes.inject(0){|acc,c| acc += c}
  sum % 26 == 0
end

def analyze_password
  for a in ("A".."Z").to_a
    for b in ("A".."Z").to_a
      for c in ("A".."Z").to_a
        for d in ("A".."Z").to_a
          pass = [a, b, c, d].join
          decoded_text = decode_vigenere($text, pass)
          if check_sum(decoded_text[1..-1])
            if $oracles.all?{|oracle| decoded_text.include?(oracle)}
              return pass
            end
          end
        end
      end
    end
  end
  raise "password not found"
end

$password = analyze_password

