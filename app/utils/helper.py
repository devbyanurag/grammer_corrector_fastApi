from fastapi.responses import JSONResponse
from app.models.common.shared_models import ErrorResponseModel
from app.utils.constants import ResponseValues

class CustomErrorResponse:
    @classmethod
    def generate_response(cls, title: str, message: str, status_code: int):
        error_response = ErrorResponseModel(
            status=ResponseValues.ERROR,
            message=message,
            body={"error": title}
        )
        return JSONResponse(content=error_response.model_dump(), status_code=status_code)

