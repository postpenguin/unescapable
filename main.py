import time

def whatisname():
    print("      \\_/")
    print("     (* *)")
    print("    __)#(__")
    print("   ( )...( )(_)")
    print("   || |_| ||//")
    print(">==() | | ()/")
    print("    _(___)_")
    print("   [-]   [-]")
    user_input = input("I am RX-7x, what is your name? ")
    print("Welcome " + user_input + "!")
    time.sleep(1)

    print("\033[1m\033[90m*BONK!*\033[90m\033[0m")
    print("      \\_/¤---")
    print("     (x x)")
    print("    __)#(__")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(2)
    print("Ow! I must have hit my head..")
    print("    \_\ ")
    print("   (_**)")
    print("  __) #_")
    print(" ( )...()")
    print(" || | |I|")
    print(" || | |()__/")
    print(" /\(___)")
    print("_-\´´´´´´\ ")
    print("-,,,,,,,,- ,")
    time.sleep(2)

def havewemet():
    yn_input = input("Excuse me. Have we met before? (yes/no) ")
    time.sleep(2)
    if yn_input == "yes":
        print("...Sorry but I cannot remember you..")
        time.sleep(1)
        print("\033[90m...\033[0m")
        time.sleep(2)
    elif yn_input == "no":
        print("Oh.. I see, let me introduce myself!.. Ahem!")
        time.sleep(3)
        print("\033[90m...\033[0m")
        time.sleep(2)
    else:
        time.sleep(2)
        eleimination()

def eleimination():
    print("This is not a valid answer...")
    time.sleep(3)
    print("\033[91mInitiating Target Elimination\033[91m")
    time.sleep(1)
    print("\033[90m...\033[91m")
    time.sleep(1)
    print("      \\_/")
    print("     (* *)")
    print("    __)#(__")
    print("   ( )...( )(_)")
    print("   || |_| ||//")
    print(">==() | | ()/")
    print("    _(___)_")
    print("   [-]   [-]")
    time.sleep(1)
    print("        __")
    print("   _  |* *|")
    print("  / \\ \\--/ __")
    print("  ) O|----|  |   __")
    print(" / / \\ }{ /\\ )_ / _\\")
    print(")/  /\\__/\\ \\__O (__")
    print("|/  (--/\\--)    \\__/")
    print("/   _)(  )(_")
    print("   `---''---`")
    time.sleep(1)
    print("            ___")
    print("          |_|_|")
    print("          |_|_|              _____")
    print("          |_|_|     ____    |*_*_*|")
    print(" _______   _\\__\\___/ __ \\____|_|_   _______")
    print("/ ____  |=|      \\  <_+>  /      |=|  ____ \\")
    print("~|    |\\|=|======\\\\______//======|=|/|    |~")
    print(" |_   |    \\      |      |      /    |    |")
    print("  \\==-|     \\     |  []  |     /     |----|~~/")
    print("  |   |      |    |      |    |      |____~/")
    print("  |   |       \\____\\____/____/      /    / /")
    print("  |   |         {----------}       /____/ /")
    print("  |___|        /~~~~~~~~~~~~\\     |_/~|_|/")
    print("   \\_/        |/~~~~~||~~~~~\\|     /__|\\")
    print("   | |         |    ||||    |     (/|| \\)")
    print("   | |        /     |  |     \\       \\\\")
    print("   |_|        |     |  |     |")
    print("              |_____|  |_____|")
    print("              (_____)  (_____)")
    print("              |     |  |     |")
    print("              |     |  |     |")
    print("              |/~~~\\|  |/~~~\\|")
    print("              /|___|\\  /|___|\\")
    print("             <_______><_______>")
    time.sleep(1.5)

    user_choice = input("\033[90m*What is your action?* FIGHT/RUN\033[0m ").lower()

    if user_choice == "fight":
        fight()
    else:
        gameover()

