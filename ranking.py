class Ranking:
    def __init__(self, id: str, points: int, rate: float, total_games: int, avg_ranking: float, high_points: int, avg_points: int, level: int, current_games_number: int) -> None:
        self.id = id
        self.points = points
        self.rank = 0
        self.rate = rate
        self.total_games = total_games
        self.avg_ranking = avg_ranking
        self.high_points = high_points
        self.avg_points = avg_points
        self.level = level
        self.current_games_number = current_games_number

    def get_id(self) -> str:
        return self.id
    
    def get_rank(self) -> int:
        return self.rank

    def get_points(self) -> int:
        return self.points

    def get_rate(self) -> float:
        return self.rate
    
    def get_total_games(self) -> int:
        return self.total_games
    
    def get_avg_ranking(self) -> float:
        return self.avg_ranking
    
    def get_high_points(self) -> int:
        return self.high_points
    
    def get_avg_points(self) -> int:
        return self.avg_points
    
    def get_level(self) -> int:
        return self.level
    
    def get_current_games_number(self) -> int:
        return self.current_games_number

    def set_rank(self, rank: int) -> None:
        self.rank = rank

    def set_points(self, points: int) -> None:
        self.points = points

    def set_rate(self, rate: float) -> None:
        self.rate = rate

    def set_total_games(self) -> None:
        self.total_games += 1

    def set_avg_ranking(self, avg_ranking: float) -> None:
        self.avg_ranking = avg_ranking

    def set_high_points(self, high_points: int) -> None:
        self.high_points = high_points

    def set_avg_points(self, avg_points: int) -> None:
        self.avg_points = avg_points

    def set_level(self, level: int) -> None:
        self.level = level

    def set_current_games_number(self, current_games_number: int) -> None:
        self.current_games_number = current_games_number