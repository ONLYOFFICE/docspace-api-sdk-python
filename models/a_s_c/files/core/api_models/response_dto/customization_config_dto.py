from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....web.files.services.document_service.feedback_config import FeedbackConfig
    from .....web.files.services.document_service.goback_config import GobackConfig
    from .anonymous_config_dto import AnonymousConfigDto
    from .customer_config_dto import CustomerConfigDto
    from .logo_config_dto import LogoConfigDto

@dataclass
class CustomizationConfigDto(Parsable):
    # About
    about: Optional[bool] = None
    # The anonymous property
    anonymous: Optional[AnonymousConfigDto] = None
    # The customer property
    customer: Optional[CustomerConfigDto] = None
    # The feedback property
    feedback: Optional[FeedbackConfig] = None
    # Forcesave
    forcesave: Optional[bool] = None
    # The goback property
    goback: Optional[GobackConfig] = None
    # The logo property
    logo: Optional[LogoConfigDto] = None
    # MentionShare
    mention_share: Optional[bool] = None
    # Review display
    review_display: Optional[str] = None
    # Submit form
    submit_form: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomizationConfigDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomizationConfigDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomizationConfigDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....web.files.services.document_service.feedback_config import FeedbackConfig
        from .....web.files.services.document_service.goback_config import GobackConfig
        from .anonymous_config_dto import AnonymousConfigDto
        from .customer_config_dto import CustomerConfigDto
        from .logo_config_dto import LogoConfigDto

        from .....web.files.services.document_service.feedback_config import FeedbackConfig
        from .....web.files.services.document_service.goback_config import GobackConfig
        from .anonymous_config_dto import AnonymousConfigDto
        from .customer_config_dto import CustomerConfigDto
        from .logo_config_dto import LogoConfigDto

        fields: Dict[str, Callable[[Any], None]] = {
            "about": lambda n : setattr(self, 'about', n.get_bool_value()),
            "anonymous": lambda n : setattr(self, 'anonymous', n.get_object_value(AnonymousConfigDto)),
            "customer": lambda n : setattr(self, 'customer', n.get_object_value(CustomerConfigDto)),
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(FeedbackConfig)),
            "forcesave": lambda n : setattr(self, 'forcesave', n.get_bool_value()),
            "goback": lambda n : setattr(self, 'goback', n.get_object_value(GobackConfig)),
            "logo": lambda n : setattr(self, 'logo', n.get_object_value(LogoConfigDto)),
            "mentionShare": lambda n : setattr(self, 'mention_share', n.get_bool_value()),
            "reviewDisplay": lambda n : setattr(self, 'review_display', n.get_str_value()),
            "submitForm": lambda n : setattr(self, 'submit_form', n.get_bool_value()),
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
        from .....web.files.services.document_service.feedback_config import FeedbackConfig
        from .....web.files.services.document_service.goback_config import GobackConfig
        from .anonymous_config_dto import AnonymousConfigDto
        from .customer_config_dto import CustomerConfigDto
        from .logo_config_dto import LogoConfigDto

        writer.write_bool_value("about", self.about)
        writer.write_object_value("anonymous", self.anonymous)
        writer.write_object_value("customer", self.customer)
        writer.write_object_value("feedback", self.feedback)
        writer.write_bool_value("forcesave", self.forcesave)
        writer.write_object_value("goback", self.goback)
        writer.write_object_value("logo", self.logo)
        writer.write_bool_value("mentionShare", self.mention_share)
        writer.write_str_value("reviewDisplay", self.review_display)
        writer.write_bool_value("submitForm", self.submit_form)
    

