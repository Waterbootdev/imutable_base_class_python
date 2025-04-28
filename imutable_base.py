
from unlocked_context import DefaultUnlockedContext

class ImmutableBase:

    __LOCKED_ATTRIBUTE__ = "__locked"
    __LOCKED__ = True
    __UNLOCKED__ = False 

    def __init__(self, unlocked_context_class= DefaultUnlockedContext):

        ImmutableBase.__validate_class_or_raise_exception(unlocked_context_class)
        
        self._unlocked_context_class = unlocked_context_class
      
        super().__setattr__(ImmutableBase.__LOCKED_ATTRIBUTE__, ImmutableBase.__LOCKED__)

    @staticmethod
    def __validate_class_or_raise_exception(unlocked_context_class):
        
        if unlocked_context_class is None:
            raise ValueError("The 'unlocked_context_class' must not be None.")
        
        if not isinstance(unlocked_context_class, type):
            raise TypeError("The 'unlocked_context_class' must be a class type.")

        if ImmutableBase.__get_number_parameters_without_self(unlocked_context_class) != 1:
            raise TypeError("The 'unlocked_context_class' must have exactly one required parameter (besides 'self').")

    @staticmethod
    def __get_number_parameters_without_self(unlocked_context_class):
        import inspect
        return len(inspect.signature(unlocked_context_class.__init__).parameters.values()) - 1

    def __set__locked(self, value):
        if value is None:
            raise ValueError(f"__set_locked({value}) is forbidden!")

        if hasattr(self, ImmutableBase.__LOCKED_ATTRIBUTE__):
            super().__setattr__(ImmutableBase.__LOCKED_ATTRIBUTE__, value)
        else:
            raise Exception("Call super().__init__() before using unlock() or lock()!")

    def __setattr__(self, key, value):
        if getattr(self, ImmutableBase.__LOCKED_ATTRIBUTE__, True) and not key.startswith("_"):
            raise AttributeError(f"'{self.__class__.__name__}' is readonly! Modification of '{key}' is forbidden.")
        super().__setattr__(key, value)

    def lock(self):
        self.__set__locked(ImmutableBase.__LOCKED__)

    def unlock(self):
        self.__set__locked(ImmutableBase.__UNLOCKED__)

    def unlocked(self):
        return self._unlocked_context_class(self)
    
    