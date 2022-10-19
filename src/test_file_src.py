import pytest


def test_src():
    print('Test')


def src_test():
    print('Test')


def not_test_case():
    print('Test')


class TestClass:
    @pytest.mark.only
    def test_moday(self):
        print('Mon')
        a = 1
        b = 2

        assert a == b, "FAILED: test-moday is not happy"

    @pytest.mark.stress
    def test_tuesday(self, value):
        print('Tue test')
        print('Value is:', value)
