
def get_input(filepath, n):
    #Static Project Input Variables
    input = open(filepath, 'r')
    input_seperated = input.read().split(';')
    return input_seperated[n].split('|')[-1].strip()