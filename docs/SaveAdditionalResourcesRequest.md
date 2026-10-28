# SaveAdditionalResourcesRequest
Which help and community resources the interface links to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Whether the getting-started documents are offered. | [optional] 
**help_center_enabled** | **bool** | Whether the help center is linked. | [optional] 
**feedback_and_support_enabled** | **bool** | Whether the feedback and support link is shown. | [optional] 
**user_forum_enabled** | **bool** | Whether the user forum is linked. | [optional] 
**video_guides_enabled** | **bool** | Whether the video guides are linked. | [optional] 
**license_agreements_enabled** | **bool** | Whether the license agreements are linked. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.save_additional_resources_request import SaveAdditionalResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAdditionalResourcesRequest from a JSON string
save_additional_resources_request_instance = SaveAdditionalResourcesRequest.from_json(json)
# print the JSON string representation of the object
print(SaveAdditionalResourcesRequest.to_json())

# convert the object into a dict
save_additional_resources_request_dict = save_additional_resources_request_instance.to_dict()
# create an instance of SaveAdditionalResourcesRequest from a dict
save_additional_resources_request_from_dict = SaveAdditionalResourcesRequest.from_dict(save_additional_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


