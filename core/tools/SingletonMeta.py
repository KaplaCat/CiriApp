class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    _instances = {}

    # Each of the following functions use cls instead of self
    # to emphasize that although they are instance methods of
    # Singleton, they are also *class* methods of a class defined
    # with Singleton
    def __call__(cls, *args, **kwargs):
        if cls not in SingletonMeta._instances:
            SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)
        return SingletonMeta._instances[cls]

    def clear(cls):
        try:
            del SingletonMeta._instances[cls]
        except KeyError:
            pass