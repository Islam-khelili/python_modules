import sys


print("=== Player Score Analytics ===")

if len(sys.argv) <= 1:
    print("No scores provided.")
    print("Usage: python3 ft_score_analytics.py <score1> <score2> ..")
else:
    arr = []
    for num in sys.argv[1:]:
        try:
            arr.append(int(num))
        except ValueError:
            print(f"Invalid paramater: {num}")
    print(f"Scores processed: {arr}")
if len(arr) == 0:
    print("No scores provided.")
    print("Usage: python3 ft_score_analytics.py <score1> <score2> ..")
else:
    print(f"Total players: {len(arr)}")
    print(f"Total score: {sum(arr)}")
    average = float(sum(arr)/len(arr))
    print(f"Average score: {average}")
    print(f"High score: {max(arr)}")
    print(f"Low score: {min(arr)}")
    score_range = max(arr) - min(arr)
    print(f"Score range: {range}")
