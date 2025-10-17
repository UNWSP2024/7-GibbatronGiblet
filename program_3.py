# Program #3: US_Population
def main():
    value_count = int(input("How many population values do you want to enter?"))
    master_list = []
    for population_list in range(value_count):
        population_list = []
        year = int(input("Enter year number: "))
        state = input("Enter state name: ")
        population = int(input("Enter population value: "))
        population_list.append(year)
        population_list.append(state)
        population_list.append(population)
        master_list.append(population_list)

    print("These are the values you have entered:",master_list)
    sum_year = int(input("What year do you want the total population for?"))
    print("This year's population is", sum_population_for_year(master_list, sum_year))


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