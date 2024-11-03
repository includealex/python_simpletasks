class Player:
    id:int = None
    name:str = ""
    scores:int = 0
    games:list = []

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        return

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores
        return

    def get_mean(self)->float:
        return self.scores/len(self.games)

    def add_single_score(self) -> None:
        self.scores += 1
        return

class Power:
    name:str=""
    cost:int=""

    def __init__(self, name:str, cost: int) -> None:
        self.name = name
        self.cost = cost
    
    def use(self, player: Player) -> None:
        pass

class PhysicalPower(Power):
    count = 0

    def __init__(self, name: str, cost:int, count:int) -> None:
        self.name = name
        self.cost = cost
        self.count = count

    def use(self, pl: Player) -> None:
        if (self.count == 0):
            print(f"{pl.name} cannot use {self.name}")
        else:
            print(f"{pl.name} used {self.name}")
            self.count -= 1

class MagicPower(Power):
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost
    
    def use(self, pl: Player) -> None:
        print(f"{pl.name} used {self.name}")
        pl.add_single_score()
