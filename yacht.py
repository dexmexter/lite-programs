# Change the values as you see fit
YACHT = "YACHT"
ONES = "ONES"
TWOS = 'TWOS'
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

# Having the score_card here allows for a game with multiple turns. The tests as given
# will not allow for this though.

#score_card = {"YACHT": 0, "ONES": 0, "TWOS": 0, "THREES": 0, 
#    "FOURS": 0, "FIVES": 0, "SIXES": 0, "FULL_HOUSE": 0, 
#    "FOUR_OF_A_KIND": 0, "LITTLE_STRAIGHT": 0, "BIG_STRAIGHT": 0, "CHOICE": 0
#    }

def score(dice, category):
    score_card = {"YACHT": 0, "ONES": 0, "TWOS": 0, "THREES": 0, 
    "FOURS": 0, "FIVES": 0, "SIXES": 0, "FULL_HOUSE": 0, 
    "FOUR_OF_A_KIND": 0, "LITTLE_STRAIGHT": 0, "BIG_STRAIGHT": 0, "CHOICE": 0
    }

    dice.sort()
    
    if category == "ONES":
        for i in dice:
            if i == 1:
                score_card[category] += i
    
    elif category == "TWOS":
        for i in dice:
            if i == 2:
                score_card[category] += i
    
    elif category == "THREES":
        for i in dice:
            if i == 3:
                score_card[category] += i
    
    elif category == "FOURS":
        for i in dice:
            if i == 4:
                score_card[category] += i
    
    elif category == "FIVES":
        for i in dice:
            if i == 5:
                score_card[category] += i
    
    elif category == "SIXES":
        for i in dice:
            if i == 6:
                score_card[category] += i
    
    elif category == "LITTLE_STRAIGHT":
        if dice == list(range(1, 6)):
            score_card[category] = 30

    elif category == "BIG_STRAIGHT":
        if dice == list(range(2, 7)):
            score_card[category] = 30
    
    elif category == "FULL_HOUSE":
        if dice.count(dice[0]) == 2 and dice.count(dice[4]) == 3 or\
        dice.count(dice[0]) == 3 and dice.count(dice[4]) == 2: 
            score_card[category] = sum(dice)

    elif category == "FOUR_OF_A_KIND":
        if dice.count(dice[0]) >= 4:
            score_card[category] = sum(dice[:4])
        
        elif dice.count(dice[4]) >= 4:
            score_card[category] = sum(dice[1:5])
    
    elif category == "YACHT":
        if dice.count(dice[0]) == 5:
            score_card[category] = 50
    
    elif category == "CHOICE":
        for i in dice:
            score_card[category] = sum(dice)
    
    #Counting full game score is outside the scope of the requested tests
    #grand_total = 0
    #for i in score_card:
    #    grand_total += score_card[i]
    
    return score_card[category]