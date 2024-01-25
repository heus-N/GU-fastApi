from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)




# import secrets
# str = secrets.token_urlsafe(32)
# print(str) 
# // JWT SECRET DE -- /core/configs.py // --
# JWT_SECRET: str = 'YzgasyMM-eb_1_8puSyEBPTvE9nSUgaYrq-VmO8dvLA'


"""
Token de autenticação "usuario_id: 6" : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE3MDY4MTg3MDUsImlhdCI6MTcwNjIxMzkwNSwic3ViIjoiNiJ9.XH7lbzC4bsI-DggDcqDpbtAJnphXLQ9hM5UaVywDI0s
Tipo: Bearer

Token de autenticação "usuario_id: 2" : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE3MDY4MjQyMTAsImlhdCI6MTcwNjIxOTQxMCwic3ViIjoiMiJ9.GLBN32q56fqABcWMkSXmejLuIoSUbteX_H4alDOBJ8o
Tipo: Bearer
"""