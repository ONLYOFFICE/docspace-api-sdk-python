# ConnectionTestResultDto
The outcome of a connection test against an external database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Specifies whether the connection to the database succeeded. | [optional] 
**error** | **str** | The reason the connection failed, or null when it succeeded. | [optional] 

## Example

```python
from docspace_api_sdk.models.connection_test_result_dto import ConnectionTestResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTestResultDto from a JSON string
connection_test_result_dto_instance = ConnectionTestResultDto.from_json(json)
# print the JSON string representation of the object
print(ConnectionTestResultDto.to_json())

# convert the object into a dict
connection_test_result_dto_dict = connection_test_result_dto_instance.to_dict()
# create an instance of ConnectionTestResultDto from a dict
connection_test_result_dto_from_dict = ConnectionTestResultDto.from_dict(connection_test_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


