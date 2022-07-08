from loader import Loader
from .main import MainMiddleware


ld = Loader()
dp = ld.get_dispatcher()

if __name__ == "middlewares":
    dp.middleware.setup(MainMiddleware())