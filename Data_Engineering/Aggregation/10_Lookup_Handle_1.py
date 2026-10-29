
player_dict = {
    "player 1": ['Badge 1', 'Badge 2', 'Badge 4', 'Badge 5'],
    "player 2": ['Badge 5', 'Badge 2', 'Badge 4', 'Badge 6'],
    "player 3": ['Badge 2', 'Badge 4', 'Badge 7']
}

'''
## SQl equivalent ###
/**step 1:  select unique badges from the player tbl)

with unique_badges as
(
Select badge_id,count(*) from player group by 1 having count(*) = 1
),
select 
player_id
from
player p
join
unique_badges b
on
p.badge_id = b.badge_id
;

'''

## In Python ##
badge_count = {}

for badges in player_dict.values():
    for badge in badges:
        badge_count[badge] = badge_count.get(badge, 0) + 1

#print(badge_count)

unique_badges = set()

for key,value in badge_count.items():
    if value == 1:
        unique_badges.add(key)
#print(unique_badges)

player_name = []
for key,value in player_dict.items():
    for badge in value:
        if badge in unique_badges:
            player_name.append({key: badge})
#print(player_name)



# Step 1: Count how many players have each badge
badge_count = {}

for badges in player_dict.values():
    for badge in badges:
        badge_count[badge] = badge_count.get(badge, 0) + 1

#print(badge_count)

# Step 2: Find unique badges for each player
result = {}

for player, badges in player_dict.items():
    result[player] = [badge for badge in badges if badge_count[badge] == 1]

print(result)

#Output: {'player 1': ['Badge 1'], 'player 2': ['Badge 6'], 'player 3': ['Badge 7']}

