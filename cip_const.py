"""
Atomic Data Type:

          Bit = Bool
     Bit array = DWORD (32-bit boolean aray)
 8-bit integer = SINT
16-bit integer = UINT
32-bit integer = DINT
  32-bit float = REAL
64-bit integer = LINT

From Rockwell Automation Publication 1756-PM020C-EN-P November 2012:
When reading a BOOL tag, the values returned for 0 and 1 are 0 and 0xff, respectively.
"""

ELEMENT_ID = {
    "8-bit": '\x28',
    "16-bit": '\x29',
    "32-bit": '\x2a'
}

CLASS_ID = {
    "8-bit": '\x20',
    "16-bit": '\x21',
}

INSTANCE_ID = {
    "8-bit": '\x24',
    "16-bit": '\x25'
}

ATTRIBUTE_ID = {
    "8-bit": '\x30',
    "16-bit": '\x31'
}

ENCAPSULATION_COMMAND = {  # Volume 2: 2-3.2 Command Field UINT 2 byte
    "nop": '\x00\x00',
    "list_targets": '\x01\x00',
    "list_services": '\x04\x00',
    "list_identity": '\x63\x00',
    "list_interfaces": '\x64\x00',
    "register_session": '\x65\x00',
    "unregister_session": '\x66\x00',
    "send_rr_data": '\x6F\x00',
    "send_unit_data": '\x70\x00'
}

STATUS = {
    0x0000: "Success",
    0x0001: "The sender issued an invalid or unsupported encapsulation command",
    0x0002: "Insufficient memory",
    0x0003: "Poorly formed or incorrect data in the data portion",
    0x0064: "An originator used an invalid session handle when sending an encapsulation message to the target",
    0x0065: "The target received a message of invalid length",
    0x0069: "Unsupported Protocol Version"
}

"""
When a tag is created, an instance of the Symbol Object (Class ID 0x6B) is created
inside the controller.

When a UDT is created, an instance of the Template object (Class ID 0x6C) is
created to hold information about the structure makeup.
"""
CLASS_CODE = {
    "Message Router": '\x02',  # Volume 1: 5-1
    "Symbol Object": '\x6b',
    "Template Object": '\x6c',
    "Connection Manager": '\x06'  # Volume 1: 3-5
}

CONNECTION_MANAGER_INSTANCE = {
    'Open Request': '\x01',
    'Open Format Rejected': '\x02',
    'Open Resource  Rejected': '\x03',
    'Open Other Rejected': '\x04',
    'Close Request': '\x05',
    'Close Format Request': '\x06',
    'Close Other Request': '\x07',
    'Connection Timeout': '\x08'
}

TAG_SERVICES_REQUEST = {
    "Read Tag": 0x4c,
    "Read Tag Fragmented": 0x52,
    "Write Tag": 0x4d,
    "Write Tag Fragmented": 0x53,
    "Read Modify Write Tag": 0x4e,
    "Multiple Service Packet": 0x0a,
    "Get Instance Attribute List": 0x55
}

TAG_SERVICES_REPLAY = {
    0xcc: "Read Tag",
    0xd2: "Read Tag Fragmented",
    0xcd: "Write Tag",
    0xd3: "Write Tag Fragmented",
    0xce: "Read Modify Write Tag",
    0x8a: "Multiple Service Packet",
    0xd5: "Get Instance Attribute List"
}



SERVICE_STATUS = {
    0x01: "Ext error code",
    0x02: "Resource unavailable",
    0x03: "Invalid parameters value",
    0x04: "A syntax error was detected decoding the Request Path.",
    0x05: "Request Path destination unknown: Probably instance number is not present.",
    0x06: "Insufficient Packet Space: Not enough room in the response buffer for all the data.",
    0x07: "Connection lost",
    0x08: "Service not supported",
    0x09: "Invalid attribute value",
    0x0A: "Attribute list error",
    0x0B: "Already in requested mode/state",
    0x0C: "Object state conflict",
    0x0D: "Object already exist",
    0x0E: "Attribute not settable",
    0x0F: "Privilege violation",
    0x10: "Device state conflict: See extended status",
    0x11: "Reply data too large",
    0x12: "Fragmentation of a primitive value",
    0x13: "Insufficient Request Data: Data too short for expected parameters.",
    0x14: "Attribute not supported",
    0x15: "Too much data",
    0x16: "Object does not exist",
    0x17: "Service fragmentation sequence not in progress",
    0x18: "No stored attribute data",
    0x19: "Store operation failure",
    0x1A: "Routing failure,request packet too large",
    0x1B: "Routing failure,response packet too large",
    0x1C: "Missing attribute list entry data",
    0x1D: "Invalid attribute value list",
    0x1E: "Embedded service error",
    0x1F: "Vendor specific",
    0x20: "Invalid parameter",
    0x21: "Write once value or medium already written",
    0x22: "Invalid reply received",
    0x25: "Key failure in path",
    0x26: "The Request Path Size received was shorter or longer than expected.",
    0x27: "Unexpected attribute in list",
    0x28: "Invalid member ID",
    0x29: "Member not settable",
    0x2A: "Group 2 only server general failure",
    0xff: "General Error: See extended status."
}

