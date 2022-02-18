class Agent:
    def __init__(self, name, alive, lives) -> None:
        self._name = name
        self._alive = True
        self._lives = 3

    def alive(self):
        self._alive=True

    def kill(self):
        self._alive=False

    def eat(self, num):
        self._lives += num

    def food(self, item):
        foods = {
            "pancakes": 10,
            "potstickers": 50,
            "broken glass": -5,
            "poison": -50,
            "glass poison":-(self._alive)
        }
        if item in foods:
            self.eat(foods[item])
            if self._lives > 0:
                print(self._name, " died. :(")
        else:
            print("Agent ",self._name," didn't want to eat that...")