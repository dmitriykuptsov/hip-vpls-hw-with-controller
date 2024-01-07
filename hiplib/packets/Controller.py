#!/usr/bin/python3

# Copyright (C) 2019 strangebit

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class ControllerPacket():
    def __init__(self):
        pass

HEART_BEAT_TYPE = 1
HEART_BEAT_TYPE_OFFSSET = 0
HEART_BEAT_TYPE_LENGTH = 4
HEART_BEAT_LENGTH_OFFSET = 4
HEART_BEAT_LENGTH_LENGTH = 4
HEART_BEAT_HMAC_OFFSET = 8
HEART_BEAT_HMAC_LENGTH = 32
HEART_BEAT_NONCE_OFFSET = 40
HEART_BEAT_NONCE_LENGTH = 4
HEART_BEAT_HIT_OFFSET = 44
HEART_BEAT_HIT_LENGTH = 16
HEART_BEAT_IP_OFFSET = 60
HEART_BEAT_IP_LENGTH = 4

class HeartbeatPacket(ControllerPacket):
    def __init__(self, buffer):
        if not buffer:
            self.buffer = bytearray([0] * (HEART_BEAT_TYPE_LENGTH +
                                           HEART_BEAT_LENGTH_LENGTH +
                                           HEART_BEAT_HMAC_LENGTH +
                                           HEART_BEAT_NONCE_LENGTH +
                                           HEART_BEAT_HIT_LENGTH +
                                           HEART_BEAT_IP_LENGTH))
        else:
            self.buffer = buffer
    def set_packet_type(self, type):
        self.buffer[HEART_BEAT_TYPE_OFFSSET] = (type >> 24) & 0xFF;
        self.buffer[HEART_BEAT_TYPE_OFFSSET + 1] = (type >> 16) & 0xFF;
        self.buffer[HEART_BEAT_TYPE_OFFSSET + 2] = (type >> 8) & 0xFF;
        self.buffer[HEART_BEAT_TYPE_OFFSSET + 3] = type & 0xFF;
    def get_packet_type(self):
        type = 0
        type = self.buffer[HEART_BEAT_TYPE_OFFSSET]
        type = (type << 8) | self.buffer[HEART_BEAT_TYPE_OFFSSET + 1];
        type = (type << 8) | self.buffer[HEART_BEAT_TYPE_OFFSSET + 2];
        type = (type << 8) | self.buffer[HEART_BEAT_TYPE_OFFSSET + 3];
        return type
    def set_packet_length(self, length):
        self.buffer[HEART_BEAT_LENGTH_OFFSET] = (length >> 24) & 0xFF;
        self.buffer[HEART_BEAT_LENGTH_OFFSET + 1] = (length >> 16) & 0xFF;
        self.buffer[HEART_BEAT_LENGTH_OFFSET + 2] = (length >> 8) & 0xFF;
        self.buffer[HEART_BEAT_LENGTH_OFFSET + 3] = length & 0xFF;
    def get_packet_type(self):
        length = 0
        length = self.buffer[HEART_BEAT_LENGTH_OFFSET]
        length = (length << 8) | self.buffer[HEART_BEAT_LENGTH_OFFSET + 1];
        length = (length << 8) | self.buffer[HEART_BEAT_LENGTH_OFFSET + 2];
        length = (length << 8) | self.buffer[HEART_BEAT_LENGTH_OFFSET + 3];
        return length
    def set_hmac(self, hmac):
        self.buffer[HEART_BEAT_HMAC_OFFSET:HEART_BEAT_HMAC_OFFSET + HEART_BEAT_HMAC_LENGTH] = hmac
    def get_hmac(self):
        return self.buffer[HEART_BEAT_HMAC_OFFSET:HEART_BEAT_HMAC_OFFSET + HEART_BEAT_HMAC_LENGTH]
    def set_nonce(self, nonce):
        self.buffer[HEART_BEAT_NONCE_OFFSET:HEART_BEAT_NONCE_OFFSET + HEART_BEAT_NONCE_LENGTH] = nonce
    def get_nonce(self):
        return self.buffer[HEART_BEAT_NONCE_OFFSET:HEART_BEAT_NONCE_OFFSET + HEART_BEAT_NONCE_LENGTH]
    def set_hit(self, hit):
        self.buffer[HEART_BEAT_HIT_OFFSET:HEART_BEAT_HIT_OFFSET + HEART_BEAT_HIT_LENGTH] = hit
    def get_hit(self):
        return self.buffer[HEART_BEAT_HIT_OFFSET:HEART_BEAT_HIT_OFFSET + HEART_BEAT_HIT_LENGTH]
    def set_ip(self, ip):
        self.buffer[HEART_BEAT_IP_OFFSET:HEART_BEAT_IP_OFFSET + HEART_BEAT_IP_LENGTH] = ip
    def get_ip(self):
        return self.buffer[HEART_BEAT_IP_OFFSET:HEART_BEAT_IP_OFFSET + HEART_BEAT_IP_LENGTH]
    def get_buffer(self):
        return self.buffer;
    