SERVICE_EXTEND_STATUS = {
    0x45: {
        0x2105: "Access beyond end of the object."
    },
    0x52: {
        0x2105: "Number of Elements or Byte Offset is beyond the end of the requested tag."
    },
    0x4d: {
        0x2101: "Keyswitch Position: The requester is attempting to change force information in HARD RUN mode.",
        0x2105: "Number of Elements extends beyond the end of the requested tag.",
        0x2107: "Tag type used in the request does not match the target's tag data type.",
        0x2802: "Safety Status: The controller is in a state in which Safety Memory cannot be modified."
    },
    0x53: {
        0x2101: "Keyswitch Position: The requester is attempting to change force information in HARD RUN mode.",
        0x2104: "Offset is beyond end of the requested tag.",
        0x2105: "Offset plus Number of Elements extends beyond the end of the requested tag.",
        0x2107: "Data type used in the request does not match the target's tag data type.",
        0x2802: "Safety Status: The controller is in a state in which Safety Memory cannot be modified."
    },
    0x4c: {
        0x2101: "Keyswitch Position: The requester is attempting to change force information in HARD RUN mode.",
        0x2802: "Safety Status: The controller is in a state in which Safety Memory cannot be modified."
    }
}
DATA_ITEM = {
    'Connected': '\xb1\x00',
    'Unconnected': '\xb2\x00'
}

ADDRESS_ITEM = {
    'Connection Based': '\xa1\x00',
    'Null': '\x00\x00'
}

UCMM = {
    'Interface Handle': 0,
    'Item Count': 2,
    'Address Type ID': 0,
    'Address Length': 0,
    'Data Type ID': 0x00b2
}

CONNECTION_SIZE = {
    'Backplane': '\x03',     # CLX
    'Direct Network': '\x02'
}

HEADER_SIZE = 24
EXTENDED_SYMBOL = '\x91'
BOOL_ONE = 0xff
REQUEST_SERVICE = 0
REQUEST_PATH_SIZE = 1
REQUEST_PATH = 2
SUCCESS = 0
OFFSET_MESSAGE_REQUEST = 40


FORWARD_CLOSE = '\x4e'
UNCONNECTED_SEND = '\x52'
FORWARD_OPEN = '\x54'
LARGE_FORWARD_OPEN = '\x5b'
GET_CONNECTION_DATA = '\x56'
SEARCH_CONNECTION_DATA = '\x57'
GET_CONNECTION_OWNER = '\x5a'
MR_SERVICE_SIZE = 2


PRIORITY = '\x0a'
TIMEOUT_TICKS = '\x05'
TIMEOUT_MULTIPLIER = '\x01'
TRANSPORT_CLASS = '\xa3'

CONNECTION_PARAMETER = {
    'PLC5': 0x4302,
    'SLC500': 0x4302,
    'CNET': 0x4320,
    'DHP': 0x4302,
    'Default': 0x43f8,
}

DATA_TYPE = {
    'BOOL': 0xc1,
    'SINT': 0xc2,    # Signed 8-bit integer
    'INT': 0xc3,     # Signed 16-bit integer
    'DINT': 0xc4,    # Signed 32-bit integer
    'LINT': 0xc5,    # Signed 64-bit integer
    'USINT': 0xc6,   # Unsigned 8-bit integer
    'UINT': 0xc7,    # Unsigned 16-bit integer
    'UDINT': 0xc8,   # Unsigned 32-bit integer
    'ULINT': 0xc9,   # Unsigned 64-bit integer
    'REAL': 0xca,    # 32-bit floating point
    'LREAL': 0xcb,   # 64-bit floating point
    'STIME': 0xcc,   # Synchronous time
    'DATE': 0xcd,
    'TIME_OF_DAY': 0xce,
    'DATE_AND_TIME': 0xcf,
    'STRING': 0xd0,   # character string (1 byte per character)
    'BYTE': 0xd1,     # byte string 8-bits
    'WORD': 0xd2,     # byte string 16-bits
    'DWORD': 0xd3,    # byte string 32-bits
    'LWORD': 0xd4,    # byte string 64-bits
    'STRING2': 0xd5,  # character string (2 byte per character)
    'FTIME': 0xd6,    # Duration high resolution
    'LTIME': 0xd7,    # Duration long
    'ITIME': 0xd8,    # Duration short
    'STRINGN': 0xd9,  # character string (n byte per character)
    'SHORT_STRING': 0xda,  # character string (1 byte per character, 1 byte length indicator)
    'TIME': 0xdb,     # Duration in milliseconds
    'EPATH': 0xdc,    # CIP Path segment
    'ENGUNIT': 0xdd,  # Engineering Units
    'STRINGI': 0xde   # International character string
}


REPLAY_INFO = {
    0x4e: 'FORWARD_CLOSE (4E,00)',
    0x52: 'UNCONNECTED_SEND (52,00)',
    0x54: 'FORWARD_OPEN (54,00)',
    0x6f: 'send_rr_data (6F,00)',
    0x70: 'send_unit_data (70,00)',
    0x00: 'nop',
    0x01: 'list_targets',
    0x04: 'list_services',
    0x63: 'list_identity',
    0x64: 'list_interfaces',
    0x65: 'register_session',
    0x66: 'unregister_session',
}