edited_file = open("twain.txt")

word_count_dictionary = {}
 
for each_line in edited_file:
  stripped_line = each_line.rstrip()
  split_line = stripped_line.split(" ")

  for each_word in split_line:
    # word_count_dictionary[each_word] = word_count_dictionary.get(each_word, 0) + 1
    if word_count_dictionary.get(each_word) is None:
    # if each_word not in word_count_dictionary:
        word_count_dictionary[each_word] = 1
    else:
        word_count_dictionary[each_word] += 1

print word_count_dictionary 