def fight():
    print("\033[90m...\033[91m")
    time.sleep(1)
    print("          ^")
    print("         | |")
    print("       @#####@")
    print("     (###   ###)-.")
    print("   .(###     ###) \\")
    print("  /  (###   ###)   )")
    print(" (=-  .@#####@|_--\"")
    print(" /\\    \\_|l|_/ (\\")
    print("(=-\\     |l|    /")
    print(" \\  \\.___|l|___/")
    print(" /\\      |_|   /")
    print("(=-\\._________/\\")
    print(" \\             /")
    print("   \._________/")
    print("     #  ----  #")
    print("     #   __   #")
    print("     \\########/")
    print("\033[91mYou Are Trying To Fight Me? FOOL\033[91m")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(1)
    print("\033[90m...\033[91m")
    time.sleep(1)
    print("            ___              _./^^^\,")
    print("          |_|_|           ,/          `\ ")
    print("          |_|_|          ¦   _____")
    print("          |_|_|     ___\[]  |*_*_*|")
    print(" _______   _\\__\\___/ __ \\____|_|_   _______")
    print("/ ____  |=|      \\  <_+>  /      |=|  ____ \\")
    print("~|    |\\|=|======\\\\______//======|=|/|    |~")
    print(" |_   |    \\      |      |      /    |    |")
    print("  \\==-|     \\     |  []  |     /     |----|~~/")
    print("  |   |      |    |      |    |      |____~/")
    print("  |   |       \\____\\____/____/      /    / /")
    print("  |   |         {----------}       /____/ /")
    print("  |___|        /~~~~~~~~~~~~\\     |_/~|_|/")
    print("   \\_/        |/~~~~~||~~~~~\\|     /__|\\")
    print("\033[1m\033[90m*BONK!*\033[90m\033[0m")
    time.sleep(1)
    bonk()

def bonk():
    print("\033[90m...\033[0m")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(1)
    print("\033[90m...\033[0m")
    time.sleep(2)
    print("Ow! I must have hit my head..")
    print("    \_\ ")
    print("   (_**)")
    print("  __) #_")
    print(" ( )...()")
    print(" || | |I|")
    print(" || | |()__/")
    print(" /\(___)")
    print("_-\´´´´´´\ ")
    print("-,,,,,,,,- ,")
    time.sleep(2)
    havewemet()

def gameover():
    print("\033[91mThink You Can Outrun Me? HA!\033[91m")
    print("                                                 |")
    print("           _______                   ________    |")
    print("          |ooooooo|      ____       | __  __ |   |")
    print("          |[]+++[]|     [____]      |/  \\/  \\|   |")
    print("          |+ ___ +|     ]()()[      |\\__/\\__/|   |")
    print("          |:|   |:|   ___\\__/___    |[][][][]|   |")
    print("          |:|___|:|  |__|    |__|   |++++++++|   |")
    print("          |[]===[]|   |_|_/\\_|_|    | ______ |   |")
    print("        _ ||||||||| _ | | __ | | __ ||______|| __|")
    print("          |_______|   |_|[::]|_|    |________|   \\")
    print("                      \\_|_||_|_/                 \\")
    print("                        |_||_|                     \\")
    print("                       _|_||_|_                     \\")
    print("                      |___||___|                     \\")
    print("                                                       \\")
    print("                                                        \\")
    print("                  .__---~~~(~~-_.                       \\")
    print("               _-'  ) -~~- ) _-' )_                      \\")
    print("              (  ( `-,_..`.,_--_ '_,)_                    \\")
    print("             (  -_)  ( -_-~  -_ `,    )                    \\")
    print("             (_ -_ _-~-__-~`, ,' )__-'))--___--~~~--__--~~--___--__..")
    print("            _ ~`_-'( (____;--==,,_))))--___--~~~--__--~~--__----~~~'`=__-~+_-_.")
    print("           (@) (@) `````      `-_(())_-~  mn")
    time.sleep(2)
    print("\033[91mGAME OVER")
    time.sleep(5)
    print("\033[0mA light appears...")
    time.sleep(1)
    print("You feel your soul leave your body... or what is left of it.")
    time.sleep(2)

    gate_art = """
                                      {} {}
                              !  !  ! II II !  !  !
                           !  I__I__I_II II_I__I__I  !
                           I_/|__|__|_|| ||_|__|__|\\_I
                        ! /|_/|  |  | || || |  |  | \|\ !
            .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
           /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \\
           \\=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \\-__ /
            }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
           {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
     _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!
     _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
     -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
      |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
      |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
      |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
      |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  |
     _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
     -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
      jgs|  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
     ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~
    """

    print(gate_art)
    time.sleep(2)
    print("You have risen into heaven")
    time.sleep(2)
    print("Umm... who is that over there?")
    time.sleep(2)
    whatisname()
    havewemet()

continue_loop = True

while continue_loop:
        whatisname()
        havewemet()
