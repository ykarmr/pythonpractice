while True:
    try:
        x=int(input("enter a number:"))
        break
    except ValueError:
        print("try again")
    except (RuntimeError,TypeError,NameError):
        pass
