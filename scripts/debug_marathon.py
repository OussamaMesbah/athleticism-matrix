import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

# Find Marathon and Snooker
marathon = [s for s in data if 'Marathon' in s['name']][0]
snooker = [s for s in data if 'Snooker' in s['name']][0]

print("MARATHON vs SNOOKER BREAKDOWN:")
print("="*80)
print(f"\nMarathon Running (Rank {data.index(marathon)+1}, Score {marathon['total_rank']}):")
print(f"Family: {marathon['family']}")
for cat, score in sorted(marathon['scores'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat:15s}: {score:5.2f} (raw: {marathon['raw'][cat]})")

print(f"\nSnooker (Rank {data.index(snooker)+1}, Score {snooker['total_rank']}):")
print(f"Family: {snooker['family']}")
for cat, score in sorted(snooker['scores'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat:15s}: {score:5.2f} (raw: {snooker['raw'][cat]})")
