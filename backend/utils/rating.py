def ratingNumberSum(
    ratings_lc_number: int, ratings_gr_number: int, ratings_tk_number: int
):
    return sum([ratings_lc_number, ratings_gr_number, ratings_tk_number])


def calculateRating(
    rating_lc: float,
    rating_gr: float,
    rating_tk: float,
    ratings_lc_number: int,
    ratings_gr_number: int,
    ratings_tk_number: int,
):
    ratings_number_sum = ratingNumberSum(
        ratings_lc_number, ratings_gr_number, ratings_tk_number
    )
    lc = rating_lc * ratings_lc_number / 2
    gr = rating_gr * ratings_gr_number
    tk = rating_tk * ratings_tk_number

    return sum([lc, gr, tk]) / ratings_number_sum
