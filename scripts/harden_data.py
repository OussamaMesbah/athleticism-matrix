import json
import os

def harden_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_path = os.path.join(base_dir, 'data', 'sports_raw.json')
    
    with open(raw_path, 'r') as f:
        sports = json.load(f)

    # Scientific Anchors (Hard Data + USER Sanity Fixes)
    anchors = {
        "MMA": {"endurance": 70, "power": 42, "durability": 150, "hand_eye": 170, "agility": 4.1, "nerve": 110},
        "Muay Thai": {"durability": 130, "endurance": 72, "nerve": 110, "hand_eye": 160},
        "Rugby Union": {"durability": 120, "strength": 2.6, "endurance": 67, "agility": 7.23, "nerve": 150},
        "Soccer": {"endurance": 75, "power": 28, "durability": 83, "agility": 6.8, "hand_eye": 210, "nerve": 240},
        "Gymnastics (Artistic)": {"flexibility": 28, "power": 45, "strength": 2.8, "agility": 4.0, "durability": 128},
        "Marathon Running": {"endurance": 101, "power": 18, "durability": 90, "hand_eye": 350, "flexibility": 10, "speed": 4.8, "nerve": 155, "strength": 1.3}, # mental toughness to not quit + joint destruction
        "Triathlon (Ironman)": {"endurance": 101, "power": 22, "durability": 135, "nerve": 260, "strength": 1.6}, # endurance not reflexes + ironman = durability definition
        "Water Polo": {"endurance": 96, "strength": 2.4, "durability": 110, "hand_eye": 180, "agility": 7.0, "nerve": 140}, # ball sport reaction
        "Rowing": {"endurance": 101, "power": 40, "strength": 2.8, "durability": 80, "agility": 8.0, "nerve": 280, "hand_eye": 260}, # linear sport but requires stroke coordination
        "Squash": {"agility": 6.3, "endurance": 85, "hand_eye": 155, "nerve": 150}, # agility 10 (ties tennis), elite hand-eye
        "Badminton": {"agility": 6.4, "endurance": 75, "hand_eye": 155, "nerve": 150, "speed": 4.55}, # agility 9.7, elite hand-eye, 200mph+ shuttlecock
        "Surfing (Big Wave)": {"nerve": 105, "durability": 100, "endurance": 75, "hand_eye": 160},
        "Rock Climbing (Lead)": {"nerve": 175, "strength": 2.5, "flexibility": 26, "endurance": 68},
        "Baseball": {"hand_eye": 155, "agility": 7.0, "endurance": 55, "power": 32, "nerve": 160}, # pitch-hitting elite
        "Ice Hockey": {"hand_eye": 180, "durability": 70, "endurance": 64, "power": 42, "agility": 6.2, "nerve": 140},
        "Cross-Country Skiing": {"endurance": 96, "power": 32, "durability": 128, "hand_eye": 350, "flexibility": 15, "nerve": 165}, # highest VO2 max + mental torture + descents
        "Basketball": {"endurance": 72, "power": 38, "durability": 25, "agility": 7.5, "hand_eye": 185, "nerve": 190}, # 2.5 miles per game + constant jumping
        "Football (American)": {"endurance": 52, "power": 42, "durability": 110, "strength": 2.5, "agility": 7.23, "speed": 4.4, "nerve": 150},
        "Boxing": {"endurance": 72, "power": 40, "durability": 140, "hand_eye": 170, "nerve": 110, "speed": 5.1}, # fast hands ≠ sprinting speed
        "F1 Racing": {"endurance": 77, "power": 20, "durability": 80, "hand_eye": 175, "nerve": 102, "agility": 4.5}, # 170bpm for 2 hours straight
        "Weightlifting": {"endurance": 45, "power": 48, "strength": 3.0, "durability": 40, "flexibility": 20, "nerve": 220},
        "Tennis": {"endurance": 65, "power": 36, "hand_eye": 158, "agility": 6.3, "flexibility": 18, "nerve": 170, "strength": 1.7, "durability": 90}, # 5-hour grind destroys joints, 100mph forehand power
        "Track & Field (100m)": {"speed": 4.22, "power": 45, "endurance": 42, "strength": 2.0, "nerve": 130}, # gun reaction
        "Archery": {"nerve": 135, "hand_eye": 160, "endurance": 42, "analytic": 40},
        "Shooting": {"nerve": 125, "hand_eye": 150, "endurance": 38, "analytic": 40},
        # USER SANITY FIXES - ROUND 2
        "Volleyball": {"power": 47, "agility": 7.0, "endurance": 57, "hand_eye": 285, "strength": 1.8, "durability": 13}, # highest vertical jumps in world
        "Handball": {"durability": 98, "agility": 6.86, "endurance": 48, "power": 34, "strength": 1.6, "nerve": 183}, # collision team sport
        "Hurling": {"hand_eye": 170, "speed": 4.67, "agility": 7.0, "endurance": 55, "power": 34, "durability": 23, "nerve": 172}, # fastest game on grass
        "Motocross": {"endurance": 91, "strength": 2.4, "power": 27, "durability": 32, "nerve": 106, "agility": 9.0}, # 70ft jumps in traffic - extreme fear factor
        "Curling": {"agility": 9.08, "speed": 6.27, "endurance": 56, "power": 29, "strength": 1.4}, # precision, not athleticism
        "Competitive Swimming (100m)": {"power": 42, "strength": 2.0, "endurance": 58, "speed": 5.0, "agility": 8.0, "flexibility": 23}, # explosive power event
        # USER SANITY FIXES - ROUND 3 (CREDIBILITY CRITICAL)
        "Bouldering": {"strength": 2.9, "power": 42, "flexibility": 26, "nerve": 174, "endurance": 48, "agility": 9.0, "hand_eye": 205}, # one-finger pullups = elite strength-to-weight
        "Field Hockey": {"endurance": 78, "agility": 7.0, "power": 23, "hand_eye": 264, "durability": 18}, # 10km per game like soccer
        "Canoe Slalom": {"agility": 6.77, "endurance": 51, "power": 23, "strength": 1.7, "nerve": 209, "flexibility": 10}, # whitewater gate navigation = pure agility
        "Volleyball": {"power": 47, "agility": 7.0, "endurance": 57, "hand_eye": 285, "strength": 1.8, "durability": 68}, # diving on hardwood floors repeatedly
        # USER SANITY FIXES - ROUND 4 (SPECIALIST FAILURES)
        "Beach Volleyball": {"endurance": 78, "power": 47, "agility": 6.9, "strength": 2.1, "durability": 29, "hand_eye": 286, "nerve": 220, "flexibility": 16}, # sand = 10x harder than indoor
        "Cricket": {"hand_eye": 160, "agility": 8.0, "endurance": 55, "power": 30, "nerve": 180, "durability": 32, "strength": 1.7}, # 90mph spinning ball = elite hand-eye, test matches = endurance
        "Mountain Biking (XC)": {"endurance": 88, "power": 36, "strength": 1.8, "durability": 31, "agility": 8.0, "nerve": 184}, # climbing mountains = elite endurance
        "Table Tennis": {"hand_eye": 152, "agility": 4.5, "endurance": 48, "nerve": 130, "strength": 1.1, "speed": 5.84}, # wrist/forearm only, 6-foot box (no sprinting)
        "Golf": {"hand_eye": 160, "nerve": 120, "analytic": 50, "flexibility": 20, "strength": 1.4}, # elite precision - pro athletes say it's extremely difficult
        # USER SANITY FIXES - ROUND 5 (CASUAL SPORTS REALITY CHECK)
        "Snooker": {"hand_eye": 160, "nerve": 135, "analytic": 54, "agility": 9.3, "speed": 6.5, "endurance": 58, "flexibility": 11, "durability": 5}, # precision pub sport - minimal movement
        "Billiards": {"hand_eye": 155, "nerve": 138, "analytic": 60, "agility": 9.3, "speed": 6.5, "endurance": 56, "flexibility": 11, "durability": 5}, # bar sport - can play with beer
        "Bowling": {"hand_eye": 180, "nerve": 190, "analytic": 42, "power": 30, "agility": 9.5, "speed": 6.5, "endurance": 50, "strength": 1.4}, # can play while eating nachos
        "Darts": {"hand_eye": 155, "nerve": 120, "analytic": 50, "agility": 9.8, "speed": 6.8, "endurance": 48, "flexibility": 8, "durability": 3}, # pub sport - zero movement
        "Slalom Skiing": {"nerve": 108, "agility": 5.8, "speed": 4.4, "power": 33, "durability": 32, "flexibility": 18, "endurance": 62, "hand_eye": 242}, # elite downhill skiing - nerve/agility critical
        "Archery": {"nerve": 125, "hand_eye": 160, "endurance": 48, "analytic": 50, "flexibility": 18, "power": 18, "agility": 9.0}, # standing precision - can be done casually
        "Shooting": {"nerve": 110, "hand_eye": 150, "endurance": 42, "analytic": 50, "flexibility": 10, "power": 15, "agility": 9.3}, # standing precision - minimal movement
        # USER SANITY FIXES - ROUND 6 (FINAL CREDIBILITY FIXES)
        "Synchronized Swimming": {"endurance": 91, "strength": 2.4, "power": 28, "flexibility": 26, "durability": 20, "nerve": 140, "hand_eye": 270}, # hypoxic training = hardest cardio, lifting humans
        "Cheerleading": {"power": 38, "nerve": 148, "durability": 115, "agility": 6.0, "flexibility": 24, "strength": 1.9}, # catastrophic injury risk (paralysis), explosive tosses
        "Parkour": {"nerve": 101, "durability": 128, "agility": 4.5, "power": 38, "strength": 2.2, "flexibility": 22}, # death consequence, concrete impacts
        "Badminton": {"agility": 6.4, "endurance": 75, "hand_eye": 155, "nerve": 150, "speed": 4.55}, # 200mph+ shuttlecock speed
        "Cycling (Road)": {"endurance": 95, "power": 35, "strength": 1.9, "durability": 25, "nerve": 150}, # descending mountains at 60mph on thin tires
        # USER SANITY FIXES - ROUND 7 (FINAL PHYSICS CORRECTIONS)
        "Fencing": {"speed": 6.12, "agility": 6.5, "hand_eye": 165, "nerve": 140, "endurance": 52, "flexibility": 22}, # explosive lunge ≠ sprinting
        "Downhill Skiing": {"speed": 4.28, "strength": 2.6, "durability": 127, "nerve": 105, "power": 38, "agility": 5.5, "endurance": 55}, # 80mph speed, 3-4G squat, massive crash risk
        "Lacrosse": {"durability": 97, "agility": 7.2, "endurance": 62, "hand_eye": 175, "power": 32, "strength": 1.8}, # full-contact with metal poles
        "Skateboarding (Street)": {"nerve": 162, "agility": 4.8, "durability": 85, "power": 35, "strength": 2.0} # concrete landings, core strength for tricks
    }

    # Cluster baselines (to remove "random jitter" feel)
    clusters = {
        "Racing": {"nerve": 110, "analytic": 90, "hand_eye": 185, "agility": 4.8, "durability": 60},
        "Combat": {"durability": 120, "strength": 2.2, "nerve": 125, "flexibility": 15, "agility": 4.4, "hand_eye": 170},
        "Endurance": {"endurance": 80, "strength": 1.4, "power": 20, "durability": 20, "flexibility": 10, "nerve": 260, "hand_eye": 300},
        "Racket": {"hand_eye": 165, "agility": 6.5, "endurance": 60, "flexibility": 16, "nerve": 170},
        "Precision": {"endurance": 40, "power": 15, "nerve": 140, "durability": 5, "hand_eye": 160, "analytic": 75}
    }

    def get_cluster(name):
        name = name.lower()
        if any(x in name for x in ["racing", "indycar", "karting", "rally", "speedway", "bobsleigh", "luge", "skeleton"]):
            return "Racing"
        if any(x in name for x in ["mma", "muay thai", "boxing", "wrestling", "judo", "kickboxing", "karate", "taekwondo", "sambo"]):
            return "Combat"
        if any(x in name for x in ["marathon", "cycling", "triathlon", "skiing", "kayaking", "swimming", "rowing"]):
            return "Endurance"
        if any(x in name for x in ["tennis", "table tennis", "badminton", "squash", "softball", "baseball", "cricket"]):
            return "Racket" # Or Ball/Hand-Eye cluster
        if any(x in name for x in ["golf", "archery", "shooting", "bowls", "curling", "darts", "billiards"]):
            return "Precision"
        return None

    for sport in sports:
        name = sport['name']
        
        # 1. Apply Anchor data (Hard Data)
        if name in anchors:
            sport.update(anchors[name])
            
        # 2. Apply Cluster logic for missing/random fields
        cluster_key = get_cluster(name)
        if cluster_key:
            cluster_data = clusters[cluster_key]
            # Only update if current value looks "jittered" (has decimals or outside reasonable range)
            for key, val in cluster_data.items():
                if key not in anchors.get(name, {}):
                    # For fields like nerve/hand_eye, if they are > 200 and shouldn't be, cap them
                    if key in ["nerve", "hand_eye"] and sport[key] > 300 and cluster_key != "Endurance":
                        sport[key] = val
                    # Rounding rule: Change 54.6 to 55, etc.
                    sport[key] = round(sport[key])

        # 3. Universal Rounding (The "Finish")
        for key in sport:
            if key == "name": continue
            if key in ["strength", "speed", "agility"]:
                sport[key] = round(float(sport[key]), 2)
            else:
                sport[key] = round(sport[key])

    # Save hardened data
    with open(raw_path, 'w') as f:
        json.dump(sports, f, indent=4)
        
    print(f"Hardened scientific data for {len(sports)} sports.")

if __name__ == "__main__":
    harden_data()
