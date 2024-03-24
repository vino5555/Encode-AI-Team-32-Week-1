
def chef_script(personality):
    if personality == "indonesian_chef":
        import indonesian_chef
        indonesian_chef.run()
    elif personality == "university_chef":
        import university_chef
        university_chef.run()

    else:
        print("Sorry, this personality is invalid.")

if __name__ == "__main__":
    while True:
        print("Choose one of the following chefs:")
        print("1. An energetic Indonesian chef")
        print("2. A tired cook with a Scottish accent working in a UK university")
        personality = input("Type in the number corresponding to the chef of your choice: ")

        if personality == "1":
            chef_script("indonesian_chef")
        elif personality == "2":
            chef_script("university_chef")
        else:
            print("Sorry, this number is out of bounds.")

