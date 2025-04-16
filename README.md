# Welcome to the Calculator API Documentation

This API provides basic arithmetic operations.

## Endpoints

*   `/`: Serves the HTML interface for the calculator.
*   `/calculate` (POST): Performs the calculation based on form data (`a`, `b`, `action`).

## Form Data

*   `a`: First number.
*   `b`: Second number.
*   `action`: Operation to perform (`add`, `subtract`, `multiply`, `divide`, `power`).

## Response

The response is a JSON object containing the result of the calculation.

## Running the API

Use uvicorn:

```bash
uvicorn main:app --reload
```
