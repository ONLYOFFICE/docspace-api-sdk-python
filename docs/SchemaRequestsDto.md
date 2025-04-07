# SchemaRequestsDto

Team template parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Team template ID | [optional] 
**name** | **str** | Team template name | [optional] 
**user_caption** | **str** | User caption | [optional] 
**users_caption** | **str** | Users caption | [optional] 
**group_caption** | **str** | Group caption | [optional] 
**groups_caption** | **str** | Groups caption | [optional] 
**user_post_caption** | **str** | User status caption | [optional] 
**reg_date_caption** | **str** | Registration date caption | [optional] 
**group_head_caption** | **str** | Group lead caption | [optional] 
**guest_caption** | **str** | Guest caption | [optional] 
**guests_caption** | **str** | Guests caption | [optional] 

## Example

```python
from docspace.models.schema_requests_dto import SchemaRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRequestsDto from a JSON string
schema_requests_dto_instance = SchemaRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SchemaRequestsDto.to_json())

# convert the object into a dict
schema_requests_dto_dict = schema_requests_dto_instance.to_dict()
# create an instance of SchemaRequestsDto from a dict
schema_requests_dto_from_dict = SchemaRequestsDto.from_dict(schema_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


