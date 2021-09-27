# rhvEventShow

## sample test result

* Add host in cluster
```
Correlation ID : db61af2c-bc1f-40c5-9903-5d35251a62dd
2021-09-26 10:26:55,453-04  DEBUG Server: RunAction invoked!
2021-09-26 10:26:55,453-04  DEBUG Action type 'AddVds', Parameters 'AddVdsActionParameters:{commandId='null', user='null', commandType='Unknown'}'
2021-09-26 10:26:55,453-04  DEBUG IP '172.88.0.1', Session ID 'KiUBEMWmUWu_OpjyyiP322WwB73vFtlJgyZsqt39'
2021-09-26 10:26:55,689-04  DEBUG method: get, params: [3f4cac80-886a-4071-9035-759304528559], timeElapsed: 116ms
2021-09-26 10:26:55,828-04  DEBUG method: getByName, params: [tdc44c01c, 8fabc382-0c2a-4160-94df-632e5a3b93e7], timeElapsed: 53ms
2021-09-26 10:26:55,879-04  DEBUG method: getAllForHostname, params: [tdc44c01c.colso.dl02, 8fabc382-0c2a-4160-94df-632e5a3b93e7], timeElapsed: 50ms
2021-09-26 10:26:55,903-04  DEBUG Connecting 'root@tdc44c01c.colso.dl02'
2021-09-26 10:26:56,144-04  DEBUG Connected: 'root@tdc44c01c.colso.dl02'
2021-09-26 10:26:56,160-04  DEBUG Authenticating: 'root@tdc44c01c.colso.dl02'
2021-09-26 10:26:56,232-04  DEBUG Authenticated: 'root@tdc44c01c.colso.dl02'
2021-09-26 10:26:56,232-04  DEBUG Executing: '/usr/bin/vdsm-tool vdsm-id'
2021-09-26 10:26:58,740-04  DEBUG Executed: '/usr/bin/vdsm-tool vdsm-id'
2021-09-26 10:26:58,794-04  DEBUG method: getAllWithUniqueId, params: [c1c0c8a1-5f54-4469-a204-17074508eb81], timeElapsed: 51ms
2021-09-26 10:26:58,878-04   INFO Running command: AddVdsCommand internal: false. Entities affected :  ID: 8fabc382-0c2a-4160-94df-632e5a3b93e7 Type: ClusterAction group CREATE_HOST with role type ADMIN
```
* Change host state from Management to Maintenance
```
Correlation ID : d78e98ae-7d48-4acf-87ad-3553ff3ecb4f
2021-09-26 10:43:17,737-04  DEBUG Server: RunAction invoked!
2021-09-26 10:43:17,739-04  DEBUG Action type 'MaintenanceNumberOfVdss', Parameters 'MaintenanceNumberOfVdssParameters:{commandId='null', user='null', commandType='Unknown'}'
2021-09-26 10:43:17,740-04  DEBUG IP '172.88.0.1', Session ID 'KiUBEMWmUWu_OpjyyiP322WwB73vFtlJgyZsqt39'
2021-09-26 10:43:17,772-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 8ms
2021-09-26 10:43:17,776-04   INFO Lock Acquired to object 'EngineLock:{exclusiveLocks='', sharedLocks='[9200172f-930e-4255-9b43-44e3f5547548=POOL]'}'
2021-09-26 10:43:17,878-04  DEBUG method: getAllRunningForVds, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 101ms
2021-09-26 10:43:17,895-04  DEBUG method: getAllForCluster, params: [8fabc382-0c2a-4160-94df-632e5a3b93e7], timeElapsed: 7ms
2021-09-26 10:43:17,970-04   INFO Running command: MaintenanceNumberOfVdssCommand internal: false. Entities affected :  ID: 345b29a4-dac0-4f60-be3e-dde1afe1325e Type: VDSAction group MANIPULATE_HOST with role type ADMIN
2021-09-26 10:43:17,981-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 9ms
2021-09-26 10:43:17,982-04   INFO START, SetVdsStatusVDSCommand(HostName = tdc44c01c, SetVdsStatusVDSCommandParameters:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e', status='PreparingForMaintenance', nonOperationalReason='NONE', stopSpmFailureLogged='true', maintenanceReason='null'}), log id: 3a4076ff
2021-09-26 10:43:17,982-04   INFO VDS 'tdc44c01c' is spm and moved from up calling resetIrs.
2021-09-26 10:43:17,984-04   INFO START, ResetIrsVDSCommand( ResetIrsVDSCommandParameters:{storagePoolId='9200172f-930e-4255-9b43-44e3f5547548', ignoreFailoverLimit='false', vdsId='345b29a4-dac0-4f60-be3e-dde1afe1325e', ignoreStopFailed='false'}), log id: 7fc49f31
2021-09-26 10:43:17,994-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 8ms
2021-09-26 10:43:17,994-04   INFO START, SpmStopVDSCommand(HostName = tdc44c01c, SpmStopVDSCommandParameters:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e', storagePoolId='9200172f-930e-4255-9b43-44e3f5547548'}), log id: ebe56dc
2021-09-26 10:43:17,997-04  DEBUG START, HSMGetAllTasksStatusesVDSCommand(HostName = tdc44c01c, VdsIdVDSCommandParametersBase:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e'}), log id: 59496a30
2021-09-26 10:43:17,998-04  DEBUG SEND
                                  ovirtCorrelationId:d78e98ae-7d48-4acf-87ad-3553ff3ecb4f
                                  destination:jms.topic.vdsm_requests
                                  reply-to:jms.topic.vdsm_responses
                                  content-length:109
{
    "params": {},
    "jsonrpc": "2.0",
    "method": "Host.getAllTasksStatuses",
    "id": "aa679c67-e783-48e2-8884-a0de0655c6d7"
}
2021-09-26 10:43:17,998-04  DEBUG Message sent: SEND
                                  destination:jms.topic.vdsm_requests
                                  content-length:109
                                  ovirtCorrelationId:d78e98ae-7d48-4acf-87ad-3553ff3ecb4f
                                  reply-to:jms.topic.vdsm_responses
                                  <JsonRpcRequest id: "aa679c67-e783-48e2-8884-a0de0655c6d7", method: Host.getAllTasksStatuses, params: {}>
2021-09-26 10:43:18,051-04  DEBUG FINISH, HSMGetAllTasksStatusesVDSCommand, return: {}, log id: 59496a30
2021-09-26 10:43:18,052-04   INFO SpmStopVDSCommand::Stopping SPM on vds 'tdc44c01c', pool id '9200172f-930e-4255-9b43-44e3f5547548'
2021-09-26 10:43:18,052-04  DEBUG SEND
                                  ovirtCorrelationId:d78e98ae-7d48-4acf-87ad-3553ff3ecb4f
                                  destination:jms.topic.vdsm_requests
                                  reply-to:jms.topic.vdsm_responses
                                  content-length:158
{
    "params": {
        "storagepoolID": "9200172f-930e-4255-9b43-44e3f5547548"
    },
    "jsonrpc": "2.0",
    "method": "StoragePool.spmStop",
    "id": "00963dd8-2d19-4230-a9dc-e5c461ee71d5"
}
2021-09-26 10:43:18,053-04  DEBUG Message sent: SEND
                                  destination:jms.topic.vdsm_requests
                                  content-length:158
                                  ovirtCorrelationId:d78e98ae-7d48-4acf-87ad-3553ff3ecb4f
                                  reply-to:jms.topic.vdsm_responses
                                  <JsonRpcRequest id: "00963dd8-2d19-4230-a9dc-e5c461ee71d5", method: StoragePool.spmStop, params: {storagepoolID=9200172f-930e-4255-9b43-44e3f5547548}>
2021-09-26 10:43:18,144-04   INFO FINISH, SpmStopVDSCommand, return: , log id: ebe56dc
2021-09-26 10:43:18,146-04  DEBUG UNSUBSCRIBE
                                  id:66468f23-c24d-4bfc-b5fa-f822fe0df1f4
2021-09-26 10:43:18,146-04  DEBUG Message sent: UNSUBSCRIBE
                                  id:66468f23-c24d-4bfc-b5fa-f822fe0df1f4
2021-09-26 10:43:18,147-04  DEBUG DISCONNECT
                                  receipt:c5d059eb-f079-4514-905d-66afde960cf1
2021-09-26 10:43:18,147-04  DEBUG Message sent: DISCONNECT
                                  receipt:c5d059eb-f079-4514-905d-66afde960cf1
2021-09-26 10:43:19,032-04   INFO FINISH, ResetIrsVDSCommand, return: , log id: 7fc49f31
2021-09-26 10:43:19,039-04   INFO Clearing domains data for host tdc44c01c
2021-09-26 10:43:19,841-04   INFO FINISH, SetVdsStatusVDSCommand, return: , log id: 3a4076ff
2021-09-26 10:43:19,841-04  DEBUG method: runVdsCommand, params: [SetVdsStatus, SetVdsStatusVDSCommandParameters:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e', status='PreparingForMaintenance', nonOperationalReason='NONE', stopSpmFailureLogged='true', maintenanceReason='null'}], timeElapsed: 1870ms
2021-09-26 10:43:19,846-04   INFO Lock freed to object 'EngineLock:{exclusiveLocks='', sharedLocks='[9200172f-930e-4255-9b43-44e3f5547548=POOL]'}'
2021-09-26 10:43:20,924-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 8ms
2021-09-26 10:43:21,037-04  DEBUG method: getAllRunningForVds, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 113ms
2021-09-26 10:43:21,082-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 10ms
2021-09-26 10:43:21,096-04   INFO Running command: MaintenanceVdsCommand internal: true. Entities affected :  ID: 345b29a4-dac0-4f60-be3e-dde1afe1325e Type: VDS
2021-09-26 10:43:21,132-04   INFO EVENT_ID: USER_VDS_MAINTENANCE_WITHOUT_REASON(620), Host tdc44c01c was switched to Maintenance mode by admin@internal-authz.
2021-09-26 10:43:21,205-04  DEBUG method: runAction, params: [MaintenanceNumberOfVdss, MaintenanceNumberOfVdssParameters:{commandId='f33bec25-1345-44b8-a00e-503561c102fa', user='admin', commandType='Unknown'}], timeElapsed: 3465ms
2021-09-26 10:43:23,990-04   INFO Command 'MaintenanceNumberOfVdss' id: 'f33bec25-1345-44b8-a00e-503561c102fa' child commands '[]' executions were completed, status 'SUCCEEDED'
2021-09-26 10:43:25,019-04   INFO Ending command 'org.ovirt.engine.core.bll.MaintenanceNumberOfVdssCommand' successfully.
```

