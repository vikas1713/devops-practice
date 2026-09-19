# Variables and types
name = "Vikas"
count = 5
is_active = True

# f-strings - how you'll build almost every message/log line
print(f"{name} has {count} items, active: {is_active}")

# Lists and loops
sites = ["github.com", "google.com", "doesnotexist123.com"]
for site in sites:
    print(f"Checking {site}")

# Functions
def greet(person):
    return f"Hello, {person}!"

print(greet("Vikas"))

# Reading/writing files - directly relevant to log parsing later
with open("output.txt", "w") as f:
    f.write("Python wrote this line\n")

with open("output.txt", "r") as f:
    print(f.read())
