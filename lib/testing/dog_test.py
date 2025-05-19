import sys
import os

# Add the parent directory (lib/) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dog import Dog

def test_dog_sit(capsys):
    dog = Dog()
    dog.sit()
    captured = capsys.readouterr()
    assert captured.out == "The dog is sitting.\n"
