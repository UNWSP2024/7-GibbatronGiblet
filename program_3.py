# Program #3: US_Population
def main():
    value_count = 3
    all_entered_values = []
    rep_number = 1
    for population_list in range(value_count):
        population_list = []
        year = int(input(f"Enter year {rep_number}'s number: "))
        state = input(f"Enter state {rep_number}'s name: ")
        population = int(input(f"Enter population {rep_number}'s value: "))
        population_list.append(year)
        population_list.append(state)
        population_list.append(population)
        all_entered_values.append(population_list)
        rep_number += 1

    print("These are the values you have entered:",all_entered_values)
    year_to_sum = int(input("What year do you want the total population for?"))
    print(f"{year_to_sum}'s population is {sum_population_for_year(all_entered_values, year_to_sum)}.")


def sum_population_for_year(all_entered_values, year_to_sum):
    meta_list = list(all_entered_values)
    total_population = 0
    for item in meta_list:
        if item[0] == year_to_sum:
            total_population += item[2]
    return total_population

if __name__ == "__main__":
    main()

#This program was written on 10/17/25 by Logan Gibson
#Its name is "Adding State Populations"