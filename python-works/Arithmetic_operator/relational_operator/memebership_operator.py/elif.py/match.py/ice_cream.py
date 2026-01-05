ice_cream=int(input("enter your faviourate flavour between 1 to 4"))

match ice_cream:

    case 1:

        print("your faviourate flavour is strawberry")
    
    case 2:

        print("your faviourate flavour is choclate")

    case 3:

        print("your faviourate flavour is vannila")

    case 4:

         print("your faviourate flavour is butterscotch")

    case _:

        print("invalid input")
