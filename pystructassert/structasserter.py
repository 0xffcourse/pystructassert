import logging

LOGGER = logging.getLogger(__name__)


class StructAsserter:

    def __init__(self, strict_mode=False,value_strict_mode=False,type_strict_mode=True, array_strict_mode=False):
        self._strict_mode = strict_mode
        self._value_strict_mode = value_strict_mode
        self._type_strict_mode = type_strict_mode
        self._array_strict_mode = array_strict_mode

    def struct_assert(self, expected, observed, path=["root"]):
        type_expected = type(expected)
        type_observed = type(observed)
        if self._type_strict_mode:
            if type_expected != type_observed:
                raise AssertionError(
                    "Expected {type_expected}, observed {type_observed} at: {path}".format(
                        type_expected=type_expected,
                        type_observed=type_observed,
                        path=":".join(path)
                    )
                )
        if type_expected == dict:
            for expected_child in expected.keys():
                next_path = path + [str(expected_child)]
                if expected_child not in observed.keys():
                    raise AssertionError(
                        "Expected element missing at: {path}".format(
                            path=":".join(next_path)
                        )
                    )
                self.struct_assert(
                    expected[expected_child], observed[expected_child], next_path)
