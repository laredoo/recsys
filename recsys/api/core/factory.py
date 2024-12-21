from controller.fetcher import FetcherController

class Factory:
    def __init__(self):
        pass

    def get_fetcher_controller():
        return FetcherController()

factory = Factory()