from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......system.net.mime.content_disposition import ContentDisposition
    from ......system.net.mime.content_type import ContentType

@dataclass
class UploadRequestDto(Parsable):
    """
    Request parameters for uploading a file
    """
    # The contentDisposition property
    content_disposition: Optional[ContentDisposition] = None
    # The contentType property
    content_type: Optional[ContentType] = None
    # Specifies whether to create a new file if it already exists or not
    create_new_if_exist: Optional[bool] = None
    # File
    file: Optional[str] = None
    # List of files when specified as multipart/form-data
    files: Optional[List[str]] = None
    # Specifies whether to keep the file converting status or not
    keep_convert_status: Optional[bool] = None
    # Specifies whether to upload documents in the original formats as well or not
    store_original_file_flag: Optional[bool] = None
    # Request input stream
    stream: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UploadRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UploadRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UploadRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......system.net.mime.content_disposition import ContentDisposition
        from ......system.net.mime.content_type import ContentType

        from ......system.net.mime.content_disposition import ContentDisposition
        from ......system.net.mime.content_type import ContentType

        fields: Dict[str, Callable[[Any], None]] = {
            "contentDisposition": lambda n : setattr(self, 'content_disposition', n.get_object_value(ContentDisposition)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_object_value(ContentType)),
            "createNewIfExist": lambda n : setattr(self, 'create_new_if_exist', n.get_bool_value()),
            "file": lambda n : setattr(self, 'file', n.get_str_value()),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_primitive_values(str)),
            "keepConvertStatus": lambda n : setattr(self, 'keep_convert_status', n.get_bool_value()),
            "storeOriginalFileFlag": lambda n : setattr(self, 'store_original_file_flag', n.get_bool_value()),
            "stream": lambda n : setattr(self, 'stream', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from ......system.net.mime.content_disposition import ContentDisposition
        from ......system.net.mime.content_type import ContentType

        writer.write_object_value("contentDisposition", self.content_disposition)
        writer.write_object_value("contentType", self.content_type)
        writer.write_bool_value("createNewIfExist", self.create_new_if_exist)
        writer.write_str_value("file", self.file)
        writer.write_collection_of_primitive_values("files", self.files)
        writer.write_bool_value("keepConvertStatus", self.keep_convert_status)
        writer.write_bool_value("storeOriginalFileFlag", self.store_original_file_flag)
        writer.write_str_value("stream", self.stream)
    

