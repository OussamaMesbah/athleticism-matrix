import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

target_sports = ['Handball', 'Volleyball', 'Hurling', 'Motocross', 'Curling', 'Competitive Swimming (100m)', 'Billiards', 'Snooker']

print("Updated Rankings:")
print("="*60)
for idx, sport in enumerate(data, 1):
    if sport['name'] in target_sports:
        print(f"Rank {idx}: {sport['name']} - Total Score: {sport['total_rank']}")
