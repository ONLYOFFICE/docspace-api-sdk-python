from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...document_config_dto import DocumentConfigDto
    from ...editor_configuration_dto import EditorConfigurationDto
    from ...file_dto.system.int32 import Int32

@dataclass
class Int32(Parsable):
    # The document property
    document: Optional[DocumentConfigDto] = None
    # Document type
    document_type: Optional[str] = None
    # The editorConfig property
    editor_config: Optional[EditorConfigurationDto] = None
    # [0 - Desktop, 1 - Mobile, 2 - Embedded]
    editor_type: Optional[int] = None
    # Editor URL
    editor_url: Optional[str] = None
    # Error message
    error_message: Optional[str] = None
    # The file property
    file: Optional[Int32] = None
    # Filling session Id
    filling_session_id: Optional[str] = None
    # Specifies if the filling has started or not
    start_filling: Optional[bool] = None
    # Token
    token: Optional[str] = None
    # Platform type
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...document_config_dto import DocumentConfigDto
        from ...editor_configuration_dto import EditorConfigurationDto
        from ...file_dto.system.int32 import Int32

        from ...document_config_dto import DocumentConfigDto
        from ...editor_configuration_dto import EditorConfigurationDto
        from ...file_dto.system.int32 import Int32

        fields: Dict[str, Callable[[Any], None]] = {
            "document": lambda n : setattr(self, 'document', n.get_object_value(DocumentConfigDto)),
            "documentType": lambda n : setattr(self, 'document_type', n.get_str_value()),
            "editorConfig": lambda n : setattr(self, 'editor_config', n.get_object_value(EditorConfigurationDto)),
            "editorType": lambda n : setattr(self, 'editor_type', n.get_int_value()),
            "editorUrl": lambda n : setattr(self, 'editor_url', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(Int32)),
            "fillingSessionId": lambda n : setattr(self, 'filling_session_id', n.get_str_value()),
            "startFilling": lambda n : setattr(self, 'start_filling', n.get_bool_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        from ...document_config_dto import DocumentConfigDto
        from ...editor_configuration_dto import EditorConfigurationDto
        from ...file_dto.system.int32 import Int32

        writer.write_object_value("document", self.document)
        writer.write_str_value("documentType", self.document_type)
        writer.write_object_value("editorConfig", self.editor_config)
        writer.write_int_value("editorType", self.editor_type)
        writer.write_str_value("editorUrl", self.editor_url)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_int_value("file", self.file)
        writer.write_str_value("fillingSessionId", self.filling_session_id)
        writer.write_bool_value("startFilling", self.start_filling)
        writer.write_str_value("token", self.token)
        writer.write_str_value("type", self.type)
    

