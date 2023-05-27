# 17_UDP_Connectionless_Transport

- **UDP: User Datagram Protocol**
    - “no frills”, “bare bones” Internet transport protocol
    - “best effort” service, UDP segments may be
        - lost
        - delivered out-of-order to app
    - **connectionless**
        - no handshaking between UDP sender, receiver
        - each UDP segment handled independently of others
    - UDP use
        - streaming multimedia apps (loss tolerant, rate sensitive)
        - DNS
        - SNMP
    - reliable transfer over UDP
        - add reliability at application layer
        - application-specific error recovery

- **UDP: segment header**
    - why is there a UDP?
        - no connection establishment (which can delay)
        - simple: no connection state at sender, receiver
        - small header size
        - no congestion control:
            - UDP can blast away as fast as desired

- **UDP checksum**
    - Goal: detect “errors”  (e.g., flipped bits) in transmitted segment
    - Sender
        - treat segment contents, including header fields, as sequence of 16-bit integers
        - checksum: addition (one’s complement sum) of segment contents
        - sender puts checksum value into UDP checksum field
    - Receiver
        - compute checksum of received segment
        - check if computed checksum equals checksum field value
            - No - error detected
            - YES - no error detected, but maybe errors -later
            - 
