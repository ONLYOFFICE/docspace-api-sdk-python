# SchemaBaseRequestsDto

Team template parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Team template ID | [optional] 

## Example

```python
from docspace.models.schema_base_requests_dto import SchemaBaseRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaBaseRequestsDto from a JSON string
schema_base_requests_dto_instance = SchemaBaseRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SchemaBaseRequestsDto.to_json())

# convert the object into a dict
schema_base_requests_dto_dict = schema_base_requests_dto_instance.to_dict()
# create an instance of SchemaBaseRequestsDto from a dict
schema_base_requests_dto_from_dict = SchemaBaseRequestsDto.from_dict(schema_base_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


