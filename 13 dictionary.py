# Dictionary level 1
# dictionary of string and list

# movies = {
#     "3 Idiots":{
#         "year": 2009,
#         "cast":["amir khan", "R. Madhavan", "sharman joshi ","kaeena kapoor"]
#     },
#     "Bahubali":{
#         "year":2015,
#         "cast":["prabhas", "rana daggubati", "anushka shetty", "tamannah"]
#     },
    
#     "Dangal":{
#         "year": 2016,
#         "cast":["amir khan", "sakshi tanwar", "fatima", "sana shaikh", "sanya malhotra"]
#     }
# }

# # Task 1
# # Print the first actor of Dangal using indexing
# print(movies["Dangal"]["cast"][0])

# # Print the first actor of Dangal using .get method
# l = movies.get("Dangal").get("cast")
# print(l[0])

# # Print the first actor of Dangal using index slicing
# print(movies.get("Dangal").get("cast")[0][5])


# Task 2
# print(movies.items())

# for movie in movies:
#     print("Movie:", movies)
#     print("Cast:------>",movies[movie]["cast"])
#     print()

# for movie, actors in movies.items():
#     print(f"{movie} ----->")
#     for actor in actors["cast ----->"[0]]:
#         print(f"{actor},")
#     print()

# for movie, details in movies.items():
#     print(f"{movie} ----->")
#     for actor in details["cast"]:
#         print(f"cast names ----->")
#         parts = actor.strip().split()
#         first_name = parts[0] if len(parts) > 0 else ""
#         last_name = parts[1] if len(parts) > 1 else "N/A"
#         print(f"first name\n{first_name}")
#         print(f"last name\n{last_name}")
#         print()


# for k, v in movies.items():
#     print(k, "----->")
#     for a in v["cast"]: 
#         print("\t", a)
#     print("----" * 20)   


# for k, v in movies.items():
#     print(k, "----->")
#     for a in v["cast"]: 
#         print("\t", a)
#         for nm in a.split():
#             print("\t\t", nm)
#             for ch in nm:
#                 print("\t\t\t", ch)
#     print("--" * 20) 

# div_a = {
#     1:{"name":"Jay","sub":["maths","phy","chem"],"marks":[90,80,70]},
#     2:{"name":"viay","sub":["maths","phy","chem"],"marks":[80,75,60]},
#     3:{"name":"rahul","sub":["maths","phy","chem"],"marks":[70,65,50]}
# }
# div_b = {
#     1:{"name":"om","sub":["maths","phy","chem"],"marks":[66,80,70]},
#     2:{"name":"sanjay","sub":["maths","phy","chem"],"marks":[80,55,60]},
#     3:{"name":"nayan","sub":["maths","phy","chem"],"marks":[70,65,67]}
# }

# print("Roll no.:",1,"Name is :",div_a[1]["name"],"and marks is :",sum(div_a[1]["marks"])/len(div_a[1]["marks"]))
# print("Roll no.:",2,"Name is :",div_a[2]["name"],"and marks is :",sum(div_a[2]["marks"])/len(div_a[2]["marks"]))
# print("Roll no.:",3,"Name is :",div_a[3]["name"],"and marks is :",sum(div_a[3]["marks"])/len(div_a[3]["marks"]))


# print("Average of jay:",sum(div_a[1]["marks"])/len(div_a[1]["marks"]))
# print("Average of viay:",sum(div_a[2]["marks"])/len(div_a[2]["marks"]))
# print("Average of rahul:",sum(div_a[3]["marks"])/len(div_a[3]["marks"]))


MI = [
    {"jn": 45, "p_name": "Rohit Sharma", "runs": 5656, "wickets": 29, "t_name": "Mumbai Indians"},
    {"jn": 18, "p_name": "Suryakumar Yadav", "runs": 4567, "wickets": 12, "t_name": "Mumbai Indians"},
    {"jn": 9, "p_name": "Jasprit Bumrah", "runs": 1234, "wickets": 150, "t_name": "Mumbai Indians"}
]

CSK = [
    {"jn": 7, "p_name": "MS Dhoni", "runs": 4567, "wickets": 0, "t_name": "Chennai Super Kings"},
    {"jn": 8, "p_name": "Ravindra Jadeja", "runs": 3456, "wickets": 155, "t_name": "Chennai Super Kings"},
    {"jn": 17, "p_name": "Deepak Chahar", "runs": 500, "wickets": 70, "t_name": "Chennai Super Kings"}
]

RCB = [
    {"jn": 18, "p_name": "Virat Kohli", "runs": 7263, "wickets": 4, "t_name": "Royal Challengers Bangalore"},
    {"jn": 32, "p_name": "Glenn Maxwell", "runs": 2719, "wickets": 31, "t_name": "Royal Challengers Bangalore"},
    {"jn": 73, "p_name": "Mohammed Siraj", "runs": 108, "wickets": 78, "t_name": "Royal Challengers Bangalore"}
]

GT = [
    {"jn": 33, "p_name": "Hardik Pandya", "runs": 2309, "wickets": 53, "t_name": "Gujarat Titans"},
    {"jn": 19, "p_name": "Rashid Khan", "runs": 443, "wickets": 139, "t_name": "Gujarat Titans"},
    {"jn": 7, "p_name": "Shubman Gill", "runs": 2790, "wickets": 0, "t_name": "Gujarat Titans"}
]

IPL_t20_db = {"MI": MI, "CSK": CSK, "RCB": RCB, "GT": GT}

print("--- Average Runs per Team ---")

for team_code, players in IPL_t20_db.items():
    total_runs = 0
    player_count = len(players)
    
    for player in players:
        total_runs += player["runs"]
    
    avg = total_runs / player_count
    print(f"{team_code}: {avg:.2f} runs per player")


top_batsman = {"p_name": "", "runs": 0}
top_bowler = {"p_name": "", "wickets": 0}

for team in IPL_t20_db.values():
    for player in team:
        # Check for runs
        if player["runs"] > top_batsman["runs"]:
            top_batsman = player
        
        # Check for wickets
        if player["wickets"] > top_bowler["wickets"]:
            top_bowler = player

print(f"Tournament Orange Cap: {top_batsman['p_name']} ({top_batsman['runs']} runs)")
print(f"Tournament Purple Cap: {top_bowler['p_name']} ({top_bowler['wickets']} wickets)")

best_all_rounder = None
highest_score = 0

for team_code, players in IPL_t20_db.items():
    for p in players:
        # Calculate a combined performance score
        current_score = p["runs"] + (p["wickets"] * 20)
        
        if current_score > highest_score:
            highest_score = current_score
            best_all_rounder = p

print(f"MVP (All-Rounder): {best_all_rounder['p_name']} from {best_all_rounder['t_name']}")
print(f"Calculated Score: {highest_score}")