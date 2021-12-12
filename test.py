questions = ["1+1", "2+2", "3+3"]
answers = ["2", "4", "6"]
number=0
correct=0
for running in range(3):
  inp=input("What is "+questions[number]+"? ")
  if(inp==answers[number]):
    print("Correct")
    correct+=1
  else:
    print("Wrong. The answer is "+answers[number])
  number=+1
print("You got "+str(correct)+"/3")
