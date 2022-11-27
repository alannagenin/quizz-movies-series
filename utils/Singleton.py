class Singleton(type):
    """
    Singleton is a creational design pattern, which ensures that
    only one object of its kindexists and provides a single point
    of access to it for any other code.
    Source: https://refactoring.guru/fr/design-patterns/singleton
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Instanciatiation of only one object.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
