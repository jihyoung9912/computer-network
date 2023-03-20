# Network Core

- **Network Core**
    - mesh of interconnected routers
    - Mesh 형태로 연결된 router들의 집합, Network of networks
    - **Packet-Switching**
        - application-layer(프로토콜의 최상위 계층)에서 Host가 보낼 데이터 messages를 packets으로 쪼개는 것
        - router에서 다음 router로 Packet을 전달하면서 source부터 destination까지 전달함.
    - Packet-Switching 특징
        - **store-and-forward**
            - A 라우터가 비트를 모두 B에게 전달해준 후, B가 모두 받고 저장 후 C 라우터로 전송하는 방법
            - 한 개의 packet 전체가 모두 transmitted 되어야 다음 router or hosts로 전송 ↔ Circuit Switching
            - Packet Transmission Delay
                - A 라우터에서 B 라우터까지 완전히 도착하는 데 걸리는 시간 → L/R
                - N개의 link가 있을 때 zero propagation delay 가정 총 시간 N*L/R
                
                
        - **Queueing**
            
            
            - 만약 시간당 arrival rate (in bits)가 link의 transmission rate를 넘어가면 packet은 queue에 쌓이고, link로 transmitted 되기까지 대기한다 —> queue
                - memory(buffer) 이상으로 쌓이면 Packet Loss 발생
    - **Network-Core의 기능**
        - **Routing**
            - Routing Algorithm을 통해 source 에서 destination 까지의 경로를 결정하는 것
                - forwarding table을 만들고, 이를 통해 경로를 파악할 수 있음
            - 다른 라우터들과 함께 고려하기에 Global Action
        - **Forwarding**
            - Router 내부에서 Router 입력 포트에서 Router 출력 포트로 Packet을 이동시키는 것
            - 라우터 내부에서만 일어나기에 Local Action
    - Store-and-Forward의 대안 Circuit Switching
        - source에서 destination 까지의 resource를 미리 할당시켜 놓고 미리 신호가 되어 있는 메세지들이 즉시 이동하는 것.
        - 해당 경로는 공유될 수 없음
        - 마치 source - destination 까지 선을 하나 만들어 놓은 것과 같음 (사용하지 않아도 사용할 수 없음 비효율적)
            - 위의 비효율을 보완하기 위해 FDM TDM으로 구분
                
                
            - 전체 대역폭을 잘라내어 분할하여 연결
    - Network Core가 메세지를 보내는 두가지 방식 중 어떤 것이 더 좋은가?
        - Packet Switching이 더 많은 유저가 사용할 수 있기에 사용
        
        
        - active시 100kb/s 필요, active는 전체 시간 중 10%만 사용
            - circuit → 자원을 할당하기에 10명 고정
            - packet → 35명의 유저가 1 Mb/s 이상을 사용할 가능성 0.0004. 큰 문제 없음
        - 무조건 Packet이 좋은 것은 아님.
            - bursty data 한꺼번에 마구 보내고, 이후 잘 안보내고.. 이런 상황에서는 굉장히 좋음
            - congestion possible → 더 많은 데이터가 올 경우 delay, loss 발생 가능성
                - 이를 방지하기 위해 protocols 필요

- Internet
    - network of networks
    - End Systems connect to Internet via access ISPs (SK, KT U 등등)
    - Access ISPs in turn must be interconnected (ISP들 끼리 연결되어야 함)
        - Economics, National Policies 등 복잡한 과정이 동반됨.
        - 계획적으로 진행된 것이 아니라 각자 회사들의 자발적인 시작에서 발전되는 구조이기 때문.
    - **그렇다면 현재 인터넷의 구조는?**
        - Millions of access ISPs
            1. N의 제곱만큼 연결 선을 설치한다 (가능성이 거의 없음)
            2. Global ISP에 연결한다
                - Global ISP 또한 개별 사업이기때문에 결국 또 Global ISP가 여러개가 생기고, 그 Global ISP들 끼리 연결이 필요함
                - 또한 Global까지 직접 가기 전에 regional net을 만들어 경제적으로 효율적인 ISP가 생김
                - 최근 Content Provider Network 자기들의 Network를 만들어 모든 Access Network에 접근 가능하도록 만드는 추세 (Google, AWS 등) 가장 빠름.
                
- **Packet Loss and Delay**
    - 각 Router 들은 Queue를 가지고 있으며 이를 다음 link로 내보내게 됨
    - Packet arrival rate to link exceeds output link capacity —> Delay
    - 사용 가능한 buffers가 없는 경우 → packets dropped 발생 (Loss)
        - Loss는 기본적으로 packet being transmitted delay, packet queueing delay 에 buffer가 가득 찰 때 발생
    - **Packet Delay 4가지**
        - Transmission Delay
            - Queue의 맨 앞에 있는 하나의 Packet에 담긴 모든 bit를 링크까지 옮기는 데 걸리는 Delay
            - packet length : L (bits)
            - link bandwidth R (bps)
            - D trans = transmission delay = L / R
        - Propagation Delay
            - Packet이 Link를 타고 다음 Router까지 도달하는데 걸리는 Delay
            - length of physical link : d
            - propagation speed : s
            - D prop = d / s
        - Nodal Processing Delay
            - Router로 들어온 Packet의 Header를 보고 어느 링크로 가야 하는지 판단및 처리하는 데 걸리는 Delay
            - Check bit errors
            - determine output link
        - Queueing Delay
            - Queue의 맨 뒤로 들어가 맨 앞으로 나오는 데까지 걸리는 Delay
            - 현재 Queue의 혼잡성에 따라 달라짐
            - link bandwidth : R
            - packet length : L
            - average packet arrival rate : a (1초당 몇개의 packet이 도착하는가)
            - La ⇒ 들어오는 양, R ⇒ 나가는 양
            - La / R ~ 0 : queueing delay small (거의 없음)
            - La / R -> 1: queueing delay large (0에 가까우면 queueing delay가 큼)
            - La / R > 1: average delay 무한대
