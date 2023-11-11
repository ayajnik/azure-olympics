# number of lines in the pattern
lines = 7

# loop over the range of lines
for i in range(lines):
   # if the line number is odd, print an asterisk
   if i % 2 == 0:
       print('*')
   # if the line number is even, print a hash
   else:
       print('#')