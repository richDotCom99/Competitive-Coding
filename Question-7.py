def question7(words, maxWidth=16):

  len_list = [len(element) for element in words]
  combined_words = []
  small_box = []
  lengths = []
  output = []
  counter = 0
  for length_index in range(len(len_list)):
    print(counter)
    print(words[length_index])
    if counter + len_list[length_index] <= maxWidth:
      counter += len_list[length_index] + 1
      small_box.append(words[length_index])

    else:
      combined_words.append(small_box)
      small_box = [words[length_index]]
      lengths.append(counter - 1)
      counter = len_list[length_index] + 1

  combined_words.append(small_box)
  lengths.append(counter)
  for line_index in range(len(combined_words)):
    
    if (len(combined_words[line_index]) == 1) or (line_index == (len(combined_words) - 1)):
      word = ' '.join(combined_words[line_index])
      output.append(word.ljust(maxWidth))
      continue
    
    if lengths[line_index] == maxWidth:
      output.append(' '.join(combined_words[line_index]))
      continue
      
    while lengths[line_index] < maxWidth: 
      for mini_index in range(len(combined_words[line_index])-1):
        combined_words[line_index][mini_index] += ' '
        lengths[line_index] += 1
        if lengths[line_index] == maxWidth:
          output.append(' '.join(combined_words[line_index]))
          break 
  return output
    

