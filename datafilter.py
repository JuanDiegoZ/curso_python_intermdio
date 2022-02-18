from data_staff import data
DATA = data()
def run():

#Exercise en class, used comprehensions.        
    all_python_devs=[worker["name"]for worker in DATA 
                     if worker["language"] =="python"]

#challenge, using filter and map, workers using python.
    all_python_devs_exercise=list(filter(lambda worker
                             :worker['language'] =="python",DATA)) 
    map_phython_devs=list(map(lambda worker_map
                     :worker_map['name'],all_python_devs_exercise ))                         




#Exercise en class, used comprehensions.     
    all_platzi_workers =[worker["name"] for worker in DATA 
                        if worker["organization"] =="Platzi"]


#challenge #2, using filter and map, workers in Platzi.    
    all_platzi_workers_exercise=list(filter(lambda worker
                             :worker['organization'] =="Platzi",DATA))

    platzi_workers=list(map(lambda worker_map
                             :worker_map['name'],all_platzi_workers_exercise))




#Exercise en class, used filter.
    adults =list(filter(lambda worker: worker['age'] >=18 ,DATA))                    

    names_workers =list(map(lambda worker: worker['name'],adults))


#challenge #2, using comprehensions, Workers over 18 years of age .    
    adults_comprehensions=[worker['name'] for worker in DATA 
                          if worker['age'] >= 18]





#Exercise en class, used .
    old_people =list(map(lambda worker: worker 
                | {"old": worker['age'] > 70}, DATA))


#challenge #2, using comprehensions, Workers over 18 years of age.
    old_people_comprehensions=[worker['name'] for worker in DATA 
                          if worker['age'] >= 70]
    
    
    
    
    
    
    
    for worker in old_people_comprehensions:
        
        print(worker)

if __name__ == "__main__":
    run()