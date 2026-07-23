file_name = input("Enter the log file name: ")
search_term = input("Enter a search term: ").lower()
match_count = 0
try:
    with open(file_name, "r" ) as log_file:
        for line in log_file:
            lowercase_line = line.lower()
            if search_term in lowercase_line:
                print(line.strip())
                match_count += 1

    print(f"total matches found: {match_count}")
except FileNotFoundError:
    print(f"Error the file {file_name} Not Found")