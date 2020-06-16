class InvalidMealId(Exception):
    def __init__(self, msg):
        self.msg = msg

class InvalidItemId(Exception):
    def __init__(self, msg):
        self.msg = msg

class InvalidPreferenceItemId(Exception):
    def __init__(self, msg):
        self.msg = msg

class DuplicateItemIds(Exception):
    def __init__(self, msg):
        self.msg = msg

class InvalidItemQuantity(Exception):
    def __init__(self, msg):
        self.msg = msg

class MealTimeOut(Exception):
    def __init__(self, msg):
        self.msg = msg
