def find_my_age(birthyear):
    current_year = 2025
    age = current_year - birthyear
    return age

year = input("What year were you born?")
print(find_my_age(int(year)))
