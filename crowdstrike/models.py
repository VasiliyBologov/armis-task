from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator

import lib

class Policy(BaseModel):
    policy_type: str
    policy_id: str
    applied: bool
    settings_hash: Optional[str] = None
    assigned_date: Optional[datetime] = None
    applied_date: Optional[datetime] = None
    rule_groups: Optional[List[Any]] = None
    uninstall_protection: Optional[str] = None
    rule_set_id: Optional[str] = None

class DevicePolicies(BaseModel):
    prevention: Optional[Policy] = None
    sensor_update: Optional[Policy] = None
    global_config: Optional[Policy] = None
    remote_response: Optional[Policy] = None
    device_control: Optional[Policy] = None
    firewall: Optional[Policy] = None

class Meta(BaseModel):
    version: str
    version_string: str

class CrowdstrikeHosts(BaseModel):
    id: str = Field(alias="_id")
    device_id: str
    cid: str
    agent_load_flags: str
    agent_local_time: datetime
    agent_version: str
    bios_manufacturer: Optional[str] = None
    bios_version: Optional[str] = None
    config_id_base: Optional[str] = None
    config_id_build: Optional[str] = None
    config_id_platform: Optional[str] = None
    cpu_signature: Optional[str] = None
    external_ip: Optional[str] = None
    mac_address: Optional[str] = None
    instance_id: Optional[str] = None
    service_provider: Optional[str] = None
    service_provider_account_id: Optional[str] = None
    hostname: str
    first_seen: datetime
    last_seen: datetime
    local_ip: Optional[str] = None
    major_version: str
    minor_version: str
    os_version: Optional[str] = None
    os_build: Optional[str] = None
    platform_id: str
    platform_name: str
    policies: List[Policy]
    reduced_functionality_mode: str
    device_policies: DevicePolicies
    groups: List[str]
    group_hash: str
    product_type_desc: str
    provision_status: str
    serial_number: str
    status: str
    system_manufacturer: Optional[str] = None
    system_product_name: Optional[str] = None
    tags: List[Any]
    modified_timestamp: datetime
    meta: Meta
    zone_group: Optional[str] = None
    kernel_version: Optional[str] = None
    chassis_type: Optional[str] = None
    chassis_type_desc: Optional[str] = None
    connection_ip: Optional[str] = None
    default_gateway_ip: Optional[str] = None
    connection_mac_address: Optional[str] = None

    @field_validator('modified_timestamp', mode='before')
    @classmethod
    def normalize(cls, value: dict) -> int:
        str_value = value.get('$date')
        return lib.validate_datetime(str_value)