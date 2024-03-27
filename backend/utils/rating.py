def ratingNumberSum(
    ratings_lc_number: int | None,
    ratings_gr_number: int | None,
    ratings_tk_number: int | None,
):
    return sum(filter(None, [ratings_lc_number, ratings_gr_number, ratings_tk_number]))


def calculateRating(
    rating_lc: float | None,
    rating_gr: float | None,
    rating_tk: float | None,
    ratings_lc_number: int | None,
    ratings_gr_number: int | None,
    ratings_tk_number: int | None,
):
    ratings_number_sum = ratingNumberSum(
        ratings_lc_number, ratings_gr_number, ratings_tk_number
    )

    lc = rating_lc * ratings_lc_number / 2 if rating_lc is not None else 0
    gr = rating_gr * ratings_gr_number if rating_gr is not None else 0
    tk = rating_tk * ratings_tk_number if rating_tk is not None else 0

    return sum([lc, gr, tk]) / ratings_number_sum if ratings_number_sum != 0 else 0