FIREWALL_CONFIGURATION_TYPE = 2
FIREWALL_CONFIGURATION_TYPE_OFFSSET = 0
FIREWALL_CONFIGURATION_TYPE_LENGTH = 4
FIREWALL_CONFIGURATION_LENGTH_OFFSET = 4
FIREWALL_CONFIGURATION_LENGTH_LENGTH = 4
FIREWALL_CONFIGURATION_HMAC_OFFSET = 8
FIREWALL_CONFIGURATION_HMAC_LENGTH = 32
FIREWALL_CONFIGURATION_NONCE_OFFSET = 40
FIREWALL_CONFIGURATION_NONCE_LENGTH = 4
FIREWALL_CONFIGURATION_NUM_OFFSET = 44
FIREWALL_CONFIGURATION_NUM_LENGTH = 32
FIREWALL_CONFIGURATION_HIT_LENGTH = 16
FIREWALL_CONFIGURATION_RULE_LENGTH = 4

class FirewallConfigurationPacket(ControllerPacket):
    def __init__(self, buffer):
        if not buffer:
            self.buffer = bytearray([0] * (FIREWALL_CONFIGURATION_TYPE_LENGTH +
                                           FIREWALL_CONFIGURATION_LENGTH_LENGTH +
                                           FIREWALL_CONFIGURATION_HMAC_LENGTH +
                                           FIREWALL_CONFIGURATION_NONCE_LENGTH))
        else:
            self.buffer = buffer
    def set_packet_type(self, type):
        self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET] = (type >> 24) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 1] = (type >> 16) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 2] = (type >> 8) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 3] = type & 0xFF;
    def get_packet_type(self):
        type = 0
        type = self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET]
        type = (type << 8) | self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 1];
        type = (type << 8) | self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 2];
        type = (type << 8) | self.buffer[FIREWALL_CONFIGURATION_TYPE_OFFSSET + 3];
        return type
    def set_packet_length(self, length):
        self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET] = (length >> 24) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 1] = (length >> 16) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 2] = (length >> 8) & 0xFF;
        self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 3] = length & 0xFF;
    def get_packet_type(self):
        length = 0
        length = self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET]
        length = (length << 8) | self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 1];
        length = (length << 8) | self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 2];
        length = (length << 8) | self.buffer[FIREWALL_CONFIGURATION_LENGTH_OFFSET + 3];
        return length
    def set_hmac(self, hmac):
        self.buffer[FIREWALL_CONFIGURATION_HMAC_OFFSET:FIREWALL_CONFIGURATION_HMAC_OFFSET + FIREWALL_CONFIGURATION_HMAC_LENGTH] = hmac
    def get_hmac(self):
        return self.buffer[FIREWALL_CONFIGURATION_HMAC_OFFSET:FIREWALL_CONFIGURATION_HMAC_OFFSET + FIREWALL_CONFIGURATION_HMAC_LENGTH]
    def set_nonce(self, nonce):
        self.buffer[FIREWALL_CONFIGURATION_NONCE_OFFSET:FIREWALL_CONFIGURATION_NONCE_OFFSET + FIREWALL_CONFIGURATION_NONCE_LENGTH] = nonce
    def get_nonce(self):
        return self.buffer[FIREWALL_CONFIGURATION_NONCE_OFFSET:FIREWALL_CONFIGURATION_NONCE_OFFSET + FIREWALL_CONFIGURATION_NONCE_LENGTH]
    def get_rules(self):
        num = (self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET] >> 24) & 0xFF
        num = num | ((self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 1] >> 16) & 0xFF)
        num = num | ((self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 2] >> 8) & 0xFF)
        num = num | ((self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 3]) & 0xFF)
        rules = []
        for i in range(0, num):
            hit1 = self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               (FIREWALL_CONFIGURATION_HIT_LENGTH * i):
                               FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 1)].decode()
            hit2 = self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 1):
                               FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               (FIREWALL_CONFIGURATION_NUM_LENGTH + 
                                FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 2))].decode()
            rule = (self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 2)] << 24) 
            rule = (self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 2) + 1] << 16) | rule
            rule = (self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 2) + 2] << 8) | rule
            rule = (self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (i + 2) + 3]) | rule
            rules.append({
                "hit1": hit1,
                "hit2": hit2,
                "rule": rule
            })
        return rules
    
    def set_rules(self, rules, num):
        self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET] = (num >> 24) & 0xFF
        self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 1] = (num >> 16) & 0xFF
        self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 2] = (num >> 8) & 0xFF
        self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 3] =  num & 0xFF
        for i in range(0, num):
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * 2 * i + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i:
                               FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 1) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i] = bytearray(rules[i]["hit1"])
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 1) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i:
                               FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 2) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i] = bytearray(rules[i]["hit2"])
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 2) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i] = (rules[i]["rule"] >> 24) & 0xFF 
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 2) +
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i + 1]  = (rules[i]["rule"]<< 16) & 0xFF
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 2) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i + 2]  = (rules[i]["rule"]<< 8) & 0xFF
            self.buffer[FIREWALL_CONFIGURATION_NUM_OFFSET + 
                               FIREWALL_CONFIGURATION_NUM_LENGTH + 
                               FIREWALL_CONFIGURATION_HIT_LENGTH * (2 * i + 2) + 
                               FIREWALL_CONFIGURATION_RULE_LENGTH * i + 3]  = rules[i]["rule"] & 0xFF
    def get_buffer(self):
        return self.buffer;

