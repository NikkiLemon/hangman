def display_hangman(tries):
    """
    Shows how many tries left on users word guess
    """
    if tries == 6:
        hangman = """\
_________
|/       |
|
|
|
|
|___________

6 Tries Left
        """
        elif tries == 5:
            hangman = """\
_________
|/       |
|        0
|
|
|
|___________


5 Tries Left
        """
        elif tries == 4:
            hangman = """\
_________
|/       |
|        0
|        |
|        |
|
|___________

4 Tries Left
        """
        elif tries == 3:
            hangman = """\
_________
|/       |
|        0
|       /|
|        |
|
|___________

3 Tries Left
        """
        elif tries == 2:
            hangman = """\
_________
|/       |
|        0
|       /|\\
|        |
|
|___________

2 Tries Left
        """
        elif tries == 1:
            hangman = """\
_________
|/       |
|        0
|       /|\\
|        |
|       /
|___________

1 Try Left
        """
        elif tries == 0:
            hangman = """\
_________
|/       |
|        0
|       /|\\
|        |
|       / \\
|___________

0 Tries Left - GAME OVER
        """
        else:
            hangman = " "

