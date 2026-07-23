search_term = "Accepted password"
match_count = 0
with open("sample.log", "r") as log_file:
    for line in log_file:
        if search_term in line:
            print(line.strip())
            match_count += 1
print(f"Total matches found: {match_count}")