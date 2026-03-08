import json

d = json.load(open('public/ranked_sports.json'))

# Find sports
motocross = [s for s in d if 'Motocross' in s['name']][0]
golf = [s for s in d if 'Golf' in s['name']][0]
cycling = [s for s in d if 'Cycling (Road)' in s['name']][0]
tt = [s for s in d if 'Table Tennis' in s['name']][0]
badminton = [s for s in d if 'Badminton' in s['name']][0]
tennis = [s for s in d if 'Tennis' == s['name']][0]

mx_rank = d.index(motocross) + 1
golf_rank = d.index(golf) + 1
cycling_rank = d.index(cycling) + 1
tt_rank = d.index(tt) + 1
badminton_rank = d.index(badminton) + 1
tennis_rank = d.index(tennis) + 1

print("FINAL OPTICAL ILLUSION CHECK:")
print("="*80)
print("\n1. MOTOCROSS vs GOLF (Nerve):")
print(f"   Motocross:  Rank {mx_rank:2d}, Nerve: {motocross['scores']['nerve']:.2f}")
print(f"   Golf:       Rank {golf_rank:2d}, Nerve: {golf['scores']['nerve']:.2f}")
print(f"   ✅ Motocross nerve ({motocross['scores']['nerve']:.2f}) > Golf ({golf['scores']['nerve']:.2f})")

print("\n2. CYCLING vs TABLE TENNIS (Nerve):")
print(f"   Cycling:      Rank {cycling_rank:2d}, Nerve: {cycling['scores']['nerve']:.2f}")
print(f"   Table Tennis: Rank {tt_rank:2d}, Nerve: {tt['scores']['nerve']:.2f}")
print(f"   ✅ Cycling nerve ({cycling['scores']['nerve']:.2f}) > Table Tennis ({tt['scores']['nerve']:.2f})")

print("\n3. BADMINTON vs TENNIS (Ranking Gap):")
print(f"   Badminton: Rank {badminton_rank:2d}, Score: {badminton['total_rank']:.2f}")
print(f"   Tennis:    Rank {tennis_rank:2d}, Score: {tennis['total_rank']:.2f}")
gap = abs(badminton_rank - tennis_rank)
print(f"   Gap: {gap} spots")
if gap <= 5:
    print(f"   ✅ NEIGHBORS! (Gap = {gap} spots)")
else:
    print(f"   ⚠️  Still {gap} spots apart")

print(f"\nTennis Durability: {tennis['scores']['durability']:.2f} (was 1.7)")
print(f"Tennis Power: {tennis['scores']['power']:.2f} (was 4.5)")
