from dataclasses import dataclass


@dataclass(frozen=True)
class StudentDTO:
    email: str
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    study_format: str | None
    is_active: bool = True
    has_paid: bool = False
    group_names: list[str] | None = None
