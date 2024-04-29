from fastapi import APIRouter
from app.utils.helper import CustomErrorResponse
from app.models.content_generation import GrammerCorrecterInput
from app.services.content_generation_service import grammar_corrector

router = APIRouter()
from typing import List


@router.post("/grammer")
async def product_desc(data: GrammerCorrecterInput):
    try:
        result=grammar_corrector(data.input_text)
        return {"result": result}
    except Exception as e:
        print(e, "error")
        return CustomErrorResponse.generate_response("Error", str(e), 500)
             
   