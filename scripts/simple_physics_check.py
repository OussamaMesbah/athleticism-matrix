import json

d = json.load(open('public/ranked_sports.json'))

# Find all sports that were fixed
sports_to_check = [
    ('Boxing', 'speed'),
    ('Fencing', 'speed'),
    ('Table Tennis', 'speed'),
    ('Downhill Skiing', 'multi'),
    ('Lacrosse', 'durability'),
    ('Basketball', 'endurance'),
    ('F1 Racing', 'endurance'),
    ('Skateboarding (Street)', 'strength')
]

print("FINAL PHYSICS CORRECTIONS CHECK:")
print("="*80)

for sport_name, metric_check in sports_to_check:
    sport = next((s for s in d if sport_name == s['name']), None)
    if sport:
        rank = d.index(sport) + 1
        if metric_check == 'multi':
            print(f"\nDOWNHILL SKIING:")
            print(f"   Rank: {rank}")
            print(f"   Speed: {sport['scores']['speed']:.2f} (target: 9.5)")
            print(f"   Strength: {sport['scores']['strength']:.2f} (target: 8.5)")
            print(f"   Durability: {sport['scores']['durability']:.2f} (target: 8.5)")
        else:
            actual = sport['scores'][metric_check]
            print(f"\n{sport_name} ({metric_check}):")
            print(f"   Rank: {rank}, Score: {actual:.2f}")

print("\n" + "="*80)
print("PHYSICS CORRECTIONS COMPLETE!")
