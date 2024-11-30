while 1:
  print("Enter a math equation (enter q to quit)")
  b = input()
  b = b.replace("^", "**")
  if b == "q":
      exit()
  try: 
      print(eval(b))
  except (SyntaxError, NameError):
    print("Try again, this doesn't work")
