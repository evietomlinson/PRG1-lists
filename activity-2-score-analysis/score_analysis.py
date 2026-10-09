PASS_MARK = 40
DISTINCTION_MARK = 70
FAIL_MARK = 40 

scores = [72, 38, 55, 91, 40, 27, 66, 83, 45, 39]

passed = []
failed = []
distinction = [] 

for score in scores:
    if score >= PASS_MARK and score >= DISTINCTION_MARK:
        passed.append(score) # 7 pass
    elif score >= DISTINCTION_MARK:
        distinction.append(score)
    else:
        failed.append(score) # 3 fail 

print(f"{len(scores)} learners sat the paper") #10
print(f"{len(passed)} passed, {len(failed)} did not with {len(distinction)} getting a distinction") #7 passed, 3 did not 

average = sum(scores) / len(scores)
print(f"Average: {average:.1f}") # Average: 55.6
print(f"Highest: {max(scores)}") # Highest: 91
print(f"Lowest: {min(scores)}") # Lowest: 27 

pass_rate = len(passed) / len(scores) * 100 #
print(f"Pass rate: {pass_rate:.0f}%") #Pass rate: 70%

print(f"Needs support: {sorted(failed)}") #Needs support: [27, 38, 39]