- **Throughput**
    - sender receiver까지 1초에 몇 bit를 보내는지
        - Instantaneous : 시간마다 달라지며 특정 시간의 throughput
        - average : 평균
    - rate (bits/time unit) at which bits transferred between sender / receiver
    - **bottleneck link**
        - link on end-end path that constrains end-end throughput 병목 링크
        
        
    - Internet scenario
        - 보통 Core보다 Rc or Rs 등 host 들에서 bottleneck이 생김
        
        

- **Protocol Layers**
    - Networks are complex, with many pieces
    - 너무 복잡하기에 Network를 Layer로 나누어 계층별 관계들을 찾아내는 과정
        - 편리한 업데이트 유지보수
    - **Internet Protocol Stack**
        - Application
            - supporting network applications (HTTP, FTP, SMTP)
        - Transport
            - process-process data transfer (TCP, UDP)
            - 프로세스: 실행이 되고 있는 프로그램.
        - Network
            - routing of datagrams(packets) from source to destination (IP, routing protocols)
        - Link
            - data transfer between neighboring network elements (Ethernet, 802.11, ppp)
            - 물리적 링크로 인접해있는 Node간 Data transfer
        - Physical
            - bits on the wire
            - 물리적으로 bit를 전달하는 계층
    - ISO/OSI reference mdoel (실질적 표준)
        
        
        - Presentation
            - allow applications to interpret meaning of data (encryption, compression)
            - data의 meaning을 해석
        - Session
            - synchronization, checkpointing, recovery of data exchange
            - 동기, 데이터를 주고 받다 끊어지는 경우
        - 상횡마다 필요한 경우가 있으며, 만약 필요하다면, application layer에 합쳐 구현
    - 각각의 계층에서는 본인의 할 일만을 분업적으로 진행하며 상호간의 영향은 최소화.
    - **Encapsulation**
        - 각각 계층에서 아래 계층으로 보낼 때 해당 계층에 필요한 데이터를 Header에 붙여서 내려 보내는 과정 각 계층마다 필요한 Header가 다름.
        - M → Message
        - Ht M → Segment
        - Hn Ht M → datagram
        - Hl Hn Ht M → frame
    
    

- **Network Security**
    - Hacker → put malware into hosts via internet
    - Malware
        - Virus → 자가복제 감염 (다운 받은 후 실행해야 감염)
        - Worm → 스스로 실행 (다운 받자마자 실행)
    - Spyware
        - keystroke 저장
        - 웹 방문 기록 저장 (광고 등에 이용됨)
    - host가 감염되어 Botnet에 올라간다면, 디도스의 위험.
    - DDos (Distribute Denaial of service)
        - Attacker가 어떤 서버가 갖고 있는 resource를 모두 사용하게 만들어버림
            - 정상적인 Traffic이 해당 resource를 사용하지 못함
        - Target을 선정하고 Botnet에 속한 모든 컴퓨터가 해당 타겟 서버에 메세지를 보냄. 서버는 메세지가 왔으니 처리를 해야만 하고, 많은 Resource를 사용하기에 정상적인 Message, Packet이 거부됨.
            
            
    - Packet Sniffing
        
        
        - B가 A에게 링크를 보낼 때 해당 Link가 shared link인 경우 C가 해당 link를 볼 수 있음
            - Network Interface를 promiscouos로 변경할 경우 본인에게 오는 packet이 아님에도 볼 수 있음
        - broadcast media (shared Ethernet, wireless)
        - wireshark
            - 모든 packet을 볼 수 있음 (화이트 해커쪽)
    - IP spoofing
        - C가 A에게 B가 보내는 것처럼 만들어 보냄.
            - 이를 통해 B가 보낸 줄 알고 어떤 resource를 처리하게 됨.
            - send packet with false source address
        
- Internet History
    - 1961 Kleinrock → Packet Switching 등장
        - 기존 Circuit Switching만 있었으며, 소련이 이를 공격하여 통신망을 마비 시켜도 통신 가능하게 하기 위해 발명
    - 1972 - 1980 새로운 Internetworking이 생기기 시작
    - 1974 Cerf and Kahn → interconnecting에 대한 설계 고안 오늘 날의 인터넷 Architecture에 기반이 되는 상호 연결의 기반을 만들어냄.
    - early 1990s Web이 생기며 Berners-Lee의 HTML
