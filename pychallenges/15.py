#Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
#The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.


def sum_polygon(n):
    return (n-2) * 180 