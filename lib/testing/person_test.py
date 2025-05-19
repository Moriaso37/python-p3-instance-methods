import sys
import os

# Add the parent directory (lib/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from person import Person

def test_person_talk(capsys):
    person = Person()
    person.talk()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"

def test_person_walk(capsys):
    person = Person()
    person.walk()
    captured = capsys.readouterr()
    assert captured.out == "The person is walking.\n"