HOSTS_CONFIGURATION_TYPE = 3
HOSTS_CONFIGURATION_TYPE_OFFSSET = 0
HOSTS_CONFIGURATION_TYPE_LENGTH = 4
HOSTS_CONFIGURATION_LENGTH_OFFSET = 4
HOSTS_CONFIGURATION_LENGTH_LENGTH = 4
HOSTS_CONFIGURATION_HMAC_OFFSET = 8
HOSTS_CONFIGURATION_HMAC_LENGTH = 32
HOSTS_CONFIGURATION_NONCE_OFFSET = 40
HOSTS_CONFIGURATION_NONCE_LENGTH = 4
HOSTS_CONFIGURATION_NUM_OFFSET = 44
HOSTS_CONFIGURATION_NUM_LENGTH = 32
HOSTS_CONFIGURATION_HIT_LENGTH = 16
HOSTS_CONFIGURATION_IP_LENGTH = 4

class HostsConfigurationPacket(ControllerPacket):
    def __init__(self, buffer):
        if not buffer:
            self.buffer = bytearray([0] * (HOSTS_CONFIGURATION_TYPE_LENGTH +
                                           HOSTS_CONFIGURATION_LENGTH_LENGTH +
                                           HOSTS_CONFIGURATION_HMAC_LENGTH +
                                           HOSTS_CONFIGURATION_NONCE_LENGTH))
        else:
            self.buffer = buffer
    def set_packet_type(self, type):
        self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET] = (type >> 24) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 1] = (type >> 16) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 2] = (type >> 8) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 3] = type & 0xFF;
    def get_packet_type(self):
        type = 0
        type = self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET]
        type = (type << 8) | self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 1];
        type = (type << 8) | self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 2];
        type = (type << 8) | self.buffer[HOSTS_CONFIGURATION_TYPE_OFFSSET + 3];
        return type
    def set_packet_length(self, length):
        self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET] = (length >> 24) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 1] = (length >> 16) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 2] = (length >> 8) & 0xFF;
        self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 3] = length & 0xFF;
    def get_packet_type(self):
        length = 0
        length = self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET]
        length = (length << 8) | self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 1];
        length = (length << 8) | self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 2];
        length = (length << 8) | self.buffer[HOSTS_CONFIGURATION_LENGTH_OFFSET + 3];
        return length
    def set_hmac(self, hmac):
        self.buffer[HOSTS_CONFIGURATION_HMAC_OFFSET:HOSTS_CONFIGURATION_HMAC_OFFSET + HOSTS_CONFIGURATION_HMAC_LENGTH] = hmac
    def get_hmac(self):
        return self.buffer[HOSTS_CONFIGURATION_HMAC_OFFSET:HOSTS_CONFIGURATION_HMAC_OFFSET + HOSTS_CONFIGURATION_HMAC_LENGTH]
    def set_nonce(self, nonce):
        self.buffer[HOSTS_CONFIGURATION_NONCE_OFFSET:HOSTS_CONFIGURATION_NONCE_OFFSET + HOSTS_CONFIGURATION_NONCE_LENGTH] = nonce
    def get_nonce(self):
        return self.buffer[HOSTS_CONFIGURATION_NONCE_OFFSET:HOSTS_CONFIGURATION_NONCE_OFFSET + HOSTS_CONFIGURATION_NONCE_LENGTH]
    def get_hosts(self):
        num = (self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET] >> 24) & 0xFF
        num = num | ((self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 1] >> 16) & 0xFF)
        num = num | ((self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 2] >> 8) & 0xFF)
        num = num | ((self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 3]) & 0xFF)
        hosts = []
        for i in range(0, num):
            hit = self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                               HOSTS_CONFIGURATION_HIT_LENGTH * i +
                               HOSTS_CONFIGURATION_IP_LENGTH * i:
                               HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                               HOSTS_CONFIGURATION_IP_LENGTH * i +
                               HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1)].decode()
            ip = self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH +
                               HOSTS_CONFIGURATION_IP_LENGTH * i + 
                               HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1):
                               HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                               HOSTS_CONFIGURATION_IP_LENGTH * (i + 1) +
                                HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1)].decode()
            
            hosts.append({
                "hit": hit,
                "ip": ip
            })
        return rules
    
    def set_hosts(self, hosts, num):
        self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET] = (num >> 24) & 0xFF
        self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 1] = (num >> 16) & 0xFF
        self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 2] = (num >> 8) & 0xFF
        self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 3] =  num & 0xFF
        for i in range(0, num):
            self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                               (HOSTS_CONFIGURATION_HIT_LENGTH * i):
                               HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                               HOSTS_CONFIGURATION_IP_LENGTH * i +
                               HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1)] = bytearray(hosts[i]["hit"])
            self.buffer[HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                                HOSTS_CONFIGURATION_IP_LENGTH * i +
                               (HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1)):
                               HOSTS_CONFIGURATION_NUM_OFFSET + 
                               HOSTS_CONFIGURATION_NUM_LENGTH + 
                                HOSTS_CONFIGURATION_IP_LENGTH * (i + 1) +
                               HOSTS_CONFIGURATION_HIT_LENGTH * (i + 1)] = bytearray(hosts[i]["ip"])    
    def get_buffer(self):
        return self.buffer;


