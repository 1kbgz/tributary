import tributary.lazy as tl
from tributary.utils import _ismethod


def func(a, b=1):
    pass


class Example:
    def meth(self, a, b=1):
        pass

    @staticmethod
    def stat(a):
        pass

    @classmethod
    def clsmeth(cls, a):
        pass


class TestIsMethod:
    def test_function(self):
        assert not _ismethod(func)

    def test_bound_method(self):
        assert _ismethod(Example().meth)

    def test_unbound_method(self):
        # class attributes are plain functions whose first argument is ``self``
        assert _ismethod(Example.meth)

    def test_staticmethod(self):
        assert not _ismethod(Example.stat)

    def test_classmethod(self):
        assert _ismethod(Example.clsmeth)

    def test_builtin(self):
        assert not _ismethod(len)

    def test_non_callable(self):
        assert not _ismethod(5)
        assert not _ismethod(None)


class TestLazyNodeFromIssue189:
    # https://github.com/1kbgz/tributary/issues/189
    def test_node_construction_with_value(self):
        a = tl.Node(value=5)
        b = a + 2
        c = b % 4
        assert c() == 3
