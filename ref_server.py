import time
import random
import BaseHTTPServer

from players_dict import PLAYERS_CONFIG, Player

HOST_NAME = 'localhost'
PORT_NUMBER = 8888

#############################################################################################
##Functions
#############################################################################################

def create_players():
    global PLAYER_OBJECTS
    PLAYER_OBJECTS = []
    for player in PLAYERS_CONFIG:
        p = Player(player)
        PLAYER_OBJECTS.append(p)
    return "Players created"

def draw_matches():
    global MATCHES
    MATCHES = []
    if 'PLAYER_OBJECTS' in globals() and len(PLAYER_OBJECTS) > 1:
        for i in xrange(0,len(PLAYER_OBJECTS)/2):
            a = random.choice(PLAYER_OBJECTS)
            PLAYER_OBJECTS.remove(a)
            b = random.choice(PLAYER_OBJECTS)
            PLAYER_OBJECTS.remove(b)
            MATCHES.append([a, b])
        return "Matches drawn"
    else:
        return "No players to draw matches"

def start_games():
    global SEMIS
    global finalist1
    global finalist2
    global champion
    SEMIS = []
    if 'MATCHES' in globals() and len(MATCHES)> 1:
        for match in MATCHES:
            winner = play(match[0], match[1])
            SEMIS.append(winner)
        
        finalist1 = play(SEMIS[0]['winner'], SEMIS[3]['winner'])
        finalist2 = play(SEMIS[1]['winner'], SEMIS[2]['winner'])

        champion = play(finalist1['winner'], finalist2['winner'])
        return "Matches Done"

    else:
        return "No matches to play"

def play(a, b, a_score=0, b_score=0, attacker_a=True):
    attack_number = 0
    defence_array = []
    #print a_score, b_score
    if a_score >= 5:
        #print "Winner a"
        return {'winner':a, 'winner_score':a_score, 'loser_score': b_score}
    if b_score >= 5:
        #print "Winner b"
        return {'winner':b, 'winner_score':b_score, 'loser_score': a_score}


    attack_number = random.randint(1,10)
    arr_size = a.defence if attacker_a else b.defence
    defence_array = random.sample(xrange(1, 10), arr_size)
    #print "Attack number " + str(attack_number)
    #print "Defense Array " + str(defence_array)

    if attack_number in defence_array:
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


def result():
    if set(['MATCHES', 'SEMIS', 'finalist1', 'finalist2','champion']).issubset(globals()):
        response = ""
        for i in xrange(0,4):
            response += "Match "+str(i)+" :: " + MATCHES[i][0].name + " vs " + MATCHES[i][1].name + ", Winner = " + SEMIS[i]['winner'].name + " with score " + str(SEMIS[i]['winner_score']) + " to " + str(SEMIS[i]['loser_score'])+"</br>"
        
        response += "SEMI 1 :: " + SEMIS[0]['winner'].name + " vs " + SEMIS[3]['winner'].name + ", Winner = " + finalist1['winner'].name + " with score " + str(finalist1['winner_score']) + " to " + str(finalist1['loser_score'])+"</br>"
        response += "SEMI 2 :: " + SEMIS[1]['winner'].name + " vs " + SEMIS[2]['winner'].name + ", Winner = " + finalist2['winner'].name + " with score " + str(finalist2['winner_score']) + " to " + str(finalist2['loser_score'])+"</br>"
        response += "FINAL :: " + finalist1['winner'].name + " vs " + finalist2['winner'].name + ", Winner = " + champion['winner'].name + " with score " + str(champion['winner_score']) + " to " + str(champion['loser_score'])+"</br>"

        return response

    else:
        return "Not all matches completed"


#############################################################################################
##Testing
#############################################################################################

def test():
    create_players()
    draw_matches()
    start_games()
    result()
    return "Done"

#############################################################################################
##Function pointer for paths
#############################################################################################
router = {'/create_players':create_players,
'/draw_matches':draw_matches,
'/play':start_games,
'/result':result,
'/test':test}
#############################################################################################
##HTTP Handler class
#############################################################################################

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        req = router.get(s.path)
        if req:
            resp = req()
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(resp)
        else:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("<p>You accessed path: %s, no mathing function pointer</p>" % s.path)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Referee Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Referee Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
