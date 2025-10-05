from administrator.dto.instructor_dto import InstructorDTO
from administrator.enums import RoleType
from authorization.helpers import generate_valid_password
from authorization.models import Role, User
from email_manager.services import EmailService


class InstructorService:

    @staticmethod
    def create_instructor(dto: InstructorDTO) -> User:
        password = generate_valid_password()
        user = User(
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            phone_number=dto.phone_number,
            specialization=dto.specialization,
            is_active=dto.is_active
        )
        user.set_password(password)
        user.save()

        teacher_role, _ = Role.objects.get_or_create(name="INSTRUCTOR")
        user.roles.set([teacher_role])

        EmailService.send_account_creation(
            user.id, user.email, user.first_name or "", password, RoleType.INSTRUCTOR.value
        )

        return user

    @staticmethod
    def update_instructor(user: User, dto: InstructorDTO) -> User:
        user.email = dto.email
        user.first_name = dto.first_name
        user.last_name = dto.last_name
        user.phone_number = dto.phone_number
        user.specialization = dto.specialization
        user.is_active = dto.is_active
        user.save()
        return user
