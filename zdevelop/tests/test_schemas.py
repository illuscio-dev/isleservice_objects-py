from isleservice_objects.schemas import NameSchema


def test_name_validation_fails():
    data = {"first": "Obi Wan", "last": "Kenobi san"}
    assert "first" in NameSchema().validate(data)
    assert "last" in NameSchema().validate(data)
