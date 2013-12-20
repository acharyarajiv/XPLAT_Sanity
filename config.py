config = {

"PUBLISHSETTINGS_FILE" : "D:\\Xplat_Phy\\Subs.publishsettings",

#************** ACCOUNT VARIABLES *****************

"LOG_FILE" : "D:\\Xplat_Phy\\Test_Summary.log",

"FILE_PATH" : "D:\\Xplat_Phy\\Role_Info.json",

"CERT_FILE" : "D:\\Xplat_Phy\\File_Cert.pem",

#************** ACCOUNT VARIABLES *****************

"SUBSCRIPTION_ID" : "db1ab6f0-4769-4b27-930e-01e2ef9c123c",

"CONFIG_KEY" : "Key",

"CONFIG_VALUE" : "Value",

#************** VM VARIABLES *****************
"VM_NAME" : "OffshoreTestXplat",
"VM_VNET_NAME" : "OffshoreTestVNet",
"VM_VNET_LABEL" : "Offshore_vnet_img_vm",
"VM_SIZE_NAME" : "OffshoreTestSize",
"VM_COMM_NAME" : "OffshoreTestComm",
"VM_SSH_NAME" : "OffshoreTestSsh",

"IMAGE_NAME" :"Some Linux Image Name",
"WIN_IMAGE_NAME" :"Some Windows Image Name",
"VM_VNET_IMAGE_NAME" :"OffshoreTestImage002",
"VM_COMM_IMAGE_NAME" :"vmdepot-2440-6-1",

"USER_NAME" :"OffshoreTestUser",
"PASSWORD" :"Pa$$word@123" ,
"LOCATION":'"West US"',

"VM_BLOB_URL":"http://acsforsdk2.blob.core.windows.net/disks/OffshoreTestVM002.vhd",

#************** VM IMAGE VARIABLES *****************
"AFFINITY_GRP_NAME":"OffshoreTestAffinGrp",
"AFFINITY_GRP_LABEL":"OffshoreTestGrp",
"AFFINITY_GRP_DESC":'"Test Offshore Affinity Group"',
#************** VM NETWORK VARIABLES *****************
"NETWORK_NAME":"offshoreTestNetwork",

#************** VM IMAGE VARIABLES *****************
"VM_IMAGE_NAME" : "OffshoreTestImage002",
"VM_IMAGE_LABEL" : "OffshoreTestImage",
"VM_IMAGE_DESC" : '"Test Offshore Image"',
"VM_DISK_SOURCE_PATH" :"http://acsforsdk2.blob.core.windows.net/vhd-store/OffshoreTestXplat-d0f0d5b80477e5e9.vhd",
"IMAGE_BLOB_URL" :"http://acsforsdk2.blob.core.windows.net/vm-images/OffshoreTestImage002.vhd" ,
"TARGET_IMG_NAME" : "OffshoreTestImage003",

#************** VM DISK IMAGE VARIABLES *****************
"VM_DISK_IMAGE_NAME" :"OffshoreTestDiskImage002",
"VM_DISK_NEW_IMAGE_NAME" :"OffshoreTestDiskImage003",
"VM_DISK_LABEL" : "OffshoreTestDisk",
"VM_DISK_NEW_LABEL" : "OffshoreTestDisk001",
"VM_DISK_DESC" : '"Test Offshore Disk"',
"DISK_IMAGE_BLOB_URL":"http://acsforsdk2.blob.core.windows.net/disks/OffshoreTestDiskImage002.vhd",
"VM_DISK_ATTACH_BLOB_URL": "http://acsforsdk2.blob.core.windows.net/disks/OffshoreTestDiskImage003.vhd",

#************** VM DISK UPLOAD VARIABLES *****************
"DISK_UPLOAD_BLOB_URL":"http://acsforsdk2.blob.core.windows.net/disks/OffshoreTestDiskImage002.vhd",
"DISK_UPLOAD_SOURCE_PATH" : "http://acsforsdk2.blob.core.windows.net/vm-images/OffshoreTestImage002.vhd",
"STORAGE_ACCOUNT_KEY":"YW55IGNhcm5hbCBwbGVhc3VyZQ==",

#************** MULTIPLE ENDPOINT VALUES **************************
"ONLYPP_PUBLICPORT":"3333",

"PPANDLP_PUBLICPORT":"4444",
"PPANDLP_LOCALPORT":"4454",

"PP_LPANDLBSET_PUBLICPORT":"5555",
"PP_LPANDLBSET_LOCALPORT":"5565",
"PP_LPANDLBSET_PROTOCOL":"tcp",
"PP_LPANDLBSET_ENABLEDIRECTSERVERRETURN":"false",
"PP_LPANDLBSET_LOADBALANCERSETNAME":"LbSet1",

"PP_LP_LBSETANDPROB_PUBLICPORT":"6666",
"PP_LP_LBSETANDPROB_LOCALPORT":"6676",
"PP_LP_LBSETANDPROB_PROTOCOL":"tcp",
"PP_LP_LBSETANDPROB_ENABLEDIRECTSERVERRETURN":"false",
"PP_LP_LBSETANDPROB_LOADBALANCERSETNAME":"LbSet2",
"PP_LP_LBSETANDPROB_PROBPROTOCOL":"http",
"PP_LP_LBSETANDPROB_PROBPORT":"7777",
"PP_LP_LBSETANDPROB_PROBPATH":"/prob/listner1",

#************** FLAG VALUES **************************

"GLOBAL_FLAG" : "0",

# NPM FLAGS

"NPM_CLEAR_FLAG" : "0" ,
"NPM_INSTALL_FLAG" : "0" ,

# ACCOUNT FLAGS 

"AZURE_HELP_FLAG" : "1" ,
"ACCOUNT_DWNLD_FLAG" : "1" ,
"ACCOUNT_IMPRT_FLAG" : "1" ,
"ACCOUNT_LIST_FLAG" : "1" ,
"ACCOUNT_SET_FLAG" : "1" ,
"ACCOUNT_AFF_GRP_FLAG" : "1" ,
"ACCOUNT_AFF_GRP_CREATE_FLAG" : "1" ,
"ACCOUNT_AFF_GRP_SHOW_FLAG" : "1" ,
"ACCOUNT_STORAGE_LIST_FLAG" : "1" ,
"ACCOUNT_CONFIG_LIST_FLAG" : "1" ,
"ACCOUNT_CONFIG_SET_FLAG" : "1" ,
"AZURE_SERV_LIST_FLAG" : "1" ,
"AZURE_LOC_LIST_FLAG" : "1" ,
"AZURE_SERVICE_DEL_FLAG" : "1" ,
"ACCOUNT_CLEAR_FLAG" : "1" ,

# VM FLAGS

"VM_CREATE_FLAG" : "1" ,
"VM_VNET_CREATE_FLAG" : "1" ,
"VM_SIZE_CREATE_FLAG" : "1" ,
"VM_COMM_IMG_CREATE_FLAG" : "1" ,
"VM_SSH_FLAG" : "1" ,
"VM_EXPORT_FLAG" : "1" ,
"VM_CAPTURE_FLAG" : "1" ,
"VM_CREATE_FROM_FLAG" : "1" ,
"VM_LIST_FLAG" : "1" ,
"VM__SHOW_FLAG" : "1" ,
"VM_SHUTDWN_FLAG" : "1" ,
"VM_START_FLAG" : "1" ,
"VM_RESTART_FLAG" : "1" ,
"VM_ENDPNT_CREATE_FLAG" : "1" ,
"VM_ENDPNT_CREATE_MUL_FLAG" : "1" ,
"VM_ENDPNT_SHOW_FLAG" : "1" ,
"VM_ENDPNT_LIST_FLAG" : "1" ,
"VM_ENDPNT_UPD_FLAG" : "1" ,
"VM_ENDPNT_DEL_FLAG" : "1" ,
"VM_DEL_FLAG" : "1" ,
"VM_AFFINITY_DEL_FLAG" : "1" ,
"VM_VNET_DEL_FLAG" : "1" ,
"VM_SIZE_DEL_FLAG" : "1" ,
"VM_COMM_DEL_FLAG" : "1" ,
"VM_SSH_DEL_FLAG" : "1" ,

# IMAGE FLAGS

"IMAGE_CREATE_FLAG" : "1" ,
"IMAGE_LIST_FLAG" : "1" ,
"IMAGE_SHOW_FLAG" : "1" ,
"IMAGE_DEL_FLAG" : "1" ,

# DISK FLAGS

"DISK_LIST_FLAG" : "1" ,
"DISK_CREATE_FLAG" : "1" ,
"DISK_ATTCH_FLAG" : "1" ,
"DISK_ATTCH_NEW_FLAG" : "1" ,
"DISK_DETACH_FLAG" : "1" ,
"DISK_SHOW_FLAG" : "1" ,
"DISK_UPLOAD_FLAG" : "1 " ,
"NETWORK_CREATE_FLAG" : "1" ,
"NETWORK_DELETE_FLAG" : "1" ,
"DISK_DEL_FLAG" : "1" ,

}
