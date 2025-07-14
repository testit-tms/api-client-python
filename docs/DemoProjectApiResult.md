# DemoProjectApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Demo project ID | 
**project_global_id** | **int** | Demo project global ID | 
**job_id** | **str** | Job ID | 

## Example

```python
from testit_api_client.models.demo_project_api_result import DemoProjectApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of DemoProjectApiResult from a JSON string
demo_project_api_result_instance = DemoProjectApiResult.from_json(json)
# print the JSON string representation of the object
print DemoProjectApiResult.to_json()

# convert the object into a dict
demo_project_api_result_dict = demo_project_api_result_instance.to_dict()
# create an instance of DemoProjectApiResult from a dict
demo_project_api_result_from_dict = DemoProjectApiResult.from_dict(demo_project_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


