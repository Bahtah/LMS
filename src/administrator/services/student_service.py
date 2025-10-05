from administrator.dto.student_dto import StudentDTO
from administrator.enums import RoleType
from authorization.helpers import generate_valid_password
from authorization.models import User, Role
from email_manager.services import EmailService
from groups.models import Group


class StudentService:

    @staticmethod
    def create_student(dto: StudentDTO) -> User:
        groups_objs = Group.objects.filter(group_name__in=dto.group_names) if dto.group_names else []

        password = generate_valid_password()
        user = User(
            email=dto.email,
            first_name=dto.first_name,
            last_name=dto.last_name,
            phone_number=dto.phone_number,
            study_format=dto.study_format,
            is_active=dto.is_active,
            has_paid=dto.has_paid,
        )
        user.set_password(password)
        user.save()

        student_role, _ = Role.objects.get_or_create(name="STUDENT")
        user.roles.set([student_role])

        if groups_objs:
            user.groups.set(groups_objs)

        EmailService.send_account_creation(
            user.id, user.email, user.first_name or "", password, RoleType.STUDENT.value
        )

        return user

    @staticmethod
    def update_student(user: User, dto: StudentDTO) -> User:
        user.email = dto.email
        user.first_name = dto.first_name
        user.last_name = dto.last_name
        user.phone_number = dto.phone_number
        user.study_format = dto.study_format
        user.is_active = dto.is_active
        user.has_paid = dto.has_paid
        user.save()

        if dto.group_names is not None:
            groups_objs = Group.objects.filter(group_name__in=dto.group_names)
            print(f"{groups_objs=}")
            user.groups.set(groups_objs)

        return user

