from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ("resourceName",)
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    resourceName: str
    def __init__(self, resourceName: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ("status_code", "Response")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    Response: str
    def __init__(self, status_code: _Optional[int] = ..., Response: _Optional[str] = ...) -> None: ...
