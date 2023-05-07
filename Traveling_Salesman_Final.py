import string
import pygad
import numpy
from random import choice, random

# function_inputs [[src_city][designation_city]]
function_inputs = [[100, 75, 99, 9, 35, 63, 8],
[51, 100, 86, 46, 88, 29, 20],
[50, 5, 100, 16, 28, 35, 28],
[20, 45, 11, 100, 59, 53, 49],
[86, 63, 33, 65, 100, 76, 72],
[36, 53, 89, 31, 21, 100, 52],
[58, 31, 43, 67, 52, 60, 100]]


num_genes = 7
gene_type = int



def fitness(solution, solution_idx):
    start_city = solution[0]
    end_city = solution[num_genes - 1]
    cost = 0

    for i in range(num_genes-1): # calculates the distance between each of the cities. 
        cost = cost - function_inputs[solution[i]-1][solution[i+1]-1]
        

    cost = cost - function_inputs[end_city -1][start_city-1]

    return cost


def on_generation(g): #prints out the time stamps and the best solution per generation
     best,best_fitness,_=g.best_solution()
     pop_fit = g.cal_pop_fitness()
     avg_fitness = round(-1 * sum(pop_fit)/len(pop_fit), 2)


     print("Generation:", g.generations_completed)
     print("Best Individual:", best)
     print("Best Individual's Fitness:", abs(best_fitness))
     print("Population's Average Fitness:", avg_fitness, "\n")



num_generations = 500

gene_space =  [[1],[2,3,4,5,6,7],[2,3,4,5,6,7],[2,3,4,5,6,7],[2,3,4,5,6,7],[2,3,4,5,6,7],[2,3,4,5,6,7]]

num_parents_mating = 20

fitness_function = fitness

parent_selection_type = "sss" #steady-state selection
keep_parents = 1

crossover_type = "single_point"
crossover_probability=0.4
    
mutation_type = "random"
mutation_num_genes = 1

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       gene_space=gene_space,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       crossover_probability=crossover_probability,
                       mutation_type=mutation_type,
                       mutation_num_genes=mutation_num_genes,
                       on_generation=on_generation,
                       allow_duplicate_genes=False, #set to false so we don't revisit cities 
                       sol_per_pop=30,
                       gene_type=gene_type, 
                       stop_criteria="saturate_150")  
ga_instance.run() 






# Start
# Initialize Population
# Calculate fitness
# Repeat (termination criteria is reached)
#      Selection
#      Crossover
#      Mutation (optional)
#      Calculate fitness
#      Find best
# Return best
