import json
import os

def check_relations(data):
    violations = []
    
    # helper to find a sport by name
    def get_sport(name):
        for s in data:
            if s['name'] == name:
                return s
        return None

    # Define Pairs of Interest (Invariants)
    # Format: (Sport A, Metric, Comparison, Sport B, Reason)
    rules = [
        # Endurance
        ("Marathon Running", "endurance", ">=", "Soccer", "Professional runners have higher VO2 max than court athletes"),
        ("Triathlon (Ironman)", "endurance", ">=", "Water Polo", "Elite endurance specialists have higher baseline endurance"),
        ("Water Polo", "endurance", ">", "MMA", "Swimming combat is more metabolic than land combat"),
        
        # Strength
        ("Wrestling", "strength", ">", "Soccer", "Grapplers are stronger than pitch players"),
        ("Rugby Union", "strength", ">", "Tennis", "Rugby players require more absolute mass-moving strength"),
        ("Gymnastics (Artistic)", "strength", ">", "Golf", "Gymnasts have immense relative strength"),
        
        # Agility
        ("Squash", "agility", ">=", "Tennis", "Squash court requires more frequent rapid direction changes"),
        ("Badminton", "agility", ">=", "Soccer", "Racket sports have higher frequency redirection"),
        ("Basketball", "agility", ">", "Marathon Running", "Crossover/Dribble agility vs linear running"),
        
        # Nerve (Latency/Steadiness)
        ("F1 Racing", "nerve", ">=", "Marathon Running", "F1 requires faster reaction times (lower ms)"),
        ("Boxing", "nerve", ">", "Archery", "Combat reaction speed (incoming punches) vs static focus"), # This is debatable, but usually Nerve=Reaction in this context
        ("Shooting", "nerve", ">", "Soccer", "Precision steadiness vs team sport jitter"),
        
        # Hand-Eye
        ("Table Tennis", "hand_eye", ">", "Basketball", "Smallest ball, fastest speed relative to distance"),
        ("Baseball", "hand_eye", ">", "Soccer", "Pitch hitting vs foot-eye coordination"),
        ("Tennis", "hand_eye", ">", "Basketball", "High speed racket-ball contact"),
        
        # Power
        ("Football (American)", "power", ">", "Marathon Running", "NFL is explosive, Marathon is not"),
        ("Gymnastics (Artistic)", "power", ">", "Archery", "Tumbling requires explosive power"),
    ]

    for sport_a_name, metric, op, sport_b_name, reason in rules:
        sport_a = get_sport(sport_a_name)
        sport_b = get_sport(sport_b_name)
        
        if not sport_a or not sport_b:
            continue
            
        val_a = sport_a["scores"][metric]
        val_b = sport_b["scores"][metric]
        
        violated = False
        if op == ">" and not (val_a > val_b): violated = True
        if op == ">=" and not (val_a >= val_b): violated = True
        if op == "<" and not (val_a < val_b): violated = True
        if op == "<=" and not (val_a <= val_b): violated = True
        
        if violated:
            violations.append({
                "rule": f"{sport_a_name} {metric} {op} {sport_b_name}",
                "values": f"{val_a} vs {val_b}",
                "reason": reason
            })

    return violations

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'public', 'ranked_sports.json')
    
    with open(data_path, 'r') as f:
        sports = json.load(f)
        
    violations = check_relations(sports)
    
    print(f"Total Violations Found: {len(violations)}")
    for v in violations:
        print(f"FAILED: {v['rule']} ({v['values']}) - {v['reason']}")

if __name__ == "__main__":
    main()
