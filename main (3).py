class player:
  def play (self):
    print("the player is playing cricket.")

class Batsman (player):
  def play (self):
    print("the Batsman is batting.")

class Bowler (player):
  def play (self):
    print("the Bowler is bowling.")

Batsman = Batsman()
Bowler = Bowler()
Batsman . play()
Bowler . play()
