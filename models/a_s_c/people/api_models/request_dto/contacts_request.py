from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....web.api.models.contact import Contact

@dataclass
class ContactsRequest(Parsable):
    """
    Parameters for updating user contacts
    """
    # List of user contacts
    contacts: Optional[List[Contact]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContactsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContactsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContactsRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....web.api.models.contact import Contact

        from ....web.api.models.contact import Contact

        fields: Dict[str, Callable[[Any], None]] = {
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
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
        from ....web.api.models.contact import Contact

        writer.write_collection_of_object_values("contacts", self.contacts)
    

