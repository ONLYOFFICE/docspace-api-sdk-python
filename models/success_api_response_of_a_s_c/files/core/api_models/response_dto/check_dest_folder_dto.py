from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......a_s_c.files.core.api_models.response_dto.check_dest_folder_dto import CheckDestFolderDto
    from .check_dest_folder_dto_links import CheckDestFolderDto_links

@dataclass
class CheckDestFolderDto(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The count property
    count: Optional[int] = None
    # The links property
    links: Optional[List[CheckDestFolderDto_links]] = None
    # The response property
    response: Optional[CheckDestFolderDto] = None
    # The status property
    status: Optional[int] = None
    # The statusCode property
    status_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckDestFolderDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckDestFolderDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckDestFolderDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......a_s_c.files.core.api_models.response_dto.check_dest_folder_dto import CheckDestFolderDto
        from .check_dest_folder_dto_links import CheckDestFolderDto_links

        from ......a_s_c.files.core.api_models.response_dto.check_dest_folder_dto import CheckDestFolderDto
        from .check_dest_folder_dto_links import CheckDestFolderDto_links

        fields: Dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(CheckDestFolderDto_links)),
            "response": lambda n : setattr(self, 'response', n.get_object_value(CheckDestFolderDto)),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_int_value()),
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
        from ......a_s_c.files.core.api_models.response_dto.check_dest_folder_dto import CheckDestFolderDto
        from .check_dest_folder_dto_links import CheckDestFolderDto_links

        writer.write_int_value("count", self.count)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_object_value("response", self.response)
        writer.write_int_value("status", self.status)
        writer.write_int_value("statusCode", self.status_code)
        writer.write_additional_data_value(self.additional_data)
    

