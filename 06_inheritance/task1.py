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

