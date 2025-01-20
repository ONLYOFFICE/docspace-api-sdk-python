from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....web.files.services.document_service.file_reference_data import FileReferenceData
    from .....web.files.services.document_service.options import Options
    from .....web.files.services.document_service.permissions_config import PermissionsConfig
    from .info_config_dto import InfoConfigDto

@dataclass
class DocumentConfigDto(Parsable):
    # File type
    file_type: Optional[str] = None
    # The info property
    info: Optional[InfoConfigDto] = None
    # Is linked for me
    is_linked_for_me: Optional[bool] = None
    # Key
    key: Optional[str] = None
    # The options property
    options: Optional[Options] = None
    # The permissions property
    permissions: Optional[PermissionsConfig] = None
    # The referenceData property
    reference_data: Optional[FileReferenceData] = None
    # Shared link key
    shared_link_key: Optional[str] = None
    # Shared link param
    shared_link_param: Optional[str] = None
    # Title
    title: Optional[str] = None
    # Url
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentConfigDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentConfigDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentConfigDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....web.files.services.document_service.file_reference_data import FileReferenceData
        from .....web.files.services.document_service.options import Options
        from .....web.files.services.document_service.permissions_config import PermissionsConfig
        from .info_config_dto import InfoConfigDto

        from .....web.files.services.document_service.file_reference_data import FileReferenceData
        from .....web.files.services.document_service.options import Options
        from .....web.files.services.document_service.permissions_config import PermissionsConfig
        from .info_config_dto import InfoConfigDto

        fields: Dict[str, Callable[[Any], None]] = {
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "info": lambda n : setattr(self, 'info', n.get_object_value(InfoConfigDto)),
            "isLinkedForMe": lambda n : setattr(self, 'is_linked_for_me', n.get_bool_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_object_value(Options)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_object_value(PermissionsConfig)),
            "referenceData": lambda n : setattr(self, 'reference_data', n.get_object_value(FileReferenceData)),
            "sharedLinkKey": lambda n : setattr(self, 'shared_link_key', n.get_str_value()),
            "sharedLinkParam": lambda n : setattr(self, 'shared_link_param', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        from .....web.files.services.document_service.file_reference_data import FileReferenceData
        from .....web.files.services.document_service.options import Options
        from .....web.files.services.document_service.permissions_config import PermissionsConfig
        from .info_config_dto import InfoConfigDto

        writer.write_str_value("fileType", self.file_type)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isLinkedForMe", self.is_linked_for_me)
        writer.write_str_value("key", self.key)
        writer.write_object_value("options", self.options)
        writer.write_object_value("permissions", self.permissions)
        writer.write_object_value("referenceData", self.reference_data)
        writer.write_str_value("sharedLinkKey", self.shared_link_key)
        writer.write_str_value("sharedLinkParam", self.shared_link_param)
        writer.write_str_value("title", self.title)
        writer.write_str_value("url", self.url)
    

