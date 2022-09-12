import importlib


def repository(repo):
    module = importlib.import_module("src.repositories." + repo)
    return module.Repository()
