from dataclasses import dataclass

@dataclass(frozen=True)
class PasswordResetRequestDTO:
    email: str
    resend: bool = False


@dataclass(frozen=True)
class PasswordResetConfirmDTO:
    email: str
    confirmation_code: int
    new_password: str


@dataclass(frozen=True)
class PasswordResetResultDTO:
    success: bool
    message: str
