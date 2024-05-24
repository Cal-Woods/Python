passes = 0
failures = 0
count = 1




number = int(input("How many results do you wish to enter? "))



while count <= number:
    
      result = int(input('Please enter result: '))

      if result >= 50:
          passes = passes + 1

      else:
          failures = failures + 1

      count = count+1

print ('Number of passes: ', passes)

print ('Number of failures: ', failures)

