# 03_Network_Application_Layer

- Top Down Approach

- Network Application Program
    - run on different end systems
    - network application 배포 위해선 end-system에만 해당 어플리케이션이 실행되면 됨
        - network-core 에서는 무언가 해줄 필요가 없음
        - no need to write software for network-core devices
        - 어떤 프로그램 개발을 위해 Router를 수정할 필요가 없음
        - 만약 어떤 소프트웨어가 router에 종속되어 실행된다면 어떤 어플리케이션을 만들 때마다 Router를 이에 맞춰 수정해야하며, 굉장히 비효율적이고 현재 어플리케이션들의 개발이 불가능했음.

- Application 간의 통신 방식은 크게 두 가지
    - Client-Server Architecture
        - client/server model에서 해당 네트워크를 server, clients로 구분
            
            
        - Server
            - always-on host (항상 켜져 있어야 함)
            - Permanent IP address
                - 영구적인 IP 주소가 필요
            - Data centers for scaling
        - Clients
            - communicate with server
            - intermittently connected
                - 간헐적으로 연결되어도 상관 없음. 사용할 때만 연결.
                - dynamic IP Address
                    - IP 주소가 달라져도 상관 없음
                - do not communicate directly with each other (clients)
    - P2P Architecture (peer-to-peer)
        
        
        - no always-on server
        - arbitrary end systems directly communicate
            - server 없이 end-system간 서로 간 데이터를 주고 받음
        - peers request service from other peers, provide service in return to other peers
            - **self scalability**
                - new peers bring new service capacity, as well as new service demands
                - 어떤 p2p system에 참여한다면 나의 cpu, bandwidth 등을 사용하여 타인이 나의 파일을 받아갈 수 있다라는 것.
        - peers are intermittently connected and change IP addresses
        - complex management (어떤 파일을 어떤 IP가 가지고 있는지 기억을 해놔도 계속 바뀌고 업데이트 해줘야 하기 때문 / 해당 파일이 살아 있는지 계속 확인해줘야 함.)
            - server/client는 서버가 항상 켜져 있고, 모든 데이터가 server에 있기 때문에 관리가 용이함.

- Processes Communicating
    - Network Application을 실행시킨다는 것은 해당 Process를 실행시킨다는 것.
    - **process**
        - program을 실행시키면 운영체제 입장에서 process가 되는 것.
        - program running within a host
        - within same host, two processes communicate using inter-process communication (defined by OS)
            - 두개의 프로세스가 같은 host (컴퓨터)에 있다면 해당 프로세스 사이에선 inter-process communication을 통해 통신.
        - processes in different hosts communicate by exchanging messages
            - 다른 host에 있다면 Network를 통해 Message를 교환하는 방식으로 통신
        - client/server인 경우 client process server process 존재
            - client process (web browser)
                - 해당 커뮤니케이션을 시작하는 사람
                - process that initiatess communication
            - server process (web server)
                - 실행됐지만 컨택 접근을 기다리는 사람
                - process that waits to be contracted
        - P2P Application의 경우 해당 process가 client process, server process 역할 모두 해야 함.
    - **Sockets**
        
        
        - process sends/receives messages to/from its socket
        - 프로세스가 다른 컴퓨터의 프로세스와 통신하기 위해선 아래의 transport layer로 어떤 서비스 정보를 주고 다른 end-system (transport layer) 까지 전달될 수 있게 처리해야 함.
            - socket을 통해 해당 메세지를 주고 받게 됨.
            - Application의 process가 각각 socket을 하나씩 생성하여 socket으로 데이터를 보내고 데이터를 읽어오게 됨.
        - socket analogous to door (문과 비교 가능)
            - sending process shoves message out door
            - sending process relies on transport infrastructure on other side of door to deliver message to socket at receiving process
                - socket을 만들기만 하면 socket이 알아서 전달. application은 몰라도 됨.
                - process를 app developer가 만들어 내는 것, 하등의 layers는 OS가 개발하는 것.
                - 어떤 다른 소켓과 메세지를 전달할지 최소한의 정보를 주고받는 과정은 필요

- Addressing processes
    - 상대방의 주소를 받아내는 방법
    - to receive messages, process must have identifier
        - 해당 소켓을 인지할 수 있는 id 가 필요
    - host device has unique 32-bit IP address
    - 하지만 IP 주소만으로는 특정 프로세스를 식별할 수 없다. 즉 identify 하기에는 충분하지 않다.
        - 한 IP 주소의 PC에서 여러 개의 process를 실행하고 있다.
    - 그래서 Port Numbers 가 필요함.
        - Ip address: 128.119.245.12
        - Port Num: 80
    - IP 주소와 Port Num을 알고 있다면 인터넷 상에서 실행되는 특정 프로세스를 정확히 identify 할 수 있다.
    - 이때 두개의 프로세스 사이 메세지를 주고 받기 위해 Protocol을 따라야 함.
