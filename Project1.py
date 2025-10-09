# SI 201 Project 1
# Your name: Isa Wilson
# Your student id: 8164 2148
# Your email: ifwilson@umich.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# If you worked with generative AI also add a statement for how you used it. 
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

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


def calculate_heaviest_species(penguins): 
    data = {}
    '''
    Grouping the body masses by species and island 
    Input: penguins(list of dictionaries)
    # Output: penguins(list of dictionaries)
    '''
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
    '''
    Finding the averages of each (island, species)
    # Input: csv_file(string)
    Output: list_tups(tuple)
    '''
    list_tups = [] 
    for island, species_dict in data.items(): 
        for species, masses in species_dict.items(): 
            avg_mass = sum(masses) / len(masses)
            list_tups.append((island, species, int(avg_mass)))
    return list_tups

def main(): 
    penguins = load_penguin('penguins.csv')
    result = calculate_heaviest_species(penguins)
    print(result)

if __name__ == "__main__": 
    main() 