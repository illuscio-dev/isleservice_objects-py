from isleservice_objects.models import Name, Enemy


def test_name_full():
    assert Name("Billy", "Peake").full_name == "Billy Peake"


def test_enemy_addressable():
    assert Enemy("Captain", Name("Billy", "Peake")).addressable == "Captain Peake"
