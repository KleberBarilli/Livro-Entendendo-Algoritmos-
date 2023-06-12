voted = {}

def verify_voter(name):
    if voted.get(name):
        print("Go out!!")
    else:
        voted[name] = True
        print("Vote held!!")

verify_voter("kick")
verify_voter("john")
verify_voter("kick")