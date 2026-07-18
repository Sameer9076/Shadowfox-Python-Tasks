# Initial List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Original List:", justice_league)

# 1. Number of members
print("\n1. Number of Members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After Adding Batgirl and Nightwing:")
print(justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman becomes Leader:")
print(justice_league)

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("\n4. Green Lantern moved between Aquaman and Flash:")
print(justice_league)

# 5. Replace the entire team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("\n5. New Justice League:")
print(justice_league)

# 6. Sort Alphabetically
justice_league.sort()
print("\n6. Sorted Justice League:")
print(justice_league)

print("\nNew Leader:", justice_league[0])