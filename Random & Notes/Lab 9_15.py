class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses) if self.wins + self.losses !=0 else 0.0

    # TODO: Define print_standing()
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print('Win percentage: {:.2f}'.format(win_percentage))
        if win_percentage >= 0:
            print('Congratulations, Team {} has a winning average!'.format(self.name))
        else:
            print('Team {} has a lossing average.'.format(self.name))

if __name__ == "__main__":
    team = Team()
   
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()