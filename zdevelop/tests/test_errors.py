from spantools.errors_api import APIError

import isleservice_objects.errors as error_module


def test_spanreed_code_compliance():
    """
    THIS TEST SHOULD REMAIN. IT VALIDATES THAT ALL ERRORS HAVE A UNIQUE CODE AND DO
    NOT CONFLICT WITH SPANREED'S RESERVED ERROR CODES
    """
    used_codes = set()

    for obj in error_module.__dict__.values():
        if not isinstance(obj, type):
            continue

        if not issubclass(obj, APIError):
            continue

        if not obj.__module__.endswith(".errors"):
            continue

        print(f"checking: {obj.__name__} from module: {obj.__module__}")

        assert isinstance(obj.api_code, int)
        assert obj.api_code > 1099

        assert obj.api_code not in used_codes
        used_codes.add(obj.api_code)

        assert isinstance(obj.http_code, int)
