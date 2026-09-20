# FileLink
The address the content of a file is fetched from, together with the signature that authorises the fetch, as  the document service is handed it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filetype** | **str** | The format the stored content is in, lower-cased and with the leading dot, which is how the document  service learns how to read the bytes behind the address. It stays empty when the file title carries no  extension at all. | 
**token** | **str** | Signs the address and the format above so that the document service can trust them. It stays empty on a  portal that has no signature secret configured for the document service, and the address is then meant  to be fetched unsigned. | [optional] 
**url** | **str** | Where the content is fetched from: the portal download handler, pinned to the revision the file was at  when the address was issued and carrying an authorisation key of limited validity. It is addressed to  the host the document service can reach, which on a deployment with a private editor network is not the  address a browser should follow. | 

## Example

```python
from docspace_api_sdk.models.file_link import FileLink

# TODO update the JSON string below
json = "{}"
# create an instance of FileLink from a JSON string
file_link_instance = FileLink.from_json(json)
# print the JSON string representation of the object
print(FileLink.to_json())

# convert the object into a dict
file_link_dict = file_link_instance.to_dict()
# create an instance of FileLink from a dict
file_link_from_dict = FileLink.from_dict(file_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


