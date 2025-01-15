from abstractions.base_request import BaseRequest
from config import magic_cookie, request_message_type

class RequestMsg(BaseRequest):
    
    def __init__(self, file_size:int):
        self.magic_cookie:str = magic_cookie
        self.message_type:str = request_message_type
        self.file_size = file_size
        