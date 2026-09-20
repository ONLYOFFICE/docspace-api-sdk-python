# FileReference
The file reference parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**FileReferenceData**](FileReferenceData.md) | How this document is named when another spreadsheet refers to it. Send it back as it stands to resolve the  reference again. | [optional] 
**error** | **str** | Filled in when the reference resolved to nothing; the rest of the descriptor is then empty and must not be  handed to the editors. | [optional] 
**path** | **str** | The title of the document the reference resolved to. | [optional] 
**url** | **str** | Where the content is fetched from. It is addressed to the host the document service can reach, which on a  deployment with a private editor network is not the address a browser should follow. | [optional] 
**file_type** | **str** | The format the content is in, without the leading dot. | [optional] 
**key** | **str** | Identifies the exact revision to the editors: two clients that receive the same key read the same co-editing  session, and the key changes as soon as the document is saved. | [optional] 
**link** | **str** | The address of the document in the portal web editor - the link to put in front of a person, unlike the  download address above. | [optional] 
**token** | **str** | Signs this descriptor so that the editors can trust it. It stays empty on a portal that has no signature  secret configured for the document service. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_reference import FileReference

# TODO update the JSON string below
json = "{}"
# create an instance of FileReference from a JSON string
file_reference_instance = FileReference.from_json(json)
# print the JSON string representation of the object
print(FileReference.to_json())

# convert the object into a dict
file_reference_dict = file_reference_instance.to_dict()
# create an instance of FileReference from a dict
file_reference_from_dict = FileReference.from_dict(file_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


