# Classes and functions will be defined here.

class Card(object):
    """Cards are either Weapons, Rooms, or Suspects.
    they are held in your hand, a computer player's hand,
    or in the casefile."""

    hand = None

    def __init__(self, name, cluetype):
        self.name = name
        self.cluetype = cluetype

class Player(object):

    """ Players are either computer players or the user.
    They have a location (they are present in a room in the
    mansion). They have cards in their hands."""

    def __init__(self):
        pass

class Room(object):

    """Players move around the mansion as play progresses"""

    passage = None
    
    def __init__(self, name):
        self.name = name



class Move(object):

    """Moves will consist of 'rolling', moving to a new
    location, making a guess, and being shown a card by
    the other players."""

    def __init__(self):
        pass
