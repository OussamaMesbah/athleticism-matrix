import json
import os

def normalize(value, min_val, max_val):
    if min_val == max_val:
        return 5.0
    score = (value - min_val) / (max_val - min_val)
    return round(max(0, min(10, score * 10)), 2)

def get_sport_families(sport_name):
    name = sport_name.lower()
    families = []
    if any(x in name for x in ['mma', 'boxing', 'wrestling', 'judo', 'bjj', 'muay thai']): families.append('Combat')
    if any(x in name for x in ['soccer', 'basketball', 'rugby', 'football', 'hockey', 'lacrosse']): families.append('Team Ball')
    if any(x in name for x in ['marathon', 'triathlon', 'cycling', 'rowing', 'cross-country']): families.append('Endurance')
    if any(x in name for x in ['gymnastics', 'skating', 'diving', 'trampolining']): families.append('Acrobatic')
    if any(x in name for x in ['f1', 'motocross', 'rally', 'racing']): families.append('Motor Racing')
    if any(x in name for x in ['darts', 'golf', 'snooker', 'billiards', 'bowls', 'curling', 'shooting', 'archery']): families.append('Precision')
    if not families: families.append('General')
    return families

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_path = os.path.join(base_dir, 'data', 'sports_raw.json')
    output_path = os.path.join(base_dir, 'data', 'ranked_sports.json')
    public_output_path = os.path.join(base_dir, 'public', 'ranked_sports.json')

    constants = {
        "endurance": {"min": 35, "max": 105},
        "strength": {"min": 0.5, "max": 3.5},
        "power": {"min": 5, "max": 55},
        "speed": {"min": 6.5, "max": 4.0},
        "agility": {"min": 10.5, "max": 3.8},
        "flexibility": {"min": 0, "max": 35},
        "nerve": {"min": 300, "max": 80},
        "durability": {"min": 0, "max": 200},
        "hand_eye": {"min": 400, "max": 130},
        "analytic": {"min": 20, "max": 100}
    }

    with open(raw_path, 'r') as f:
        sports_raw = json.load(f)

    # REFINED SCORING ENGINE
    max_multiplier_anchor = 1.65

    ranked_sports = []

    for sport in sports_raw:
        normalized_sport = {
            "name": sport["name"],
            "scores": {},
            "raw": sport,
            "families": get_sport_families(sport["name"]),
            "confidence": sport.get("confidence", 70),
            "evidence": sport.get("evidence", "Archetype Inference"),
            "justification": sport.get("justification", "")
        }
        
        cat_scores = {}
        for cat, range_vals in constants.items():
            val = sport[cat]
            score = normalize(val, range_vals["min"], range_vals["max"])
            normalized_sport["scores"][cat] = score
            cat_scores[cat] = score

        # 1. BASE ATHLETICISM (Physical 60% / Technical 40%)
        physical_score = (sum([cat_scores[c] for c in ["endurance", "strength", "power", "speed", "agility"]])) / 5.0
        skill_score = (sum([cat_scores[c] for c in ["flexibility", "nerve", "durability", "hand_eye", "analytic"]])) / 5.0
        
        # Specialist Protection: Reward elite single peaks (e.g. Sprinting speed)
        max_single_peak = max(cat_scores.values())
        peak_bonus = (max_single_peak / 10.0) * 2.0 # Increased to 2.0 for better specialist protection
        
        base_athleticism = (physical_score * 0.6) + (skill_score * 0.4) + peak_bonus
        
        # 2. SCIENTIFIC MULTIPLIERS
        metabolic_factor = sport["metabolic_demand"] / 10.0
        dof_factor = sport["dof"] / 24.0
        g_factor = (sport["g_load"] ** 0.5) / 3.0
        talent_factor = sport["scarcity"] / 5.0
        
        multiplier = (metabolic_factor * 0.4) + (dof_factor * 0.3) + (g_factor * 0.2) + (talent_factor * 0.1)
        
        # 3. FINAL NORMALIZATION & CONFIDENCE WEIGHTING
        # Calculate raw rank
        total_rank_raw = (base_athleticism * (multiplier / max_multiplier_anchor)) * 10
        
        # RELIABILITY PENALTY: Lower confidence data has higher "error bars"
        # We slightly penalize the displayed score for low confidence to reflect the "True Athleticism" 
        # bias towards proven high-evidence sports.
        # Penalty: max 5% reduction for 0% confidence (linear)
        reliability_factor = 0.95 + (sport.get("confidence", 70) / 100.0) * 0.05
        
        normalized_sport["total_rank"] = round(max(0, min(100, total_rank_raw * reliability_factor)), 2)
        
        normalized_sport["breakdown"] = {
            "physical_base": round(physical_score, 2),
            "skill_base": round(skill_score, 2),
            "peak_bonus": round(peak_bonus, 2),
            "metabolic_mult": round(metabolic_factor, 2),
            "biomechanic_mult": round(dof_factor, 2),
            "trauma_mult": round(g_factor, 2),
            "scarcity_mult": round(talent_factor, 2),
            "total_multiplier": round(multiplier, 2)
        }
        
        ranked_sports.append(normalized_sport)

    ranked_sports.sort(key=lambda x: x["total_rank"], reverse=True)

    with open(output_path, 'w') as f:
        json.dump(ranked_sports, f, indent=4)
    with open(public_output_path, 'w') as f:
        json.dump(ranked_sports, f, indent=4)
    
    print(f"Processed {len(ranked_sports)} sports with refined Specialist Protection.")

if __name__ == "__main__":
    main()
