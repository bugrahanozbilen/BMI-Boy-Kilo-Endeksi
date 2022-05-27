# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

sol =  round (weight / (height * height))

if sol <= 18.5:
  print(f"Your BMI is {sol}, you are underweight.")
elif sol < 25:
  print(f"Your BMI is {sol}, you have a normal weight.")
elif sol < 30:
  print(f"Your BMI is {sol}, you are slightly overweight.")
elif sol < 35:
  print(f"Your BMI is {sol}, you are obese.")
  
else:
  print(f"Your BMI is {sol}, you are clinically obese.")