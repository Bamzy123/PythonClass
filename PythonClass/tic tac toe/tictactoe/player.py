class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def get_move(self):
        movement = {
            1:(0, 0), 2:(0, 1), 3:(0, 2),
            4:(1, 0), 5:(1, 1), 6:(1, 2),
            7:(2, 0), 8:(2, 1), 9:(2, 2)
        }
        while True:
            try:
                move = int(input(f"{self.name} choose position (1-9): "))

                if move in movement:
                    return movement[move]
                else:
                    print("Invalid movement, choose from 1-9.")
            except ValueError:
               print("Invalid movement, choose position from 1-9.")


    def get_token(self):
        return self.token

    def get_name(self):
        return self.name