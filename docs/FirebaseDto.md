# FirebaseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key | [optional] 
**auth_domain** | **str** | Authentication domain | [optional] 
**project_id** | **str** | Project ID | [optional] 
**storage_bucket** | **str** | Storage bucket | [optional] 
**messaging_sender_id** | **str** | Message sender ID | [optional] 
**app_id** | **str** | Application ID | [optional] 
**measurement_id** | **str** | Measurement ID | [optional] 
**database_url** | **str** | Database URL | [optional] 

## Example

```python
from docspace.models.firebase_dto import FirebaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FirebaseDto from a JSON string
firebase_dto_instance = FirebaseDto.from_json(json)
# print the JSON string representation of the object
print(FirebaseDto.to_json())

# convert the object into a dict
firebase_dto_dict = firebase_dto_instance.to_dict()
# create an instance of FirebaseDto from a dict
firebase_dto_from_dict = FirebaseDto.from_dict(firebase_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


