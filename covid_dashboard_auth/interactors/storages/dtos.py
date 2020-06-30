from dataclasses import dataclass

@dataclass()
class UserDetailsDTO:
    user_id: int
    is_admin: bool
