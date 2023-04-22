# 03_Packet_Loss&Delay

- **Packet Loss and Delay**
    - Packets queue in router buffers, waiting for turn for transmission
        - queue length grows when arrival rate to link exceeds output link capacity
    - 각 Router 들은 Queue를 가지고 있으며 이를 다음 link로 내보내게 됨
    - Packet arrival rate to link exceeds output link capacity —> Delay
    - packet loss occurs when memory to hold queued packets fills up
    
    
    - 사용 가능한 buffers가 없는 경우 → packets dropped 발생 (Loss)
        - Loss는 기본적으로 packet being transmitted delay, packet queueing delay 에 buffer가 가득 찰 때 발생
    - **Packet Delay 4가지**
        
        
        - Nodal Processing Delay
            - Router로 들어온 Packet의 Header를 보고 어느 링크로 가야 하는지 판단 및 처리하는데 걸리는 Delay
            - Check bit errors
            - determine output link
        - Queueing Delay
            - time waiting at output link for transmission
            - Queue의 맨 뒤로 들어가 맨 앞으로 나오는 데까지 걸리는 Delay
            - depends on congestion level of router
            - 현재 Queue의 혼잡성에 따라 달라짐
            - **link bandwidth : R    packet length : L**
            - **average packet arrival rate : a (1초당 몇개의 packet이 도착하는가)**
            - **La ⇒ 들어오는 양, R ⇒ 나가는 양**
                - **La / R ~ 0 : queueing delay small (거의 없음)**
                - **La / R -> 1: queueing delay large (1에 가까우면 queueing delay가 큼)**
                - **La / R > 1: average delay infinite**
                
                
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
    - Real Internet delays and routes
        - what do real Internet delay and loss look like?
        - **traceroute program**: provides delay measurement from source to router along end-end Internet path towards destination
            - sends three packets that will reach router i on path towards destination (with time-to-live field value of i)
            - router i will return packets to sender
            - sender measures time interval between transmission and reply
            - 라우터 i 까지 도착하는데에 걸리는 시간을 알아낼 수 있는 프로그램
- **Throughput**
    - rate at which bits are being sent from sender to receiver
    - sender receiver까지 1초에 몇 bit를 보내는지
        - Instantaneous : 시간마다 달라지며 특정 시간의 throughput
        - average : 평균
    - **bottleneck link**
        - link on end-end path that constrains end-end throughput: 병목 링크
        
        
    - **Network scenario**
        - 보통 Core보다 Rc or Rs 등 host 들에서 bottleneck이 생김
