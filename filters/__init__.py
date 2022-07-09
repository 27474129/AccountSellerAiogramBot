from .price import PriceFilter
from .rating import RatingFilter
from .decency import AccountDecency
from .lvl import AccountLvl
from .hours import AccountHours
from .ranks import RanksFilter
from .faceit import FaceitFilter
from loader import Loader


ld = Loader()
dp = ld.get_dispatcher()

if (__name__ == "__filters__"):
    dp.filters_factory.bind(PriceFilter)
    dp.filters_factory.bind(RatingFilter)
    dp.filters_factory.bind(AccountLvl)
    dp.filters_factory.bind(AccountDecency)
    dp.filters_factory.bind(RanksFilter)
    dp.filters_factory.bind(AccountHours)
    dp.filters_factory.bind(FaceitFilter)