import random

############################################################################
## CONSTANTS
############################################################################
PLAYERS = [{"no":1, "name":"Joey", "defense":8}, 
{"no":2, "name":"Nick", "defense":8},
{"no":3, "name":"Russel", "defense":7},
{"no":4, "name":"Vivek", "defense":7},
{"no":5, "name":"Pritam", "defense":6},
{"no":6, "name":"Amit", "defense":6},
{"no":7, "name":"Chandler", "defense":5},
{"no":8, "name":"Colwin", "defense":5}]

############################################################################
## FUNCTIONS
############################################################################

def draw_match(players):
    a = random.choice(PLAYERS)
    PLAYERS.remove(a)
    b = random.choice(PLAYERS)
    PLAYERS.remove(b)
    return [a, b]

def play(a, b, a_score=0, b_score=0, attacker_a=True):
    attack_number = 0
    defense_array = []

    #print a_score, b_score
    if a_score >= 5:
        #print "Winner a"
        return {'winner':a, 'winner_score':a_score, 'loser_score': b_score}
    if b_score >= 5:
        #print "Winner b"
        return {'winner':b, 'winner_score':b_score, 'loser_score': a_score}


    attack_number = random.randint(1,10)
    arr_size = a.get('defense') if attacker_a else b.get('defense')
    defense_array = random.sample(xrange(1, 10), arr_size)
    #print "Attack number " + str(attack_number)
    #print "Defense Array " + str(defense_array)

    if attack_number in defense_array:
        if attacker_a:
            b_score += 1
            return play(a, b, a_score, b_score, False)
        else:
            a_score += 1
            return play(a, b, a_score, b_score, True)
    else:
        if attacker_a:
            a_score += 1
            return play(a, b, a_score, b_score, True)
        else:
            b_score += 1
            return play(a, b, a_score, b_score, False)

############################################################################
## MAIN
############################################################################

def refree():
    match1 = draw_match(PLAYERS)
    match1_winner = play(match1[0], match1[1])
    print "Match 1 between = " + match1[0].get('name') + " and " + match1[1].get('name')
    print "Match 1 winner = " + match1_winner.get('winner').get('name') + " Score = " + str(match1_winner.get('winner_score')) + " to " + str(match1_winner.get('loser_score'))

    match2 = draw_match(PLAYERS)
    match2_winner = play(match2[0], match2[1])
    print "Match 2 between = " + match2[0].get('name') + " and " + match2[1].get('name')
    print "Match 2 winner = " + match2_winner.get('winner').get('name') + " Score = " + str(match2_winner.get('winner_score')) + " to " + str(match2_winner.get('loser_score'))

    match3 = draw_match(PLAYERS)
    match3_winner = play(match3[0], match3[1])
    print "Match 3 between = " + match3[0].get('name') + " and " + match3[1].get('name')
    print "Match 3 winner = " + match3_winner.get('winner').get('name') + " Score = " + str(match3_winner.get('winner_score')) + " to " + str(match3_winner.get('loser_score'))

    match4 = draw_match(PLAYERS)
    match4_winner = play(match4[0], match4[1])
    print "Match 4 between = " + match4[0].get('name') + " and " + match4[1].get('name')
    print "Match 4 winner = " + match4_winner.get('winner').get('name') + " Score = " + str(match4_winner.get('winner_score')) + " to " + str(match4_winner.get('loser_score'))

    PLAYERS.append(match1_winner.get('winner')) 
    PLAYERS.append(match2_winner.get('winner')) 
    PLAYERS.append(match3_winner.get('winner')) 
    PLAYERS.append(match4_winner.get('winner')) 

    semi1 = draw_match(PLAYERS)
    semi1_winner = play(semi1[0], semi1[1])
    print "SEMI 1 between = " + semi1[0].get('name') + " and " + semi1[1].get('name')
    print "SEMI 1 winner = " + semi1_winner.get('winner').get('name') + " Score = " + str(semi1_winner.get('winner_score')) + " to " + str(semi1_winner.get('loser_score'))
     
    semi2 = draw_match(PLAYERS)
    semi2_winner = play(semi2[0], semi2[1])
    print "SEMI 2 between = " + semi2[0].get('name') + " and " + semi2[1].get('name')
    print "SEMI 2 winner = " + semi2_winner.get('winner').get('name') + " Score = " + str(semi2_winner.get('winner_score')) + " to " + str(semi2_winner.get('loser_score'))

    PLAYERS.append(semi1_winner.get('winner'))
    PLAYERS.append(semi2_winner.get('winner')) 

    final = draw_match(PLAYERS)
    final_winner = play(final[0], final[1])
    print "final between = " + final[0].get('name') + " and " + final[1].get('name')
    print "final winner = " + final_winner.get('winner').get('name') + " Score = " + str(final_winner.get('winner_score')) + " to " + str(final_winner.get('loser_score'))

if __name__=='__main__':
    refree()
   