MESH_CONFIGURATION_TYPE = 2
MESH_CONFIGURATION_TYPE_OFFSSET = 0
MESH_CONFIGURATION_TYPE_LENGTH = 4
MESH_CONFIGURATION_LENGTH_OFFSET = 4
MESH_CONFIGURATION_LENGTH_LENGTH = 4
MESH_CONFIGURATION_HMAC_OFFSET = 8
MESH_CONFIGURATION_HMAC_LENGTH = 32
MESH_CONFIGURATION_NONCE_OFFSET = 40
MESH_CONFIGURATION_NONCE_LENGTH = 4
MESH_CONFIGURATION_NUM_OFFSET = 44
MESH_CONFIGURATION_NUM_LENGTH = 32
MESH_CONFIGURATION_HIT_LENGTH = 16
MESH_CONFIGURATION_RULE_LENGTH = 4

class MeshConfigurationPacket(ControllerPacket):
    def __init__(self, buffer):
        if not buffer:
            self.buffer = bytearray([0] * (MESH_CONFIGURATION_TYPE_LENGTH +
                                           MESH_CONFIGURATION_LENGTH_LENGTH +
                                           MESH_CONFIGURATION_HMAC_LENGTH +
                                           MESH_CONFIGURATION_NONCE_LENGTH))
        else:
            self.buffer = buffer
    def set_packet_type(self, type):
        self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET] = (type >> 24) & 0xFF;
        self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 1] = (type >> 16) & 0xFF;
        self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 2] = (type >> 8) & 0xFF;
        self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 3] = type & 0xFF;
    def get_packet_type(self):
        type = 0
        type = self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET]
        type = (type << 8) | self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 1];
        type = (type << 8) | self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 2];
        type = (type << 8) | self.buffer[MESH_CONFIGURATION_TYPE_OFFSSET + 3];
        return type
    def set_packet_length(self, length):
        self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET] = (length >> 24) & 0xFF;
        self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 1] = (length >> 16) & 0xFF;
        self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 2] = (length >> 8) & 0xFF;
        self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 3] = length & 0xFF;
    def get_packet_type(self):
        length = 0
        length = self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET]
        length = (length << 8) | self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 2];
        length = (length << 8) | self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 1];
        length = (length << 8) | self.buffer[MESH_CONFIGURATION_LENGTH_OFFSET + 3];
        return length
    def set_hmac(self, hmac):
        self.buffer[MESH_CONFIGURATION_HMAC_OFFSET:MESH_CONFIGURATION_HMAC_OFFSET + MESH_CONFIGURATION_HMAC_LENGTH] = hmac
    def get_hmac(self):
        return self.buffer[MESH_CONFIGURATION_HMAC_OFFSET:MESH_CONFIGURATION_HMAC_OFFSET + MESH_CONFIGURATION_HMAC_LENGTH]
    def set_nonce(self, nonce):
        self.buffer[MESH_CONFIGURATION_NONCE_OFFSET:MESH_CONFIGURATION_NONCE_OFFSET + MESH_CONFIGURATION_NONCE_LENGTH] = nonce
    def get_nonce(self):
        return self.buffer[MESH_CONFIGURATION_NONCE_OFFSET:MESH_CONFIGURATION_NONCE_OFFSET + MESH_CONFIGURATION_NONCE_LENGTH]
    def get_mesh(self):
        num = (self.buffer[MESH_CONFIGURATION_NUM_OFFSET] >> 24) & 0xFF
        num = num | ((self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 1] >> 16) & 0xFF)
        num = num | ((self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 2] >> 8) & 0xFF)
        num = num | ((self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 3]) & 0xFF)
        mesh = []
        for i in range(0, num):
            hit1 = self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               (MESH_CONFIGURATION_HIT_LENGTH * 2 * i):
                               MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 1)].decode()
            hit2 = self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 1):
                               MESH_CONFIGURATION_NUM_OFFSET + 
                               (MESH_CONFIGURATION_NUM_LENGTH + 
                                MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 2))].decode()
            
            mesh.append({
                "hit1": hit1,
                "hit2": hit2
            })
        return mesh
    
    def set_rules(self, rules, num):
        self.buffer[MESH_CONFIGURATION_NUM_OFFSET] = (num >> 24) & 0xFF
        self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 1] = (num >> 16) & 0xFF
        self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 2] = (num >> 8) & 0xFF
        self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 3] =  num & 0xFF
        for i in range(0, num):
            self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * 2 * i: 
                               MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 1)] = bytearray(rules[i]["hit1"])
            self.buffer[MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 1):
                               MESH_CONFIGURATION_NUM_OFFSET + 
                               MESH_CONFIGURATION_NUM_LENGTH + 
                               MESH_CONFIGURATION_HIT_LENGTH * (2 * i + 2)] = bytearray(rules[i]["hit2"])
            
    def get_buffer(self):
        return self.buffer;