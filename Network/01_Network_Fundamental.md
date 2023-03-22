- **Network**
    - 컴퓨터끼리 서로 정보를 주고 받을 수 있도록 연결된 통신망
- **Internet**
    - Billions of connected computing devices
    - 여러 통신망을 하나로 연결하는 것
    - Internet을 보는 두 가지 관점 (nuts and bolts, service view)
- **nuts and bolts view**
    - 구성요소로 인터넷을 정의하는 관점
    - billions of connected computing devices
    - Internet: network of networks
    - 이렇게 연결된 네트워크에서 모든 장치들을 (connected computing devices) host or end system 이라고 하며, 해당 host가 network apps를 실행하고 있다.
        - end system은 communication link(통신 링크)와 packet switch를 통해 네트워크로 연결됨
        - 이 연결은 동축케이블, 광케이블과 같은 물리적 매체를 통해 이뤄지며 데이터 전송의 속도를 따지는 것을 transmission (전송률) 단위는 bps (bit per second)
        - transmission rate = bandwidth
            - link의 성능
        - Packet Switches
            - Router or Switches 를 통해 Forward packets
    - interconnected ISPs
        - **ISP**는 **Internet Service Provider, end host들에게 인터넷 접속점을 제공해주는 역할.**
    1. 수백만개의 연결된 컴퓨팅 장치들이 존재하고 컴퓨팅 장치에서는 **host** 또는 **end system** 에 네트워크 어플리케이션이 실행되고 있다.
    2. 이 장치들은 **communication links**라 불리는 **fiber, copper, radio, satelite**로 통하여 데이터를 전송한다.
    3. 이때 데이터들은 전송속도를 의미하는 **bandwidth**를 bit per second 단위로 표기할 수 있다.
    4. **packet switches**는 패킷을 전송하는 network 3 계층 장비들을 의미한다. 대표적으로 **router**와 **switch**가 존재한다.
    5. 인터넷은 **"network of networks"**이다. **ISP(Internet Service Provider)**들과도 다 연결이 되어있다.
    6. **protocols**은 메세지를 전송 및 수신을 위한 일종의 약속이다. **TCP, IP, HTTP, Skype, 802.11** 같은 약속들이 존재한다.
    7. **Internet standards**를 규정하는 문서가 존재한다. **RFC(Request for comments)**, **IETF(Internet Engineering Task Force)**이다.
- **services view**
    - 구성요소가 아니라 인터넷이 나에게 무엇을 제공해줄 수 있느냐의 관점
    - Infrastructure that provides services to applications
    - 어플리케이션들에게 서비스를 제공하는 기반 시스템
    - 이런 관점에서 어플리케이션은 Web, Email, Games 등
    - provides programming interface to distributed applications (API를 제공해줘야 함)
    - 어플리케이션에게 코딩 가능한 socket interface 제공, end system에서 end system으로 전송 및 수신 가능한 distributted application 제작을 돕는다
