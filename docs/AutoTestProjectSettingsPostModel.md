# AutoTestProjectSettingsPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_flaky_auto** | **bool** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional] [default to False]
**flaky_stability_percentage** | **int** | Stability percentage for autotest flaky computing | [optional] [default to 100]
**flaky_test_run_count** | **int** | Last test run count for autotest flaky computing | [optional] [default to 100]
**rerun_enabled** | **bool** | Auto rerun enabled | 
**rerun_attempts_count** | **int** | Auto rerun attempt count | 

## Example

```python
from testit_api_client.models.auto_test_project_settings_post_model import AutoTestProjectSettingsPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestProjectSettingsPostModel from a JSON string
auto_test_project_settings_post_model_instance = AutoTestProjectSettingsPostModel.from_json(json)
# print the JSON string representation of the object
print AutoTestProjectSettingsPostModel.to_json()

# convert the object into a dict
auto_test_project_settings_post_model_dict = auto_test_project_settings_post_model_instance.to_dict()
# create an instance of AutoTestProjectSettingsPostModel from a dict
auto_test_project_settings_post_model_from_dict = AutoTestProjectSettingsPostModel.from_dict(auto_test_project_settings_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


