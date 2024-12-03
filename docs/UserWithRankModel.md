# UserWithRankModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**middle_name** | **str** |  | 
**user_name** | **str** |  | 
**display_name** | **str** |  | 
**user_type** | **str** |  | 
**avatar_url** | **str** |  | 
**avatar_metadata** | **str** |  | 
**is_deleted** | **bool** |  | 
**is_disabled** | **bool** |  | 
**provider_id** | **str** |  | [optional] 
**is_active_status_by_entity** | **bool** |  | 
**user_rank** | [**UserRankModel**](UserRankModel.md) |  | 

## Example

```python
from testit_api_client.models.user_with_rank_model import UserWithRankModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithRankModel from a JSON string
user_with_rank_model_instance = UserWithRankModel.from_json(json)
# print the JSON string representation of the object
print(UserWithRankModel.to_json())

# convert the object into a dict
user_with_rank_model_dict = user_with_rank_model_instance.to_dict()
# create an instance of UserWithRankModel from a dict
user_with_rank_model_from_dict = UserWithRankModel.from_dict(user_with_rank_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


