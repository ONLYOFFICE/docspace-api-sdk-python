# CheckConversionRequestDto
The parameters of one file conversion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | The file to convert. It is taken from the route of the operation, so a value sent in the body is overwritten. | [optional] 
**sync** | **bool** | How to wait for the result: `true` converts inside the request and answers with the finished result, which is  only sensible for small documents, while `false` queues the conversion and answers with an entry to poll. | [optional] 
**start_convert** | **bool** | Whether the conversion is to be started. It is set by the operation itself, so a value sent in the body is  overwritten. | [optional] 
**version** | **int** | The version to convert; 0 or less means the current version. | [optional] 
**password** | **str** | The password that opens the source document, for a file that is protected by one; anything else may be left  out. | [optional] 
**output_type** | **str** | The extension of the format to convert into, without the dot, and one the portal can produce from that  source format; left out, the default of the portal for that kind of document is used. | [optional] 
**create_new_if_exist** | **bool** | Where the result goes when the file has been converted before: `true` creates another file beside the source,  `false` replaces the converted file that already exists. | [optional] 

## Example

```python
from docspace_api_sdk.models.check_conversion_request_dto import CheckConversionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckConversionRequestDto from a JSON string
check_conversion_request_dto_instance = CheckConversionRequestDto.from_json(json)
# print the JSON string representation of the object
print(CheckConversionRequestDto.to_json())

# convert the object into a dict
check_conversion_request_dto_dict = check_conversion_request_dto_instance.to_dict()
# create an instance of CheckConversionRequestDto from a dict
check_conversion_request_dto_from_dict = CheckConversionRequestDto.from_dict(check_conversion_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


