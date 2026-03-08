import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

comparisons = [
    ('Bowling', 'Mountain Biking (XC)'),
    ('Volleyball', 'Beach Volleyball'),
    ('Table Tennis', 'Tennis'),
    ('Snooker', 'Marathon Running'),
    ('Baseball', 'Cricket'),
    ('Rally Racing', 'Rowing')
]

print("ABSURDITY CHECK - Before/After Rankings:")
print("="*70)

# Create lookup
sport_dict = {s['name']: (idx+1, s['total_rank']) for idx, s in enumerate(data)}

for sport_a, sport_b in comparisons:
    rank_a, score_a = sport_dict.get(sport_a, (999, 0))
    rank_b, score_b = sport_dict.get(sport_b, (999, 0))
    
    winner = sport_a if score_a > score_b else sport_b
    diff = abs(score_a - score_b)
    
    print(f"\n{sport_a} vs {sport_b}:")
    print(f"  {sport_a:30s} Rank {rank_a:2d}  Score {score_a:.2f}")
    print(f"  {sport_b:30s} Rank {rank_b:2d}  Score {score_b:.2f}")
    print(f"  Winner: {winner} (+{diff:.2f})")
