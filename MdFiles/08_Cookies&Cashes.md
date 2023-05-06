# 08_Cookies&Cashes

- User-Server state: **Cookies**
    - many Web sites use cookies
        - HTTP는 stateless이지만 user-server state인 cookie를 통해 상태를 저장할 수 있다.
        - **four components**
            - cookie header line of HTTP response message
            - cookie header line in next HTTP request message
                - HTTP response, request header에는 cookie header가 함께 있음.
            - cookie file kept on user’s host, managed by user’s browser
            - back-end database at Web site
                - 웹 사이트 백엔드 디비에도 쿠키를 저장하는 곳이 존재.
            - 클라이언트와 서버 모두 쿠키를 저장함으로써 방문 기록이 있는 유저에게 서비스의 차별점을 제공할 수 있음.
                
                
                - Cookies: Keeping “State”
                - 아마존에 접속시 1678이라는 ID를 만들고 저장함.
                - 추후 set-cookie를 http response에 담아 보내고, client는 해당 쿠키속 ID를 저장.
                - 다음 요청부터 client가 저장한 쿠키 ID를 함께 보내며 다음 접속시 해당 쿠키를 기반으로 웹 사이트의 운영을 달리 할 수 있음.
                - cookie에도 expire time이 존재, 일정 시간 지나면 사라지게 됨.
    - What cookies can be used for
        - authorization
        - shopping carts
        - recommendations
        - user session state (Web e-mail)
    - How to keep “State”
        - protocol endpoints: maintain state at sender/receiver over multiple transactions
        - cookies: http messages carry state
            - protocol endpoints가 cookie를 유지함.
    - cookie를 통해 유저의 웹 이력을 볼 수 있기에 privacy 침해의 위험이 있다.

- **Web caches (proxy server)**
    - goal: satisfy client request without involving origin server
        - origin server의 관여 없이 request 처리 방식 (cache: origin data copy data)
    - browser sends all HTTP requests to chace
        - object in cache: cache returns object
        - else cache requests object from origin server, then returns object to client
        - proxy server가 한번 보낸 data는 cache로 저장하기 때문에 가능
        - origin이 멀고 proxy가 가까우면 좋은 전략이 됨.
        
        
    - cache acts as both client and server
    - typically cache is installed by ISP (Internet Service Provider)
        - 보통 대학 회사 등에 설치. 유저들과 지리적으로 가까운 곳에 설치해야 origin으로 부터 proxy가 가깝기에 성능 향상. propagation delay를 줄이는 것.
    - why Web caching?
        - reduce response time for client request (cache가 해당 object를 가지고 있을 경우.)
        - reduce traffic on an institution’s access link
            - 기관에서 일어나는 access link의 traffic을 줄일 수 있어 외부로 나가는 Network를 줄이기에 경제적으로 이점을 가질 수 있음. 빠른 속도.
        - Internet dense with caches: enables “poor” content providers to effectively deliver content
            - 현재 인터넷은 많은 캐쉬를 통해 서비스를 제공하고 있으며, 돈이 없는 제공자들의 인터넷에 많은 트래픽이 일어나도 캐쉬 서비스를 통해 비용을 절감할 수 있다.
    - Proxy server로 접근하는 것은 client 브라우저에서 설정하는 것.
    - Caching을 통해 Response Time 줄이는 예제
        
        
        - 클라이언트가 서버로부터 요청하는 object의 평균 사이즈 100K, 평균 요청 rate는 초당 15회라면 초당 1.5Mbps의 데이터를 다운받아야 함.
        - Traffic Intensity → 1.50/1.54 거의 1에 가까운 굉장히 위험한 상태, Queueing Delay가 엄청 늘어남.
        - Lan Utilization은 1.50Mbps/1000Mbps → 0.15%
        - Access Link Utilization = 99%( Queueing Delay가 엄청 큼을 알 수 있음.)
        - total delay = Internet delay + access delay + LAN delay
            
            = 2 sec + minutes(Queueing Delay) + usecs (Institutional network에 도착하면 거의 delay가 없기에 Micro에 가까움)
            
        - access link를 100배 154Mbps로 늘리면
            - access link utilization 0.99%
            - 2 sec + msecs + usecs —> access link를 늘리는 것이 굉장히 비쌈.
        - **Cache를 둔다면?**
            - 얼마나 많은 정보가 local web cache에 저장되었느냐에 따라 access link utilization, total delay가 정해짐.
            - access link의 utilization을 계산하기 위해선 가정해야 함.
            - hit rate 0.4로 가정 (LAN이 요청 데이터를 갖고 있을 확률 40%)
            
            
            - 60%의 요청만 access link를 통해 다운받기 때문에 0.6 * 1.50Mbps = 0.9Mbps
            - utilization → 0.9/1.54 = 0.58
                - 99% → 58% 개선
            - **total delay 계산**
                - 154Mps로 많은 가격을 들인 것보다 cache를 두는 것이 더 좋은 효율을 만들 수 있다.
    - Cache로 저장하고 있긴 하지만 그 정보가 origin server에서 바뀔 수도 있음.
    - Proxy는 항상 본인이 가지고 있는 Cache가 Origin Data와 같은지 비교를 해야 함.
        
        
    - HTTP request msg If-modified-since 메세지를 통해 파악
        - client가 보낸 date와 server의 수정 date를 비교하여 수정 date가 더 이르면 Not modified를 주고, 이를 통해 proxy cache에서 데이터를 가지고 오는 것.
        - 그래서 사실 위 계산에선 빠졌지만 proxy는 요청을 받으면 서버에게 한번 물어봐야함.
        - not modified는 data를 갖고 있지 않기에 utilization에 영향을 주진 않음. 즉 modified 요청과 응답은 매우 가벼움.
