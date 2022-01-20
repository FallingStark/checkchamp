"""Main du selecteur"""




def main():
    """Demande quelle option l'user veut utilisé"""
    choice_bool = False

    while choice_bool is not True:
        print("Que veut tu faire")
        print("Check tes stats lol [1]")
        try:
            choice = int(input(""))
        except:
            choice = 0
        if 1 <= choice <= 2:
            choice_bool = True
    print(f"ton choice est {choice}")


if __name__ == "__main__":
    main()