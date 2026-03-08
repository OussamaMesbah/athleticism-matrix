import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

comparisons = [
    'Slalom Skiing',
    'Billiards',
    'Marathon Running',
    'Snooker',
    'Golf'
]

print("CASUAL SPORT CHECK:")
print("="*80)
for idx, sport in enumerate(data, 1):
    if sport['name'] in comparisons:
        print(f"\nRank {idx:2d}: {sport['name']}")
        print(f"  Total Score: {sport['total_rank']}")
        print(f"  Top 3 metrics:")
        sorted_scores = sorted(sport['scores'].items(), key=lambda x: x[1], reverse=True)[:3]
        for cat, score in sorted_scores:
            print(f"    {cat:15s}: {score:5.2f}")
