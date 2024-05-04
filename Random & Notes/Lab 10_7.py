def get_age():
    age=int(input())
    if age < 18 or age > 75:
        print("Invalid age.")
        print("Could not calculate heart rate info.")
        raise ValueError
    else:
        return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heartRate = 220 - age
    heart_rate = heartRate * 0.7
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    age = get_age()
    hr = fat_burning_heart_rate(age)

    print(f"Fat burning heart rate for a {age} year-old: {hr} bpm")