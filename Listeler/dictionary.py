my_fitness_dictionary =  {
  "run":100,
  "swim":200
  }

my_fitness_dictionary["run"]=50
hebele=my_fitness_dictionary["run"]

print(my_fitness_dictionary)

print(hebele)

print(my_fitness_dictionary.get("swim"))## key valueyi verdi

my_fitness_dictionary["dumbell"] = 100

print(my_fitness_dictionary)