- **Protocol**
    - control, sending, receiving of messages
    - 컴퓨터 네트워크에서 데이터를 주고 받을 때 수행되는 절차 규약 관례
    - it defines the format, order of messages sent 등
    
    ![imgae](https://user-images.githubusercontent.com/102154146/225836854-99f12fa7-4b8e-41a8-ad26-e818e822730b.png)

    
- **Internet Standards**
    - Protocol을 정의하는 기준 규칙
    - 인터넷 표준. 인터넷에 적용되는 기술이나 방법론을 표준으로 제정한 규격
    - IETF (Internet Engineering Task Force)
        - 국제 인터넷 표준화 기구. 인터넷 표준을 제정 및 공표하는 기구
    - RFC (Request for Comments)
        - 비평을 기다리는 문서
        - 인터넷 기술에 적용 가능한 새로운 연구, 기법 등을 나타냄

- **Network Edge**
    - hosts = clients and servers로 구성
    - servers often in data centers
- **Access Networks, Physical media**
    - 유선 또는 무선의 communications link를 가지는 네트워크
    - Network Edge와 Network Core를 연결시켜 주는 것 (LAN)
- **Network core**
    - interconnected routers
    - 라우터끼리 연결되어 있는 것
    - network of networks
    - Mesh 형태로 연결된 routers의 연결 집합.
- **Access network : Cable Network**
    - End System과 Edge Router의 연결 역할, 다양한 종류
    - cable-based access
        - Frequency division multiplexing
            - 전체 대역폭을 주파수로 나눠 여러개의 정보를 쪼개 동시에 보냄.
            - 서로 다른 chanel들이 서로 다른 대역폭에서 전송되는 방식 (주파수)
            - 대역폭이 크면 담을 수 있는 데이터가 많아짐
            - Shared 회선을 사용 —> HFC (Hybrid Fiber Coax) 광동축 혼합망
    - Digital Subscriber Line (DSL)
        - 인터넷 선 보급 전 존재했던 dedicated 전화선 사용 방식
        - 전화 선이 모이는 central office의 DSLAM이 전화와 인터넷을 구분하여 telephone network와 ISP network로 전달해주는 multiplexer 역할을 함
        - 빠르고 편리한 설치, 전화선을 통해 구성한 네트워크기에 낮은 성능
    - Home Networks
        - wireless access point —> 공유기.
        - 여러 장치들이 이 곳에 연결할 수 있다.
    - Enterprise Networks (Ethernet)
        - 주로 회사나 학교에서 쓰이는 네트워크 구성
        - 다양한 transmission rates가 존재
    - Data Center Networks
        - 고대역 메모리 링크
- **Access network : Wireless**
    - Shared wireless access network
    - 전파가 공기 매질을 통해 퍼져 연결하는 방법이며, 모두가 같은 전파 신호를 감지할 수 있음
    - 같은 공유기를 공유할 때, 한 기기가 전파를 보내고 있으면 다른 기기는 전파를 보낼 수 없음
        - wireless LANs, Wide-Area wireless

- **Host = End systems**
    - application의 message를 받고, 이를 보내야 함
    - sends packets of data / 데이터의 packet(chunk)를 보내는 주체
    - 데이터를 packets이라고 부르는 smaller chunks로 쪼개서 전송
        - 그 길이를 L bits라고 부름
    - packet이 access network의 link로 전환(도착)되기까지 걸리는 시간을 transmission rate (=link capacity, =link bandwidth) 라고 하며 R bit/sec 단위를 사용함 1초당 몇 bit를 보낼 수 있느냐.
    
    ![Untitled](https://user-images.githubusercontent.com/102154146/225836657-9e19c481-66e2-4cd6-8c9e-fc833944255e.png)

    ![Untitled](https://user-images.githubusercontent.com/102154146/225836674-26725164-9287-4d0b-8a9f-46b413f40b5c.png)

    - ***Packet Transmission Delay - 하나의 패킷을 전부 전송하는데 얼마나 걸리느냐.***

- Physical media
    - 유선일 경우 어떤 선을 사용하는가
        - TP Twisted Pair
            - 쌓여져 있는 구리선
            - 기본적으로 최소 송신 수신이 필요하고, 두개 이상의 구리선을 통해 전기를 이동시킴. 이때 자기장이 발생하며 서로에게 영향을 미치게 됨. 그렇기에 내부에서 서로 방해되지 않게 선을 꼬아 놓음.
        - Coaxial Cable
            - 두개의 구리 유도체 (전도체)의 중심 축이 같음.
            - 양방향 통신.
            - broadband
                - bandwidth가 넓어 여러개의 채널 가능
        - fiber optic cable
            - 광케이블.
            - 빛을 보냈다 안보냈다 하며 0, 1로 비트를 전송
            - 빠른 속도 적은 에러
            - 전기를 통한 자기장의 Noise에 면역
    - radio link types
        - 무선 전파
        - 양방향 통신
        - 사방면 모두 나아가기에 반사가 생길 수도 있으며 물체에 막힐 수도 있고, 타 전파들에 간섭을 받을 위험이 있음
            - microwave
            - LAN
            - wide-area
            - satelite
                - 굉장히 장거리까지 닿지만, 그만큼 end-end delay가 김
