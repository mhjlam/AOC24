import sys
import subprocess

def main():
    answers = [
        ["2031679", "19678534"],
        ["359", "418"],
        ["174103751", "100411201"],
        ["2618", "2011"],
        ["5275", "6191"],
        ["4982", "1663"],
        ["4364915411363", "38322057216320"],
        ["423", "1287"],
        ["6337921897505", "6362722604045"],
        ["760", "1764"],
        ["203953", "242090118578155"],
        ["1573474", "?"]
    ]

    errors = []
    with open("results", "w") as outfile:
        for i in range(1, 13):
            filename = f"source/day{i:02d}.py"
            result = subprocess.run([sys.executable, filename], capture_output=True, text=True)
            
            # Get the first non-empty line of output
            lines = [l for l in result.stdout.splitlines() if l.strip()]
            res1_num, res2_num = None, None
            if lines:
                parts = lines[0].strip().split()
                res1_num = parts[0] if len(parts) > 0 else None
                res2_num = parts[1] if len(parts) > 1 else None
            a1, a2 = answers[i-1]
            ok1 = res1_num == a1
            ok2 = res2_num == a2
            status = "SUCCESS" if ok1 and ok2 else "FAILURE"

            # Write status and results for the day
            outfile.write(f"{status} {res1_num if res1_num is not None else ''} {res2_num if res2_num is not None else ''}\n")
            outfile.flush()
            if not ok1:
                errors.append(f"ERROR: Day {i:02d} Part 1: result {res1_num}, answer {a1}")
            if not ok2:
                errors.append(f"ERROR: Day {i:02d} Part 2: result {res2_num}, answer {a2}")
    
    # Print errors to terminal
    for err in errors:
        print(err, file=sys.stderr)

if __name__ == "__main__":
    main()
