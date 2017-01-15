
def get_trans_table(key)
  alphabets = ["A".."Z", "a".."z", "0".."9"].map{|r| r.to_a.join}
  alphabets.map{|ab| [ab, ab[key%ab.size..-1] + ab[0, key%ab.size]]}.
    transpose.map{|a| a.join}
end

if __FILE__ == $0
  for i in 1..26 do
    if ("ykkg".tr *get_trans_table(i)) == "http"
      puts ("ykkg://tg2.ezekveuf.tf.ag/vekvi".tr *get_trans_table(i))
      print("KEY=", i, "\n")
      break
    end
  end
end

