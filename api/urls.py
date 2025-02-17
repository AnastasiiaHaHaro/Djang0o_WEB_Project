
from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

# /api/v1/categories/   GET            All categories
# /api/v1/courses/      GET, POST      All courses
# /api/v1/categories/2/ GET            Single category
# /api/v1/course/3/     GET, DALETE    Single course

# For  DELETE, POST requests enable Authorization header
# EXAMPLE: ApiKey admin:admin123



urlpatterns = [
    path('', include(api.urls))
]