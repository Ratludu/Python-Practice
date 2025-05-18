def sum_odd_digits(digits: list) -> int:

    tracking_sum = 0

    for i in digits:
        assert isinstance(i,int), f"{i} is not a integer!"
        if i % 2 != 0:
            tracking_sum += i

    return tracking_sum
