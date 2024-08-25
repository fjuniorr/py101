from notepad import decide_winner, Play, display_winner

winner = decide_winner(Play(username='player', choice='spock'),
              Play(username='computer', choice='spock'))


display_winner(winner, "foo")