import unittest
from pystructassert.structasserter import StructAsserter


class DictOnlyTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.struct_asserter = StructAsserter(
            strict_mode=False,
            value_strict_mode=False,
            type_strict_mode=True,
            array_strict_mode=False
        )

    def test_typestrict_passing(self):
        expected = {
            "person": {
                "name": "string",
                "location": {
                    "coordinates": {
                        "xCor": 0,
                        "yCor": 0
                    }
                }
            }
        }
        observed = {
            "person": {
                "name": "John",
                "location": {
                    "coordinates": {
                        "xCor": 76,
                        "yCor": 54,
                        "zCor": 67
                    }
                }
            }
        }
        self.struct_asserter.struct_assert(expected, observed)

    def test_typestrict_failing_by_missing(self):
        expected = {
            "person": {
                "name": "string",
                "location": {
                    "coordinates": {
                        "xCor": 0,
                        "yCor": 0
                    }
                }
            }
        }
        observed = {
            "person": {
                "name": "John",
                "location": {
                    "coordinates": {
                        "yCor": 0,
                        "zCor": 34
                    }
                }
            }
        }
        with self.assertRaises(AssertionError) as assertion_error:
            self.struct_asserter.struct_assert(expected, observed)
        assert str(
            assertion_error.exception) == "Expected element missing at: root:person:location:coordinates:xCor"

    def test_typestrict_failing_by_type(self):
        expected = {
            "person": {
                "name": "string",
                "location": {
                    "coordinates": {
                        "xCor": 0,
                        "yCor": 0
                    }
                }
            }
        }
        observed = {
            "person": {
                "name": "",
                "location": {
                    "coordinates": 45
                }
            }
        }
        with self.assertRaises(AssertionError) as assertion_error:
            self.struct_asserter.struct_assert(expected, observed)
        assert str(
            assertion_error.exception) == "Expected <class 'dict'>, observed <class 'int'> at: root:person:location:coordinates"
