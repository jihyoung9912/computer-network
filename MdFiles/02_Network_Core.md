# 02_Network_Core

- **Network Core**
    
    
    - mesh of interconnected routers
    - Mesh 형태로 연결된 router들의 집합, Network of networks
    - **Packet-Switching**
        - hosts break application-layer messages into **packets**
        - application-layer(프로토콜의 최상위 계층)에서 Host가 보낼 데이터 messages를 packets으로 쪼개는 것
        - network **forwards** packets from one router to the next, across links on path from **source to destination**
        - router에서 다음 router로 Packet을 전달하면서 source부터 destination까지 전달함.
    - **Network-Core의 기능**
        - **Routing**
            - **Global Action**
                - determine source-destination paths taken by packets
            - Routing Algorithm을 통해 source 에서 destination 까지의 경로를 결정하는 것
                - forwarding table을 만들고, 이를 통해 경로를 파악할 수 있음
        - **Forwarding**
            - **Local Action**
                - move arriving packets from router’s input link to appropriate router output link
            - Router 내부에서 Router 입력 포트에서 Router 출력 포트로 Packet을 이동시키는 것
    - Packet-Switching 특징
        - **store-and-forward**
            - A 라우터가 비트를 모두 B에게 전달해준 후, B가 모두 받고 저장 후 C 라우터로 전송하는 방법
            - 한 개의 packet 전체가 모두 transmitted 되어야 다음 router or hosts로 전송 ↔ Circuit Switching
            - **Packet Transmission Delay**
                - takes L/R seconds to transmit L-bit packet into link at R bps
                - A 라우터에서 B 라우터까지 완전히 도착하는 데 걸리는 시간 → L/R
                - N개의 link가 있을 때 zero propagation delay 가정 총 시간 N*L/R
                
                
        - **Queueing**
            
            
        - Queueing occurs when work arrives faster than it can be serviced.
            - 만약 시간당 arrival rate (in bits)가 link의 transmission rate를 넘어가면 packet은 queue에 쌓이고, link로 transmitted 되기까지 대기한다 —> queue
                - 100 Mb/s로 양쪽에서 오지만 1.5Mb/s 밖에 못보내기에 queue가 발생.
                - memory(buffer) 이상으로 쌓이면 Packet Loss 발생
            - **Packet queuing and loss**
                - if arrival rate to link exceeds transmission rate of link for some period of time
                    - packet will queue, waiting to be transmitted on output link
                    - packets can be dropped (lost) if memory buffer in router fills up
    - Alternative Store-and-Forward: **Circuit Switching**
        - end-end resources allocated to, reserved for call between source and destination
        - source에서 destination 까지의 resource를 미리 할당시켜 놓고 미리 신호가 되어 있는 메세지들이 즉시 이동하는 것.
        - circuit segment idle if not used by call (No Sharing) 경로 공유 불가.
        - 마치 source - destination 까지 선을 하나 만들어 놓은 것과 같음 (사용하지 않아도 사용할 수 없음 비효율적)
            - 위의 비효율을 보완하기 위해 FDM TDM으로 구분
                
                
            - **Frequency Division Multiplexing (FDM)**
                - optical, electromagnetic frequencies divided into narrow frequency bands
                - each call allocated its own band, can transmit at max rate of that narrow band
            - **Time Division Multiplexing (TDM)**
                - time divided into slots
                - each call allocated periodic slot, can transmit at maximum rate of frequency band during its time slot
            - FDM과 TDM의 주요 차이점은 전송 매체를 나누는 방식.
                - FDM은 주파수로 나누고 TDM은 시간으로 나눔.
                - FDM에서는 각 채널이 다른 주파수 대역을 점유하는 반면 TDM에서는 각 채널이 다른 시간 슬롯을 점유. FDM은 아날로그 신호에 사용되는 반면 TDM은 디지털 신호에 사용.
    - Two way of sending message of Network Core. Packet switching is more good.
        - Packet Switching이 더 많은 유저가 사용할 수 있기에 사용
        
        
        - active시 100Mb/s 필요, active는 전체 시간 중 10%만 사용
            - circuit → 자원을 할당하기에 10명 고정
            - packet → 35명의 유저가 1 Gb/s 이상을 사용할 가능성 0.0004. 큰 문제 없음
        - Not Packet Switching is always the best.
            - bursty data. 한꺼번에 마구 보내고, 이후 잘 안보내고.. 이런 상황에서는 굉장히 좋음
            - **excessive congestion possible**
                - packet delay and loss due to buffer overflow
                - protocols needed for reliable data transfer, congestion control
                - 더 많은 데이터가 올 경우 delay, loss 발생 가능성, 이를 방지하기 위해 protocols 필요

- Internet: network of networks
    - **End Systems connect to Internet via access ISPs (SK, KT U 등등)**
        
        
    - Access ISPs in turn must be interconnected (ISP들 끼리 연결되어야 함)
        - so that any two hosts can send packets to each other
        - evolution driven by economics, national policies.
            - Economics, National Policies 등 복잡한 과정이 동반됨.
        - 계획적으로 진행된 것이 아니라 각자 회사들의 자발적인 시작에서 발전되는 구조이기 때문.
    - **그렇다면 현재 인터넷의 구조는 어떻게 연결되어 있는가?**
        - Millions of access ISPs
            1. N의 제곱만큼 연결 선을 설치한다 (가능성이 거의 없음)
            2. Global ISP에 연결한다
                - Global ISP 또한 개별 사업이기때문에 결국 또 Global ISP가 여러개가 생기고, 그 Global ISP들 끼리 연결이 필요함
                - 또한 Global까지 직접 가기 전에 regional net을 만들어 경제적으로 효율적인 ISP가 생김
                - 최근 Content Provider Network 자기들의 Network를 만들어 모든 Access Network에 접근 가능하도록 만드는 추세 (Google, AWS 등) 가장 빠름.
