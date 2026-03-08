import json

d = json.load(open('public/ranked_sports.json'))
marathon = [s for s in d if 'Marathon' in s['name']][0]
rank = d.index(marathon) + 1
print(f"Marathon Running:")
print(f"  Rank: {rank}")
print(f"  Score: {marathon['total_rank']}")
print(f"  Families: {', '.join(marathon['families'])}")
print(f"\n  Top scores:")
for k, v in sorted(marathon['scores'].items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"    {k}: {v}")
