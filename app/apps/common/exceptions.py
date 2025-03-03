from fastapi import HTTPException


class ApplicationException(HTTPException):
    status_code = 500
    detail = "Application Error"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ObjDoesNotExistException(ApplicationException):
    status_code = 404
    detail = "Object does not exist"
