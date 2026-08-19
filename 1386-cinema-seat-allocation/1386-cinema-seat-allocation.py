class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats only for rows that actually have reservations
        for row, seat in reservedSeats:
            rows.setdefault(row, set()).add(seat)

        # Every completely empty row can fit 2 families
        count = 2 * n

        for seats in rows.values():

            # Possible family groups:
            # 2,3,4,5
            # 4,5,6,7
            # 6,7,8,9

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            left_free = seats.isdisjoint(left)
            middle_free = seats.isdisjoint(middle)
            right_free = seats.isdisjoint(right)

            if left_free and right_free:
                # This row can already fit 2 families
                pass

            elif left_free or middle_free or right_free:
                # This row can fit 1 family instead of the default 2
                count -= 1

            else:
                # This row can fit 0 families instead of the default 2
                count -= 2

        return count