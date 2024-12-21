from controller.fetcher import FetcherController

class Factory:
    def __init__(self):
        pass

    async def get_fetcher_controller(self):
        return FetcherController()