from .price import PriceFilter
from .rating import RatingFilter
from .decency import AccountDecency
from .lvl import AccountLvl
from loader import Loader


ld = Loader()
dp = ld.get_dispatcher()

if (__name__ == "__filters__"):
    dp.filters_factory.bind(PriceFilter)
    dp.filters_factory.bind(RatingFilter)
    dp.filters_factory.bind(AccountLvl)
    dp.filters_factory.bind(AccountDecency)