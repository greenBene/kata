
book_price = 8
discounts = [1, 1, 0.95, 0.9, 0.8, 0.75]

def price(books):
    partitions = partition_books(books)
    price = get_minimum_price(partitions)

    return price


def partition_books(books):
    distinct_books = list(set(books))
    if len(distinct_books) == 0:
        return [[]]

    paritioned_books_all = []

    for i in range(1, len(distinct_books) + 1):
        new_partition = distinct_books[:i]
        other_books = remove_books(books, new_partition)
        other_books_partitioned = partition_books(other_books)
        partitioned_books = [[new_partition] + other_partitions for other_partitions in other_books_partitioned]
        paritioned_books_all += partitioned_books

    return paritioned_books_all


def remove_books(books, books_to_remove):
    books = books.copy()
    for book in books_to_remove:
        books.remove(book)
    return books


def get_minimum_price(partitions):
    prices = []
    for p in partitions:
        price = get_price_of_partition(p)
        prices.append(price)
    return min(prices)


def get_price_of_partition(partitioned_books):
    price_to_pay = 0

    for partition in partitioned_books:
        distinct_books = len(partition)
        price_to_pay += book_price * distinct_books * discounts[distinct_books]

    return price_to_pay
