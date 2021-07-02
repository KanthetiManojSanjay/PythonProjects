class MarioGame:
    def up(self):
        print('Jump')

    def down(self):
        print('goes into a hole')

    def left(self):
        pass

    def right(self):
        print('Go forward')


class ChessGame:
    def up(self):
        print('Move piece forward')

    def down(self):
        print('Move piece backward')

    def left(self):
        print('Move piece left')

    def right(self):
        print('Move piece right')

# in python no need to have common interface for polymorphisim like in java
games = [MarioGame(), ChessGame()]

for game1 in games:
    game1.up()
    game1.down()
    game1.left()
    game1.right()
