print('Calculate Body Mass Index (BMI)')
mass = float(input('Your mass (kg): '))
height = float(input('Your height (cm): '))/100
BMI = mass/(height**2)
if BMI < 16:
    print('You are severely underweight.')
elif BMI >= 16 and BMI < 18.5:
    print('You are underweight.')
elif BMI >= 18.5 and BMI < 25:
    print('You are normal.')
elif BMI >= 25 and BMI <= 30:
    print('You are overweight.')
else:
    print ('You are obese.')