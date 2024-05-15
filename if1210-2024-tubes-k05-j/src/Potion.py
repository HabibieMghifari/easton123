def Strength_Potion (atk_power):
    new_ATK = atk_power + atk_power*0.05
    return new_ATK

def Healing_Potion (hp):
    new_HP = hp + hp*0.25
    if (new_HP > 100):
        new_HP = 100
    return new_HP

def Resilience_Potion (def_power):
    new_DEF = def_power + def_power*0.25
    if (new_DEF > 50):
        new_DEF = 50
    return new_DEF
