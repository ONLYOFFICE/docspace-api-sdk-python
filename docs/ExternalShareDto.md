# ExternalShareDto
The external sharing information and validation data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**id** | **str** | The external data ID. | [optional] 
**title** | **str** | The external data title. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 
**entity_id** | **str** | The unique identifier of the shared entity. | [optional] 
**entry_title** | **str** | The title of the shared entry. | [optional] 
**shared** | **bool** | Specifies whether to share the external data or not. | [optional] 
**link_id** | **str** | The link ID of the external data. | [optional] 
**is_authenticated** | **bool** | Specifies whether the user is authenticated or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.external_share_dto import ExternalShareDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalShareDto from a JSON string
external_share_dto_instance = ExternalShareDto.from_json(json)
# print the JSON string representation of the object
print(ExternalShareDto.to_json())

# convert the object into a dict
external_share_dto_dict = external_share_dto_instance.to_dict()
# create an instance of ExternalShareDto from a dict
external_share_dto_from_dict = ExternalShareDto.from_dict(external_share_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


