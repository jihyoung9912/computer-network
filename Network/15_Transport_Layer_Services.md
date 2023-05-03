# 15_Transport_Layer_Services

- **Transport services and protocols**
    - provide logical communication between app processes running on different hosts
    - transport protocols run in end systems
        - send side: breaks app messages into segments, passes to network layer
            - 상단의 application Layer에서 보내주는 message를 segment로 break, network layer로 보냄
        - rcv (receive) side: reaseembles segments into messages, passes to app layer
        
        
    - more than one transport protocol available to apps
        - Internet: TCP and UDP

- **Transport vs Network Layer**
    - network layer
        - logical communication between hosts
    - transport layer
        - logical communication between processes
            - relies on, enhances, network layer services
            - host간의 소통이 되어야 processes간의 소통이 가능하기에 network layer에서 제공하는 서비스를 이용해서 process간의 소통을 하는 것임.
            
            
- Internet transport-layer protocols
    - reliable, in-order delivery (TCP)
        - congestion control
        - flow control
        - connection setup
        - 각각의 segment가 중간에 사라질 수도 있는데, 그럴 경우 복구해내는 기능이 있기에 reliable
        - message를 segment로 쪼갠 후 순서에 맞게 정렬하여 올려보냄 in-order
    - unreliable, unordered delivery (UDP)
        - no-frills extension of ‘best-effort’ IP
        - 빠지면 빠진대로 순서 없이 app layer로 올려보냄
    - services not available
        - delay guarantees
        - bandwidth guarantees
