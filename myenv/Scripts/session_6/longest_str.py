def longest_str(str1,str2):
  
  longest_str = ""
  for i in range (len(str1)):

    for j in range (i,len(str1)):
      sub_str = str1[i:j+1]
      if sub_str in str2:
        if len(longest_str) < len(sub_str):
          longest_str = sub_str
          
  return longest_str  