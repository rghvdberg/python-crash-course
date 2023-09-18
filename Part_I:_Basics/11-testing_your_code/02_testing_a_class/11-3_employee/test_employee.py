import pytest
from employee import Employee


@pytest.fixture
def person():
    person = Employee("John", "Doe", 0)
    return person


def test_give_default_raise(person):
    person.give_raise()
    assert person.salary == 5000


def test_give_custom_raise(person):
    person.give_raise(4269)
    assert person.salary == 4269
