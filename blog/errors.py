# it's better to use views only for business logic. therefore we create separate exception class
class NoBlogFound(Exception):  # we are inheriting Exception base class. We can raise Exception class
    pass
