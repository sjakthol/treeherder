from rest_framework import exceptions


class ResourceNotFoundException(exceptions.APIException):
    status_code = 404
    default_detail = "Resource not found"
