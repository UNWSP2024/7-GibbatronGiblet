# Program #3: US_Population
def main():
    value_count = 3
    master_list = []
    for population_list in range(value_count):
        population_list = []
        rep_number = 1
        year = int(input(f"Enter year {rep_number}'s number: "))
        state = input(f"Enter state {rep_number}'s name: ")
        population = int(input(f"Enter population {rep_number}'s value: "))
        population_list.append(year)
        population_list.append(state)
        population_list.append(population)
        master_list.append(population_list)
        rep_number += 1

    print("These are the values you have entered:",master_list)
    sum_year = int(input("What year do you want the total population for?"))
    print(f"This year's population is {sum_population_for_year(master_list, sum_year)}.")


def sum_population_for_year(master_list, sum_year):
    meta_list = list(master_list)
    total_population = 0
    for item in meta_list:
        if item[0] == sum_year:
            total_population += item[2]
    return total_population

if __name__ == "__main__":
    main()

#This program was written on 10/17/25 by Logan Gibson
#Its name is "Adding State Populations"