* Remove host in cluster
```
Correlation ID : a390d81e-4a43-409d-8d59-cbd03d0e85af
2021-09-26 10:43:49,370-04  DEBUG Server: RunMultipleAction invoked! [amount of actions: 1]
2021-09-26 10:43:49,370-04  DEBUG IP '172.88.0.1', Session ID 'KiUBEMWmUWu_OpjyyiP322WwB73vFtlJgyZsqt39'
2021-09-26 10:43:49,382-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 9ms
2021-09-26 10:43:49,399-04   INFO Before acquiring lock-timeout 'EngineLock:{exclusiveLocks='[345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS, VDS_POOL_AND_STORAGE_CONNECTIONS345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS_POOL_AND_STORAGE_CONNECTIONS]', sharedLocks=''}'
2021-09-26 10:43:49,399-04   INFO Lock-timeout acquired to object 'EngineLock:{exclusiveLocks='[345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS, VDS_POOL_AND_STORAGE_CONNECTIONS345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS_POOL_AND_STORAGE_CONNECTIONS]', sharedLocks=''}'
2021-09-26 10:43:49,407-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 7ms
2021-09-26 10:43:49,421-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 8ms
2021-09-26 10:43:49,426-04  DEBUG Executing task: EE-ManagedThreadFactory-engine-Thread-697452
2021-09-26 10:43:49,428-04   INFO Running command: RemoveVdsCommand internal: false. Entities affected :  ID: 345b29a4-dac0-4f60-be3e-dde1afe1325e Type: VDSAction group DELETE_HOST with role type ADMIN
2021-09-26 10:43:49,436-04  DEBUG method: getAllForCluster, params: [8fabc382-0c2a-4160-94df-632e5a3b93e7], timeElapsed: 8ms
2021-09-26 10:43:49,475-04  DEBUG method: getAllPinnedToHost, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 30ms
2021-09-26 10:43:49,570-04  DEBUG method: get, params: [345b29a4-dac0-4f60-be3e-dde1afe1325e], timeElapsed: 4ms
2021-09-26 10:43:49,571-04   INFO START, RemoveVdsVDSCommand( RemoveVdsVDSCommandParameters:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e'}), log id: 63751e7c
2021-09-26 10:43:49,571-04   INFO vdsManager::disposing
2021-09-26 10:43:49,573-04  DEBUG UNSUBSCRIBE
                                  id:acac4616-91cb-41fd-ac36-6749dc01b509
2021-09-26 10:43:49,574-04  DEBUG Message sent: UNSUBSCRIBE
                                  id:acac4616-91cb-41fd-ac36-6749dc01b509
2021-09-26 10:43:49,574-04  DEBUG UNSUBSCRIBE
                                  id:714de1c0-ade0-47f5-9adb-e706fe4de7db
2021-09-26 10:43:49,574-04  DEBUG Message sent: UNSUBSCRIBE
                                  id:714de1c0-ade0-47f5-9adb-e706fe4de7db
2021-09-26 10:43:49,574-04  DEBUG DISCONNECT
                                  receipt:56ed2efd-aa38-4688-add5-3feb55e72e25
2021-09-26 10:43:49,574-04  DEBUG Message sent: DISCONNECT
                                  receipt:56ed2efd-aa38-4688-add5-3feb55e72e25
2021-09-26 10:43:49,575-04   INFO FINISH, RemoveVdsVDSCommand, return: , log id: 63751e7c
2021-09-26 10:43:49,575-04  DEBUG method: runVdsCommand, params: [RemoveVds, RemoveVdsVDSCommandParameters:{hostId='345b29a4-dac0-4f60-be3e-dde1afe1325e'}], timeElapsed: 9ms
2021-09-26 10:43:49,603-04   INFO EVENT_ID: VDS_ANSIBLE_HOST_REMOVE_STARTED(562), Ansible host-remove playbook execution started on host tdc44c01c.
2021-09-26 10:44:02,050-04   INFO EVENT_ID: ANSIBLE_RUNNER_EVENT_NOTIFICATION(559), Ansible Runner.. Gathering Facts.
2021-09-26 10:44:08,176-04   INFO EVENT_ID: ANSIBLE_RUNNER_EVENT_NOTIFICATION(559), Ansible Runner.. Check if ovirt-provider-ovn-driver is installed.
2021-09-26 10:44:11,240-04   INFO EVENT_ID: ANSIBLE_RUNNER_EVENT_NOTIFICATION(559), Ansible Runner.. Unconfigure the OVN chassis.
2021-09-26 10:44:14,322-04   INFO EVENT_ID: ANSIBLE_RUNNER_EVENT_NOTIFICATION(559), Ansible Runner.. Checks hosted engine configuration file.
2021-09-26 10:44:20,434-04   INFO EVENT_ID: VDS_ANSIBLE_HOST_REMOVE_FINISHED(563), Ansible host-remove playbook execution has successfully finished on host tdc44c01c. For more details check log /var/log/ovirt-engine/ansible/ansible-20210926104349-ovirt-host-remove_yml-a390d81e-4a43-409d-8d59-cbd03d0e85af.log
2021-09-26 10:44:20,452-04   INFO EVENT_ID: USER_REMOVE_VDS(44), Host tdc44c01c was removed by admin@internal-authz.
2021-09-26 10:44:20,455-04   INFO Lock freed to object 'EngineLock:{exclusiveLocks='[345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS, VDS_POOL_AND_STORAGE_CONNECTIONS345b29a4-dac0-4f60-be3e-dde1afe1325e=VDS_POOL_AND_STORAGE_CONNECTIONS]', sharedLocks=''}'
```
