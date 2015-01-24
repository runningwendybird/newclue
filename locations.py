from clue_class import Room

# create locations (Rooms).

room_hall = Room("Hall")
room_library = Room("Library")
room_dining = Room("Dining Room")
room_conservatory = Room("Conservatory")
room_billiard = Room("Billiard")
room_lounge = Room("Lounge")
room_study = Room("Study")
room_kitchen = Room("Kitchen")
room_ball = Room("Ballroom")

# Define passageway

room_kitchen.passage = room_study
room_study.passage = room_kitchen
room_lounge.passage = room_conservatory
room_conservatory.passage = room_lounge
