from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import math

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'result': '---'})

@app.post('/calculate')
async def handle_calculation(request: Request, a: float = Form(...), b: float = Form(...), action: str = Form(...)):
    result_value: float | None = None
    error_message: str | None = None
    match action:
        case 'add':
            result_value = a + b
        case 'subtract':
            result_value = a - b
        case 'multiply':
            result_value = a * b
        case 'power':
            try:
                result_value = a ** b
                if math.isnan(result_value) or math.isinf(result_value):
                    error_message = 'Result is too large or undefined'
                    result_value = None
            except OverflowError:
                error_message = 'Result is too large (Overflow)'
            except ValueError:
                error_message = 'Invalid input for power operation'
        case 'divide':
            if b == 0:
                error_message = 'Cannot divide by zero'
            else:
                result = a / b
        case _:
            raise HTTPException(status_code=400, detail=f'Invalid action specified: {action}')

    if error_message:
        raise HTTPException(status_code=400, detail=error_message)

    if result_value is not None:
        if math.isnan(result_value) or math.isinf(result_value):
            raise HTTPException(status_code=400, detail='Calculation resulted in an undefined or infinite value')
        result_value = round(result_value, 10)
        return {'action': action, 'a': a, 'b': b, 'result': result_value}
    else:
        raise HTTPException(status_code=500, detail='Calculation failed unexpectedly')