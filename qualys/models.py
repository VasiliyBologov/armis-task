from datetime import datetime
from typing import List, Optional, Dict, Any, Union

import lib

from pydantic import BaseModel, Field, field_validator

class HostAssetAccountData(BaseModel):
    username: str

class HostAssetAccount(BaseModel):
    HostAssetAccount: HostAssetAccountData

class HostAssetInterfaceData(BaseModel):
    interfaceName: Optional[str] = None
    macAddress: Optional[str] = None
    gatewayAddress: Optional[str] = None
    address: str
    hostname: Optional[str] = None

class HostAssetInterface(BaseModel):
    HostAssetInterface: HostAssetInterfaceData

class HostAssetOpenPortData(BaseModel):
    serviceName: Optional[str] = Field(default="")
    protocol: str
    port: int


class HostAssetOpenPort(BaseModel):
    HostAssetOpenPort: HostAssetOpenPortData

class HostAssetProcessorData(BaseModel):
    name: str
    speed: int

class HostAssetProcessor(BaseModel):
    HostAssetProcessor: HostAssetProcessorData


class HostAssetSoftwareData(BaseModel):
    name: str
    version: str


class HostAssetSoftware(BaseModel):
    HostAssetSoftware: HostAssetSoftwareData


class HostAssetVolumeData(BaseModel):
    name: str
    size: int
    free: int

    @field_validator('size', 'free', mode='before')
    @classmethod
    def normalize(cls, value: Any) -> int:
        if type(value) is dict:
            str_value = value.get('$numberLong')
            return int(str_value)
        elif type(value) is int:
            return value
        else:
            return 0


class HostAssetVolume(BaseModel):
    HostAssetVolume: HostAssetVolumeData


class HostAssetVulnData(BaseModel):
    hostInstanceVulnId: int
    lastFound: datetime
    firstFound: datetime
    qid: int

    @field_validator('hostInstanceVulnId', mode='before')
    @classmethod
    def normalize(cls, value: dict) -> int:
        str_value = value.get('$numberLong')
        return int(str_value)


class HostAssetVuln(BaseModel):
    HostAssetVuln: HostAssetVulnData

class Ec2AssetSourceSimple(BaseModel):
    instanceType: str
    subnetId: str
    imageId: str
    groupName: str
    accountId: str
    macAddress: Optional[str] = None
    createdDate: datetime
    reservationId: str
    instanceId: str
    monitoringEnabled: str
    spotInstance: str
    zone: str
    instanceState: str
    privateDnsName: str
    vpcId: str
    type: str
    availabilityZone: str
    privateIpAddress: str
    firstDiscovered: datetime
    ec2InstanceTags: Dict[str, Any]
    publicIpAddress: str
    lastUpdated: datetime
    region: str
    assetId: int
    groupId: str
    localHostname: str
    publicDnsName: str

    @field_validator('createdDate', 'firstDiscovered', 'lastUpdated', mode='before')
    @classmethod
    def normalize(cls, value: dict) -> int:
        str_value = value.get('$date')
        return lib.validate_datetime(str_value)


class AssetSource(BaseModel):
    pass  # Empty in the provided data

class TagSimpleData(BaseModel):
    id: int
    name: str


class TagSimple(BaseModel):
    TagSimple: TagSimpleData

class AgentInfo(BaseModel):
    location: str
    locationGeoLatitude: str
    lastCheckedIn: datetime
    locationGeoLongtitude: str
    agentVersion: str
    manifestVersion: Dict[str, str]
    activatedModule: str
    activationKey: Dict[str, str]
    agentConfiguration: Dict[str, Any]
    status: str
    chirpStatus: str
    connectedFrom: str
    agentId: str
    platform: str

    @field_validator('lastCheckedIn', mode='before')
    @classmethod
    def normalize(cls, value: dict) -> int:
        str_value = value.get('$date')
        return lib.validate_datetime(str_value)


class SourceInfo(BaseModel):
    list: List[Union[Ec2AssetSourceSimple, AssetSource]] = Field(alias="list")

class Tags(BaseModel):
    list: List[TagSimple] = Field(alias="list")

class HostAsset(BaseModel):
    id: int = Field(alias="_id")
    account: Dict[str, List[HostAssetAccount]] = Field(alias="account")
    address: str
    agentInfo: AgentInfo
    biosDescription: Optional[str] = None
    cloudProvider: Optional[str] = None
    created: str
    dnsHostName: str
    fqdn: str
    isDockerHost: str
    lastComplianceScan: Optional[str] = Field(default="")
    lastLoggedOnUser: Optional[str] = Field(default="")
    lastSystemBoot: str
    lastVulnScan: datetime
    manufacturer: str
    model: str
    modified: str
    name: str
    networkGuid: str
    networkInterface: Dict[str, List[HostAssetInterface]] = Field(alias="networkInterface")
    openPort: Dict[str, List[HostAssetOpenPort]] = Field(alias="openPort")
    os: str
    processor: Dict[str, List[HostAssetProcessor]] = Field(alias="processor")
    qwebHostId: int
    software: Dict[str, List[HostAssetSoftware]] = Field(alias="software")
    sourceInfo: SourceInfo
    tags: Tags
    timezone: str
    totalMemory: int
    trackingMethod: str
    type: str
    volume: Dict[str, List[HostAssetVolume]] = Field(alias="volume")
    vuln: Dict[str, List[HostAssetVuln]] = Field(alias="vuln")

    @field_validator('lastVulnScan', mode='before')
    @classmethod
    def normalize(cls, value: dict) -> int:
        str_value = value.get('$date')
        return lib.validate_datetime(str_value)