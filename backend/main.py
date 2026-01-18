from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from explain import explain_text

app = FastAPI() # sets up backend server

app.add_middleware( # middleware to only allow post requests and different requests
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

class ExplainRequest(BaseModel): # the format that request will be sent to backend in
    text : str
    mode : str
    
@app.post('/explain')
def explain(req: ExplainRequest):
    """
    Docstring for explain
    
    :param req: Description
    :type req: ExplainRequest
    
    Wrapper function to do some preprocessing of request and call exlain_text function. 
    """
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text required")
    try:
        response = explain_text(req.mode,req.text)
        return {"result": response.strip()}
    except Exception:
        raise HTTPException(status_code=500, detail="AI failed")