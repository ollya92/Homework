"""
Implement a Pagination class helpful to arrange text on pages and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page
(take spaces into account as well). You need to be able to get the amount of whole symbols in text,
get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
If you're familiar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.
"""

import math


class Pagination:

    def __init__(self, text: str, symbols: int):
        self._text = text
        self._per_page = symbols

    def item_count(self):
        self.whole = len(self._text)
        return self.whole

    def page_count(self):
        self.p_count = math.ceil(len(self._text) / self._per_page)
        return self.p_count

    def count_items_on_page(self, number: int):
        self._num_page = number
        if self._num_page >= self.p_count:
            raise Exception(f"Invalid index. Page is missing.")
        else:
            if self._num_page == self.p_count - 1:
                return self.whole % self._per_page
            else:
                return self._per_page


if __name__ == "__main__":
    p = Pagination("Your beautiful text", 5)
    print(p.item_count())
    print(p.page_count())
    print(p.count_items_on_page(0))
    print(p.count_items_on_page(3))
    print(p.count_items_on_page(4))

