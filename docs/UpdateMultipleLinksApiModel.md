# UpdateMultipleLinksApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionUpdate**](ActionUpdate.md) |  | 
**links** | [**List[CreateLinkApiModel]**](CreateLinkApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.update_multiple_links_api_model import UpdateMultipleLinksApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMultipleLinksApiModel from a JSON string
update_multiple_links_api_model_instance = UpdateMultipleLinksApiModel.from_json(json)
# print the JSON string representation of the object
print UpdateMultipleLinksApiModel.to_json()

# convert the object into a dict
update_multiple_links_api_model_dict = update_multiple_links_api_model_instance.to_dict()
# create an instance of UpdateMultipleLinksApiModel from a dict
update_multiple_links_api_model_from_dict = UpdateMultipleLinksApiModel.from_dict(update_multiple_links_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


