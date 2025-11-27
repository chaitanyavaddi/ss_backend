from fastapi import APIRouter
from utils import get_conn
from fastapi.responses import JSONResponse

router = APIRouter(tags=['Employees'])

@router.get('/employees')
def get_employees():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    rows = cur.fetchall()
    # conn.commit() only for write operations
    cur.close()
    conn.close()
    return JSONResponse(content=rows)