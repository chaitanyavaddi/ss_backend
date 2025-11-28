from fastapi import APIRouter, Form, Request
from utils import get_conn
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Employees'])
templates = Jinja2Templates(directory="templates")

@router.get('/employees')
def get_employees(request: Request):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    rows = cur.fetchall()
    # conn.commit() only for write operations
    cur.close()
    conn.close()
    return templates.TemplateResponse('employees.html', {'request': request, 'persons': rows})

@router.post('/employees')
def get_employee_by_id(request: Request, emp_id = Form(...)):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees where employee_id=%s;', (emp_id,))
    person = cur.fetchone()
    # conn.commit() only for write operations
    cur.close()
    conn.close()
    
    return templates.TemplateResponse('employee_details.html', {'request': request, 'person': person})

@router.get('/employees/update/{emp_id}')
def get_employee_update_form(request: Request, emp_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees where employee_id=%s;', (emp_id,))
    person = cur.fetchone()
    # conn.commit() only for write operations
    cur.close()
    conn.close()
    
    return templates.TemplateResponse('update_employee.html', {'request': request, 'person': person})


@router.post('/employees/update')
def get_employee_update_form(request: Request, emp_id = Form(...), emp_name= Form(...)):
    conn = get_conn()
    cur = conn.cursor()
    print(emp_id, emp_name)
    cur.execute('UPDATE employees SET name=%s where employee_id=%s;', (emp_name, emp_id.strip()))
    conn.commit() 
    cur.close()
    conn.close()
    
    return templates.TemplateResponse('updated.html', {'request': request})


@router.get('/employees/delete/{emp_id}')
def get_employee_update_form(request: Request, emp_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM employees where employee_id=%s;', (emp_id,))
    conn.commit() 
    cur.close()
    conn.close()
    
    return templates.TemplateResponse('deleted.html', {'request': request})


@router.get('/')
def home(request: Request):
    return templates.TemplateResponse("home.html", {'request': request})
