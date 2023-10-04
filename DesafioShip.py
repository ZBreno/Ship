class Crew:
    def __init__(self, name, age, cpf):
        self.age = age
        self.cpf = cpf
        self.name = name
        
class Ship:
    def __init__(self, total_crew, limit_crew):
        self.total_crew = total_crew
        self.limit_crew = limit_crew
        self.crew_on_board = 0
        self.crew_members = 0
        self.hash_table = [-1, -1,- 1, -1, -1, -1, -1, -1, -1, -1]
        self.on_board = [-1, -1,- 1, -1, -1, -1, -1, -1, -1, -1]
        
        

    def calc_hash(self, crew):
        return int(crew.cpf[-1])
    
    def insert(self, crew):
        key = self.calc_hash(crew)
        if(self.crew_members < self.total_crew):
            self.crew_members += 1
            if(self.hash_table[key] == -1):
                self.hash_table[key] = crew
            else:
                self.treat_collision(crew)
        else:
            print('Tripulação atingiu o tamanho máximo')
        
    def treat_collision(self, crew, on_board=False):
        hash_table = self.on_board if on_board else self.hash_table
        key = self.calc_hash(crew)
        
        if(hash_table[key]):
            if(type(hash_table[key]) is list):
                hash_table[key].append(crew)
            else:
                hash_table[key] = [crew]
        else:
            hash_table[key] = crew
        
        
    def to_board(self, crew):        
        if(self.crew_on_board < self.limit_crew):
            self.crew_on_board += 1
            key = self.calc_hash(crew)
            if(self.hash_table[key] == -1):
                self.hash_table[key] = crew
            else:
                self.treat_collision(crew, True)
           
        else:
            print(f'\nTripulação[{crew.name}] para o embarco atingiu o tamanho máximo')
        
        
    def clear_board(self):
        self.on_board = []
        
    def search_crew(self, crew):
        
        key = self.calc_hash(crew)
        if(type(self.on_board[key]) is list):
            for i in self.on_board[key]:
                if(i == crew):
                    print(f"\nTripulante [{key}]: \nNome: {crew.name} \nIdade: {crew.age} \nCPF: {crew.cpf} ")
                    return True
        else:

            if (self.on_board[key] != -1):
                print(f"\nTripulante [{key}]: \nNome: {self.on_board[key].name} \nIdade: {self.on_board[key].age} \nCPF: {self.on_board[key].cpf} ")
                
                return True
            
        print('\nTripulante não está embarcado')
        return False
        
        
            
   
    def read_crew(self):
       for crew in self.on_board:
            if(type(crew) != int):
                if(type(crew) is list):
                    for i in crew:
                        print(f"\nTripulante [{self.calc_hash(i)}]: \nNome: {i.name} \nIdade: {i.age} \nCPF: {i.cpf} ")

                else:
        
                    print(f"\nTripulante [{self.calc_hash(crew)}]: \nNome: {crew.name} \nIdade: {crew.age} \nCPF: {crew.cpf} ")

ship = Ship(250, 50)

crew1 = Crew("Breno", "21","12350858480")
crew2 = Crew("Breno", "21","12350858481")
crew3 = Crew("Bren1o", "25","12350858480")

ship.insert(crew1)
ship.insert(crew2)
ship.insert(crew3)


ship.to_board(crew1)
ship.to_board(crew2)
ship.read_crew()
print('-'*50)
ship.search_crew(crew1)
ship.search_crew(crew2)
ship.search_crew(crew3)
print('-'*50)



    
    

       