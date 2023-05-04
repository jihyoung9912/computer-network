# 16_Multiplexing&Demultiplexing

- 각각의 process가 socket을 하나씩 만들고 packet을 보낼 때 transport layer로 전달이 됨
- transport layer는 받은 message를 network layer를 통해 상대방 host까지 보내야 하는데, 이를 위해 transport layer에선 추가적인 정보를 segment 앞에 붙이게 됨. → transport layer header
- **Multiplexing at sender**
    - handle data from multiple sockets, add transport header (later used for demultiplexing)
- **Demultiplexing at receiver**
    - use header info to deliver received segments to correct socket
    
    

- How demultiplexing works—2 4m
    - host receives IP datagrams
        - each datagram has source IP address, destination IP address
        - each datagram carries one transport-layer segment
        - each segment has source, destination port number
    - host uses **IP addresses & port numbers** to direct segment to appropriate socket
    
    

- **Conectionless demultiplexing**
    - recall: created socket has host-local port #
        - DatagramSocket mySocket1 = new DatagramSocket(12534);
    - recall: when creating datagram to send into UDP socket, must specify
        - destination IP address
        - destination port #
    - when host receives UDP segment
        - checks destination port # in segment
        - directs UDP segment to socket with that port #
        - →
        - IP datagrams with same destination port #, but different source IP addresses and/or source port numbers will be directed to same socket at destination

- **Connection-oriented demux**
    - TCP socket identified by 4-tuple
        - source IP address
        - source port number
        - dest IP address
        - dest port number
    - demux: receiver uses all four values to direct segment to appropriate socket
    - server host may support many simultaneous TCP sockets:
        - each socket identified by its own 4-tuple
    - web servers have different sockets for each connecting client
        - non-persistent HTTP will have different socket for each request
