from pydantic import BaseModel

class User(BaseModel):
    user_id : int
    user_name : str
    user_email : str
    user_pw : str
    street_address : str
    address_line_2 : str
    phone : str

    class Config:
        orm_mode = True


