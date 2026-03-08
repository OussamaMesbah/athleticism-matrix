import json

d = json.load(open('public/ranked_sports.json'))

check_sports = {
    'Synchronized Swimming': None,
    'Billiards': None,
    'Marathon Running': None,
    'Curling': None,
    'Cheerleading': None,
    'Darts': None,
    'Parkour': None,
    'Gymnastics (Artistic)': None,
    'Badminton': None
}

for idx, sport in enumerate(d, 1):
    if sport['name'] in check_sports:
        check_sports[sport['name']] = (idx, sport['total_rank'], ', '.join(sport.get('families', [])))

print("FINAL CREDIBILITY CHECK:")
print("="*80)

print("\n1. SYNCHRONIZED SWIMMING vs BILLIARDS:")
for name in ['Synchronized Swimming', 'Billiards']:
    if check_sports[name]:
        rank, score, fam = check_sports[name]
        print(f"   Rank {rank:2d}: {name:30s} Score: {score:.2f}")

print("\n2. MARATHON vs CURLING:")
for name in ['Marathon Running', 'Curling']:
    if check_sports[name]:
        rank, score, fam = check_sports[name]
        print(f"   Rank {rank:2d}: {name:30s} Score: {score:.2f}")

print("\n3. CHEERLEADING vs DARTS:")
for name in ['Cheerleading', 'Darts']:
    if check_sports[name]:
        rank, score, fam = check_sports[name]
        print(f"   Rank {rank:2d}: {name:30s} Score: {score:.2f}")

print("\n4. PARKOUR vs GYMNASTICS:")
for name in ['Parkour', 'Gymnastics (Artistic)']:
    if check_sports[name]:
        rank, score, fam = check_sports[name]
        print(f"   Rank {rank:2d}: {name:30s} Score: {score:.2f}")

print("\n5. BADMINTON SPEED CHECK:")
if check_sports['Badminton']:
    badminton = [s for s in d if s['name'] == 'Badminton'][0]
    rank, score, fam = check_sports['Badminton']
    print(f"   Rank {rank:2d}: Badminton")
    print(f"   Speed score: {badminton['scores']['speed']:.2f}")
    print(f"   Speed raw: {badminton['raw']['speed']}")
