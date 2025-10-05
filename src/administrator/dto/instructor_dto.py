from dataclasses import dataclass


@dataclass(frozen=True)
class InstructorDTO:
    email: str
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    specialization: str | None
    is_active: bool = True
