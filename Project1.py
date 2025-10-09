# SI 201 Project 1
# Your name: Isa Wilson
# Your student id: 8164 2148
# Your email: ifwilson@umich.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# If you worked with generative AI also add a statement for how you used it. 
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code




# Topic question: Is there a correlation between sex and penguin body mass?
# Description: Understand the relation of penguin part size (flipper and beak) to rest of the penguin mass and how it related to sex


import os
import csv 

def load_penguin(csv_file): 
    '''
    Reads the penguin csv file and returns it as a list of dictionaries - coverts keys that have numbered outputs into integers utilizing float to account for decimals
    Input: csv_file(string)
    Output: penguins(list of dictionaries)
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, csv_file)

    penguins = [] 
    numbered_keys = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

    with open(full_path, newline='') as csv_file: 
        reader = csv.DictReader(csv_file)
        for row in reader: 
            for key in numbered_keys: 
                value = row.get(key, '')
                if value.strip() != '': 
                    try: 
                        row[key] = int(float(value))
                    except ValueError: 
                        row[key] = None
                else: 
                    row[key] = None
            penguins.append(row)
    return penguins 

def get_measurements(penguins, measurements): 
    '''
    Creates a list of integer values for measurements
    Input: penguins (list of dictionaries), measurements (string)
    Output: list of integers
    '''
    values = []
    for p in penguins: 
        val = p.get(measurements)
        if val is not None: 
            values.append(val)
    return values


def calculate_average_body_mass_species(penguins): 
    '''
    Grouping the body masses by species and island and finding the averages of each (island, species)
    Input: csv_file(string)
    Output: avg_body_mass_dict(dictionary)
    '''
    
    data = {}
    for row in penguins: 
        island = row['island']
        species = row['species']
        body_mass = row['body_mass_g']
        
        if body_mass is None: 
            continue 
        if island not in data: 
            data[island] = {}
        if species not in data[island]: 
            data[island][species] = [] 

        data[island][species].append(body_mass)

    avg_body_mass_dict = {}
    highest_avg_mass = 0
    heaviest_species_island = None
    for island, species_dict in data.items(): 
        for species, masses in species_dict.items(): 
            avg_mass = sum(masses) / len(masses)
            avg_body_mass_dict[(island, species)] = avg_mass #calculation 1 - calculating the average mass for each species 

            if avg_mass > highest_avg_mass:
                highest_avg_mass = avg_mass #calculation 2 - calculating the highest average mass with associated species 
                heaviest_species_island = (island, species) 
    print(f"The average mass for (island, species) is: {avg_body_mass_dict}")
    print(f"The species with the highest average mass is: {heaviest_species_island} with a mass of {highest_avg_mass:.2f}g") 
    return avg_body_mass_dict, heaviest_species_island, highest_avg_mass

    


def calculate_body_flipper_to_mass_ratio(penguins, avg_body_mass_dict):
    '''
    Calculates the flipper-to-average-mass ratio for each penguin (using the above function avg mass) and then using that output, find the sex with the highest flipper-to-average-mass ratio
    Input: penguins (list of dicts) and avg_body_mass_dict (dictionary)
    Output: penguins_with_ratio and sex_highest_ratio
    '''
    #using above function, calculate flipper-to-average-mass ratio for each penguin (using the above function avg mass) and then using that output, find the sex with the highest flipper-to-average-mass ratio

    # penguins_with_ratio = []
    # highest_ratio = 0
    # sex_highest_ratio = None

    # for row in penguins:
    #     island = row['island']
    #     species = row['species']
    #     body_mass = row['body_mass_g']
    #     flipper_length = row['flipper_length_mm']
    #     sex = row.get('sex')

    pass

def analyze_bill_ratio_mass_relation(penguins, avg_body_mass_dict, sex_highest_ratio): 
    '''
    Analyzes how the average bill-length-depth-mass ratio relates to average body mass across species, island, and sex and compares that to see if its the same sex as highest_ratio (found in calculate_body_ratio)
    Input: penguins (list of dicts), avg_body_mass_dict (dictionary), sex_highest_ratio
    Output: Bill_mass_relation (dictionary), sex_match (boolean)
    '''
    #heres a start on how to approach avg_mass relation calculation
    # bill_ratio = bill_length / bill_depth
    # bill_mass_ratio = bill_ratio / avg_body_mass
    pass

def main(): 
    penguins = load_penguin('penguins.csv')
    calculate_average_body_mass_species(penguins)

if __name__ == "__main__": 
    main() 