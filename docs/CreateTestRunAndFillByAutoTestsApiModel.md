# CreateTestRunAndFillByAutoTestsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**configuration_ids** | **[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**auto_test_external_ids** | **[str]** | Specifies the external ID of the autotest. You can specify several IDs. | 
**name** | **str, none_type** | Specifies the name of the test run. | [optional] 
**description** | **str, none_type** | Specifies the test run description. | [optional] 
**launch_source** | **str, none_type** | Specifies the test run launch source. | [optional] 
**attachments** | [**[AssignAttachmentApiModel], none_type**](AssignAttachmentApiModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**[CreateLinkApiModel], none_type**](CreateLinkApiModel.md) | Collection of links to relate to the test run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


