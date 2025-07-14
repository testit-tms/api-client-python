# UserRankModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | 
**work_items_created** | **int** |  | 
**passed_test_points** | **int** |  | 
**failed_test_points** | **int** |  | 
**skipped_test_points** | **int** |  | 
**blocked_test_points** | **int** |  | 
**level_avatar_enabled** | **bool** |  | 

## Example

```python
from testit_api_client.models.user_rank_model import UserRankModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserRankModel from a JSON string
user_rank_model_instance = UserRankModel.from_json(json)
# print the JSON string representation of the object
print UserRankModel.to_json()

# convert the object into a dict
user_rank_model_dict = user_rank_model_instance.to_dict()
# create an instance of UserRankModel from a dict
user_rank_model_from_dict = UserRankModel.from_dict(user_rank_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


