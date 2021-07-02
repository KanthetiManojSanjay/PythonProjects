from abc import ABC, abstractmethod


class GamingConsole(ABC):
    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

class MarioGame(GamingConsole):
    def up(self):
        print('Jump')

    def down(self):
        print('goes into a hole')

    def left(self):
        pass

    def right(self):
        print('Go forward')


class ChessGame(GamingConsole):
    def up(self):
        print('Move piece forward')

    def down(self):
        print('Move piece backward')

    def left(self):
        print('Move piece left')

    def right(self):
        print('Move piece right')

game=MarioGame()
game.up()
game.down()
game.left()
game.right()



