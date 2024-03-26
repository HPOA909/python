#This program will accept the score as user input
#Then will print the score and letter grade
#Step 1- prompt the user to enter score and save it in a variable
#use int to convert input to a whole number
score = int (input ("Please enter your score: "))

#use if else to calculate the letter grade
#A >= 90
#B >=80
#C >=70
#D >= 60
#Otherwise F


if (score >= 90):
    letterGrade = 'A'
elif (score >= 80):
    letterGrade= 'B'
elif (score >= 70):
    letterGrade= 'C'   
elif (score >= 60):
    letterGrade= 'D'   
else:
    letterGrade='F'
#print the score and the letter grade
#recall that print can take text and variables
print ("Your score is: ", score,"\n Your letter grade is:", letterGrade)

#another way of printing
print ("Your score is {} \n Your letter Grade is {}".format (score,letterGrade))