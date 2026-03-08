import json

with open('public/ranked_sports.json', 'r') as f:
    data = json.load(f)

print("WEIGHTED SCORING RESULTS:")
print("="*80)

# Find key sports
targets = {
    'Marathon Running': None,
    'Snooker': None,
    'Golf': None,
    'Rowing': None,
    'Rally Racing': None
}

for idx, sport in enumerate(data, 1):
    if sport['name'] in targets:
        targets[sport['name']] = (idx, sport['total_rank'], sport['family'])

for name, info in targets.items():
    if info:
        rank, score, family = info
        print(f"Rank {rank:2d}: {name:30s} ({family:15s}) Score: {score:.2f}")

print("\n" + "="*80)
print("The Specialist Curse Check:")
marathon_score = targets['Marathon Running'][1] if targets['Marathon Running'] else 0
snooker_score = targets['Snooker'][1] if targets['Snooker'] else 0
diff = snooker_score - marathon_score

if diff > 0:
    print(f"❌ STILL BROKEN: Snooker beats Marathon by +{diff:.2f}")
else:
    print(f"✅ FIXED: Marathon beats Snooker by +{abs(diff):.2f}")
