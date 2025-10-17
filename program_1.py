# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
from operator import index

def main():
    rainfall = get_rainfall()
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)
    least_rainfall = min(rainfall)
    most_rainfall = max(rainfall)
    print(f'The average monthly rainfall was {average_rainfall:.2f} inches.')
    print(f'The lowest monthly rainfall was {least_rainfall:.2f} inches.')
    print(f'The highest monthly rainfall was {most_rainfall:.2f} inches.')

def get_rainfall():
    monthly_rain = []
    for index in range(12):
        rain = float(input(f'What was the rainfall for month {index + 1} in inches?'))
        monthly_rain.append(rain)
        index += 1
    return monthly_rain

if __name__ == '__main__':
    main()


#This program was written on 10/17/25 by Logan Gibson
#Its name is "Improved Rainfall Calculator"