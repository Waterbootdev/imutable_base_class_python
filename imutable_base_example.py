from imutable_base import ImmutableBase

class ImutableBaseExample(ImmutableBase):

    def __init__(self, name, alter, cache, status):
        super().__init__()
        
        with self.unlocked():
            self.name = name
            self.alter = alter

        self._cache = cache
        self._status = status

a = ImutableBaseExample("Anna", 30, "abc", "online")
b = ImutableBaseExample("Bernd", 40, "xyz", "offline")

print(a.name)  # Anna
print(b.name)  # Bernd

try:
    a.name = "Anna 2"
except AttributeError as e:
    print(e)  # ImmutableBase is readonly! Modification of 'name' is forbidden.

print(b.name)  # Bernd

# Innerhalb Context entsperrt:
with a.unlocked():
    a.name = "Anna 2"

print(a.name)  # Anna 2

# Danach wieder gesperrt:
try:
    a.name = "Anna 3"
except AttributeError as e:
    print(e)


# OK:
a = ImmutableBase()

# Fehler: None übergeben
try:
    b = ImmutableBase(None)
except Exception as e:
    print(e)  # -> The 'unlocked_context_class' must not be None.

# Fehler: kein Typ übergeben (z.B. eine Zahl)
try:
    b = ImmutableBase(123)
except Exception as e:
    print(e)  # -> The 'unlocked_context_class' must be a class type.

# Fehler: Klasse ohne passenden Konstruktor
class BadContext:
    def __init__(self, x, y):
        pass

try:
    b = ImmutableBase(BadContext)
except Exception as e:
    print(e)  # -> The 'unlocked_context_class' must have exactly one required parameter (besides 'self').
