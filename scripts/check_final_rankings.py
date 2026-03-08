import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

target_sports = [
    'Bouldering', 'Cross-Country Skiing', 'Field Hockey', 
    'Volleyball', 'Triathlon (Ironman)', 'Canoe Slalom',
    'Snooker', 'Billiards', 'Curling'
]

print("CREDIBILITY FIXES - Before/After Rankings:")
print("="*70)
for idx, sport in enumerate(data, 1):
    if sport['name'] in target_sports:
        print(f"Rank {idx:2d}: {sport['name']:30s} Score: {sport['total_rank']}")
