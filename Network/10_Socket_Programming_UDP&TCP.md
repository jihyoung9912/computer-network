# 10_Socket_Programming_UDP&TCP

- Socket Programming


- Two socket types for two transport services
    - UDP: unreliable datagram
    - TCP: reliable, byte stream-oriented
    1. client reads a line of characters (data) from its keyboard and sends data to server
        1. 입력 받은 string 그대로 server에게
    2. server receives the data and converts characters to uppercase
    3. server sends modified data to client
    4. client receives modified data and displyas line on its screen

- Socket Programming with UDP
    - **UDP: no ‘connection’ between client & server**
        - no **handshaking** before sending data
        - sender explicitly attaches IP destination address and port # to each packet
            - Socket에 상대방의 정보가 없으므로, sender가 보낼 때마다 각각의 packet에 IP 주소와 port를 담아 보내야 함.
        - receiver extracts sender IP address and port # from received packet
            - 담겨진 sender의 IP와 port를 보고 reply를 해야함.
    - **UDP: no transmitted data may be lost or received out-of-order**
        - data lost 의 가능성.  순서가 바뀔 위험.
    - Application viewpoint:
        - UDP provides unreliable transfer of groups of bytes = datagrams between client and server
        
- Client/Server socket interaction: UDP
