import json
import os

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'public', 'ranked_sports.json')
    
    with open(data_path, 'r') as f:
        sports = json.load(f)
    
    metrics = [
        "endurance", "strength", "power", "speed", "agility", 
        "flexibility", "nerve", "durability", "hand_eye", "analytic"
    ]
    
    report_path = os.path.join(base_dir, 'research', 'metric_rank_report.md')
    
    with open(report_path, 'w') as f:
        f.write("# Metric-by-Metric Ranking Report\n\n")
        f.write("Use this report to verify relative ordering of sports for each physiological metric.\n\n")
        
        for metric in metrics:
            f.write(f"## {metric.capitalize()} Rankings\n")
            f.write("| Rank | Sport | Score | Raw Value |\n")
            f.write("|------|-------|-------|-----------|\n")
            
            # Sort sports by score for this metric
            sorted_sports = sorted(sports, key=lambda x: x["scores"][metric], reverse=True)
            
            for i, sport in enumerate(sorted_sports):
                rank = i + 1
                name = sport["name"]
                score = sport["scores"][metric]
                raw = sport["raw"][metric]
                f.write(f"| {rank} | {name} | {score} | {raw} |\n")
            f.write("\n")

    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()
