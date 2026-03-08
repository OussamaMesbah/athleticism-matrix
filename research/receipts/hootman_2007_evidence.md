# Scientific Receipt: Hootman et al. (2007)
**Source**: Journal of Athletic Training 2007;42(2):311–319
**Study**: "Epidemiology of Collegiate Injuries for 15 Sports: Summary and Recommendations"

## Data Evidence: Table 1 (Injury Rates per 1000 AE)
| Sport                  | Game Rate (IIR) | CI (95%)     | Practice Rate | CI (95%)   |
| :--------------------- | :-------------- | :----------- | :------------ | :--------- |
| **Football (Men)**     | 35.9            | (35.3, 36.5) | 9.6           | (9.4, 9.7) |
| **Soccer (Men)**       | 18.8            | (17.9, 19.8) | 4.3           | (4.1, 4.5) |
| **Soccer (Women)**     | 16.4            | (15.5, 17.2) | 5.2           | (5.0, 5.4) |
| **Wrestling (Men)**    | 26.4            | (24.7, 28.1) | 5.7           | (5.4, 5.9) |
| **Basketball (Men)**   | 9.9             | (9.2, 10.6)  | 4.3           | (4.1, 4.4) |
| **Basketball (Women)** | 12.1            | (11.2, 12.9) | 4.5           | (4.3, 4.7) |
| **Baseball (Men)**     | 5.8             | (5.3, 6.3)   | 1.9           | (1.8, 2.0) |
| **Softball (Women)**   | 4.3             | (3.8, 4.7)   | 2.7           | (2.5, 2.8) |
| **Volleyball (Women)** | 4.6             | (4.0, 5.1)   | 1.8           | (1.7, 1.9) |

## Implementation in Athleticism Matrix
- We use the **Game Rate** as the primary indicator for "Physical Punishment" (Durability).
- NFL (Pro Equivalent) is anchored at 150 (max) to reflect the 35.9 IIR.
- Soccer is anchored at 83 (approx 5.5 score) to reflect the ~18 IIR, which is roughly half of Football's intensity but still significant.
- Wrestling is anchored at 120 (approx 8.0 score) to reflect the 26.4 IIR.
- Gymnastics and other sports are adjusted based on training volume intensity (practice vs game) where data suggests high chronic load.
