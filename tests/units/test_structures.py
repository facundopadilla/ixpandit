from random import randint

from ixpandit.core.utils.structures import SearchListInMemory


class TestSearchListInMemory:
    def test_put_more_elements_than_max_size(self):
        obj = SearchListInMemory(max_size=3)
        for _ in range(10):
            obj.put(randint(0, 9))
        assert len(obj.elements()) == 3

    def test_last_element_has_been_pushed(self):
        obj = SearchListInMemory(max_size=3)
        obj.put("first")
        obj.put("second")
        obj.put("third")
        obj.put("fourth")
        elements = obj.elements()
        assert (
            len(elements) == 3 and elements[0] == "fourth" and "first" not in elements
        )
