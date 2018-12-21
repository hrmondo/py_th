attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Jen", "Dave"]
potential_attendees = attendees + optional_invitees

print("There are", len(potential_attendees), "potential attendees currently")