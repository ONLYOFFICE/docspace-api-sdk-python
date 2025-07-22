# CheckConversionRequestDtoInteger
The parameters for checking file conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | The file ID to check conversion proccess. | [optional] 
**sync** | **bool** | Specifies if the conversion process is synchronous or not. | [optional] 
**start_convert** | **bool** | Specifies whether to start a conversion process or not. | [optional] 
**version** | **int** | The file version that is converted. | [optional] 
**password** | **str** | The password of the converted file. | [optional] 
**output_type** | **str** | The conversion output type. | [optional] 
**create_new_if_exist** | **bool** | Specifies whether to create a new file if it exists or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.check_conversion_request_dto_integer import CheckConversionRequestDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of CheckConversionRequestDtoInteger from a JSON string
check_conversion_request_dto_integer_instance = CheckConversionRequestDtoInteger.from_json(json)
# print the JSON string representation of the object
print(CheckConversionRequestDtoInteger.to_json())

# convert the object into a dict
check_conversion_request_dto_integer_dict = check_conversion_request_dto_integer_instance.to_dict()
# create an instance of CheckConversionRequestDtoInteger from a dict
check_conversion_request_dto_integer_from_dict = CheckConversionRequestDtoInteger.from_dict(check_conversion_request_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


