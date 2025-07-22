# GetReferenceDataDtoInteger
The request parameters for getting reference data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **str** | The unique document identifier used by the service to get a link to the file. | 
**instance_id** | **str** | The unique system identifier. | [optional] 
**source_file_id** | **int** | The source file ID. | [optional] 
**path** | **str** | The file name or relative path for the formula editor. | [optional] 
**link** | **str** | The file link. | [optional] 

## Example

```python
from docspace-api-sdk.models.get_reference_data_dto_integer import GetReferenceDataDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceDataDtoInteger from a JSON string
get_reference_data_dto_integer_instance = GetReferenceDataDtoInteger.from_json(json)
# print the JSON string representation of the object
print(GetReferenceDataDtoInteger.to_json())

# convert the object into a dict
get_reference_data_dto_integer_dict = get_reference_data_dto_integer_instance.to_dict()
# create an instance of GetReferenceDataDtoInteger from a dict
get_reference_data_dto_integer_from_dict = GetReferenceDataDtoInteger.from_dict(get_reference_data_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


