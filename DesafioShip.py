class Crew:
    def __init__(self, name, age, code):
        self.age = age
        self.code = code
        self.name = name
        
class Ship:
    def __init__(self, total_crew, limit_crew):
        self.total_crew = total_crew
        self.limit_crew = limit_crew
        self.hash_table = {}
        self.on_board = {}

    def calc_hash(self, crew):
        return str(crew.code)
    
    def on_board_ship(self, crew):
        if(str(crew.code) in self.on_board):
            return str(crew.code)
        
        return None
    
    def insert(self, crew):
        if(len(self.hash_table) < self.total_crew):
            key = self.calc_hash(crew)
            self.hash_table[key] = crew
        else:
            print("\nTripulação cheia")
        
    def to_board(self, crew):
        key = self.calc_hash(crew)
        if(key in self.hash_table):
            if(len(self.on_board) < self.limit_crew):
                self.on_board[key] = crew
            else:
                print("\nNavio cheio")
        else:
            print(f'\nTripulante[{crew.code}] não está cadastrado na tripulação')
        
        
    def clear_board(self):
        self.on_board = {}
        
    def search_crew(self, crew):
        key = self.on_board_ship(crew)
        if(key):
            print(f"\nTripulante [{key}]: \nNome: {self.hash_table[key].name} \nIdade: {self.hash_table[key].age} \nCódigo: {self.hash_table[key].code} ")
   
    def read_crew(self):
       for i in range(1, len(self.on_board)+1):
           print(f"\nTripulante [{i}]: \nNome: {self.hash_table[str(i)].name} \nIdade: {self.hash_table[str(i)].age} \nCódigo: {self.hash_table[str(i)].code} \n")
           
    
ship = Ship(2, 2)

crew1 = Crew("Breno", "21", 1)
crew2 = Crew("Breno", "21", 2)
crew3 = Crew("Breno", "21", 3)

ship.insert(crew1)
ship.insert(crew2)
ship.insert(crew3)


ship.to_board(crew1)
ship.to_board(crew3)

ship.read_crew()

ship.search_crew(crew1)


    
    

       