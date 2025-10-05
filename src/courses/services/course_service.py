from courses.dto.course_dto import CourseDTO
from courses.models import Course


from django.db import transaction

class CourseService:

    @staticmethod
    def create_course(dto: CourseDTO) -> Course:
        with transaction.atomic():
            course = Course.objects.create(
                name_course=dto.name_course,
                description=dto.description,
                course_img=dto.course_img,
                start_course=dto.start_course,
                instructor=dto.instructor
            )

            if dto.groups:
                course.groups.set(dto.groups)

        return course

    @staticmethod
    def update_course(course: Course, dto: CourseDTO) -> Course:
        course.name_course = dto.name_course
        course.description = dto.description
        course.course_img = dto.course_img
        course.start_course = dto.start_course

        if dto.instructor is not None:
            if dto.instructor == "":
                course.instructor = None
            else:
                course.instructor = dto.instructor

        course.save()

        if dto.groups is not None:
            course.groups.set(dto.groups)

        return course