- **App-Layer Protocol Defines**
    - types of messages exchanged
        - 메세지의 타입 (request, response)
    - Message Syntax
        - what fields in messages & how fields are delineated
        - 메세지의 문법을 정의
    - Message Semantics
        - meaning of information in fields
    - Rules for when and how processes send & respond to messages
    - 우리는 위를 정의한 문서를 보고 맞게 개발해야함.
    - 해당 문서의 두가지 종류
        - open protocols
            - RFCs 문서에 정의 되어 있음.
            - 누구나 문서를 보고 작성하면 다른 사람과 주고 받을 수 있음
            - allows for interoperability
            - HTTP, SMTP
        - proprietary protocols
            - 사적인 protocol

- What Transport service does an app need?
    - 메세지를 주고 받기 전 transport layer가 어떤 서비스를 제공할 수 있는지를 파악해야함.
    - data integrity
        - 데이터가 변조되어서는 안됨. transport layer가 제공해줌.
            - 파일 전송과 같은 앱은 100%의 정확성이 필요하기 때문
    - timing
        - require low delay to be effective
            - 게임과 같은 앱
    - throughput
        - some apps require minimum amount of throughput to be effective
            - 최소의 throughput을 필요로 하는 앱이 있을 수 있다.
    - security
    - 어플리케이션마다 위의 해당되는 즉 필요한 transport service가 다르다.
    
    
- Internet transport protocols service가 위 모든 것을 제공해줄 수 있지 않으며, 두가지의 서비스 제공.
    - **TCP service**
        - reliable transport between sending and receiving process
            - 믿을만한 transport service 제공. 데이터의 손실이 없음.
        - flow control
            - sender won’t overwhelm receiver
            - 두개의 process가 주고 받을 때, 주는 쪽에서 너무 빠르게 주면 받는 쪽에서 처리가 불가능 할 수도 있는데, sender가 receiver를 압도하지 않게 조정하는 기능 제공
        - congestion control
            - throttle sender when network overloaded
            - network 상황이 좋지 않다면 혼잡을 제어하는 기능 또한 제공
        - does not provide!
            - timing, minimum throughput guarantee, security
            - minimum (이 메세지를 상대방에게 몇 ms 안에 보내달라) 불가능
        - connection-oriented
            - setup required between client and server processes
            - 연결 지향적인 서비스. 데이터를 보내기 전에 상대 프로세스와 우리 프로세스 사이에 미리 연결을 설정해놓음. 즉 우리가 곧 데이터를 보내겠다 맺고 데이터를 보냄.
    - **UDP service**
        - unreliable data transfer between sending and receiving process
            - 가긴 가지만 중간에 사라지거나 유실될 수도 있음.
        - does not provide!
            - reliability, flow control, congestion control, timing, throughput guarantee, security, or connection setup
            - connection setup이 필요 없는 것은 작은 장점일 수도 있음.
    - 아무것도 못해주는데 왜 UDP가 있을까?
        - connection setup이 필요 없기에 최초 세팅에 대한 시간을 절약할 수 있음.
        
        
    - 중요한 건 어플리케이션마다 필요한 서비스가 다르기에 TCP or UDP 중 선택하여 서비스를 제공하는 것.
    - **Securing TCP**
        - TCP & UDP
            - no encryption (암호화 X)
            - cleartext passwords sent into socket traverse Internet in cleartext
                - 암호가 network 통해 cleartext로 가게 됨. (sniffing의 위험)
        - SSL (Secure Socket Layer)
            - Provides **encrypted** TCP connection
            - data integrity (진실된 데이터)
            - end-point authentication (인증을 하고 데이터를 주고 받음)
        - SSL is at app Layer
            - apps use SSL libraries, that ‘talk’ to TCP
            - SSL은 application layer에 library로 구현 되어 있어 SSL Library를 사용하고 제공되는 함수 등을 사용하는 것.
            - SSL Library가 TCP에 메세지를 보내며 communication 하는 것.
        - SSL socket API
            - cleartext passwords sent into socket traverse Internet encrypted
            - 어플리케이션이 암호를 SSL로 보내주면 SSL이 암호화하여 TCP로 전달하는 것.
