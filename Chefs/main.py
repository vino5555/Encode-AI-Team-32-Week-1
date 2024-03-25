
def chef_script(personality):
    if personality == "indonesian_chef":
        import indonesian_chef
        indonesian_chef.run()
    elif personality == "university_chef":
        import university_chef
        university_chef.run()
    elif personality == "peruvian_chef":
        import peruvian_chef
        peruvian_chef.run()

    else:
        print("Sorry, this personality is invalid.")

if __name__ == "__main__":
    while True:
        print("Choose one of the following chefs:")
        print("1. An energetic Indonesian chef")
        print("2. A tired cook with a Scottish accent working in a UK university")
        print("3. An expert Peruvian chef")
        personality = input("Type in the number corresponding to the chef of your choice: ")

        if personality == "1":
            chef_script("indonesian_chef")
        elif personality == "2":
            chef_script("university_chef")
        elif personality == "3":
            chef_script("peruvian_chef")
        else:
            print("Sorry, this number is out of bounds.")

