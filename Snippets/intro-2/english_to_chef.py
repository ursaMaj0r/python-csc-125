def eng2chef(s):
    # rules
    s = s.replace('tion','shun')
    s = s.replace('an','un')
    s = s.replace('th','z')
    s = s.replace('v','f')
    s = s.replace('w','v')
    s = s.replace('c','k')
    s = s.replace('o','oo')
    s = s.replace('i','ee')
    if s[-1] == "!":
        s = s.replace("!",". bork bork bork!!")
    return s.lower()