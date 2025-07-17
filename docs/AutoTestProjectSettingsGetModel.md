# AutoTestProjectSettingsGetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unique ID of the project. | 
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional] [default to False]
**flaky_stability_percentage** | **int** | Stability percentage for autotest flaky computing | [optional] [default to 100]
**flaky_test_run_count** | **int** | Last test run count for autotest flaky computing | [optional] [default to 100]
**rerun_enabled** | **bool** | Auto rerun enabled | 
**rerun_attempts_count** | **int** | Auto rerun attempt count | 

## Example

```python
from testit_api_client.models.auto_test_project_settings_get_model import AutoTestProjectSettingsGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestProjectSettingsGetModel from a JSON string
auto_test_project_settings_get_model_instance = AutoTestProjectSettingsGetModel.from_json(json)
# print the JSON string representation of the object
print AutoTestProjectSettingsGetModel.to_json()

# convert the object into a dict
auto_test_project_settings_get_model_dict = auto_test_project_settings_get_model_instance.to_dict()
# create an instance of AutoTestProjectSettingsGetModel from a dict
auto_test_project_settings_get_model_from_dict = AutoTestProjectSettingsGetModel.from_dict(auto_test_project_settings_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


