require './utility.rb'
require './second_page.rb'

def isalpha(str)
  !str.match(/[^A-Za-z]/)
end

def encode_vigenere_one(c, p)
  if isalpha(c.chr) == false
    return c
  end
  p2 = p - 'A'.ord
  base = 'a'.ord <= c ? 'a'.ord : 'A'.ord
  base + ((c - base + p2) % 26)
end

def decode_vigenere_one(c, p)
  if isalpha(c.chr) == false
    return c
  end
  p2 = p - 'A'.ord
  base = 'a'.ord <= c ? 'a'.ord : 'A'.ord
  base + ((c - base - p2) % 26)
end

def encode_vigenere(code, pass)
  idx = 0
  ret = code.bytes.inject([]) do |arr, c|
    arr << encode_vigenere_one(c, pass.bytes[idx])
    idx = (idx + 1) % pass.size
    arr
  end
  ret.pack("C*")
end

def decode_vigenere(code, pass)
  idx = 0
  ret = code.bytes.inject([]) do |arr, c|
    d = decode_vigenere_one(c, pass.bytes[idx])
    arr << d
    idx = (idx + 1) % pass.size
    arr
  end
  ret.pack("C*")
end

