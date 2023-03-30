# 04_HTTP_Protocols_Cookies

- **Web and HTTP**
    - web page consist of objects
        - objects: HTML file, JPEG image, Java applet, audio files…
    - web page consists of base HTML file which includes several referenced objects
    - each object is addressable by a URL
        - HTML 파일 안에 여러가지 다른 object file이 있으며 해당 html file, object를 정확하게 식별하고 다운받기 위해서 URL. 모든 object는 URL이 있다.
        
        
- HTTP (Hypertext Transfer Protocol)
    - 웹서비스에서 사용하는 protocol (Web’s application layer protocol)
    - client/server model 사용
        - client
            - browser that request, receives using HTTP and displays Web object
        - server
            - Web server sends using HTTP objects in response to requests
    - HTTP는 Application Layer이기에 Transport Layer에서 서비스를 받아야 하고, TCP UDP 중 TCP를 받는다.
        - uses TCP
            - TCP를 사용한다는 것은 socket을 하나 만든다는 것.
            - client initiates TCP connection → creates socket to server, port 80
            - server accepts TCP connection from client
            - HTTP messages exchanged between browser and Web server
            - TCP 연결로 소켓을 만들고, 소켓을 통해 HTTP 메세지를 주고 받음.
            - 주고 받은 후 TCP connection closed
    - **HTTP is Stateless**
        - server maintains no information about past client requests
        - 과거에 어떤 information을 주고 받았는지 저장하지 않음. 그저 주어진 메세지를 처리하기에 단순하다고 볼 수 있음.
        - State를 저장한다면?
            - 같은 요청이 온다면 아까 받았던 데이터를 사용하라는 식으로 res를 보내기에 효율적일 수는 있음.
            - 하지만 구현이 굉장히 복잡하다.
            - 과거의 모든 데이터를 저장하고 있어야 하는데, 서버 혹은 클라이언트의 서버가 죽게 된다면 상태를 잊게 될 수도 있으며, 이를 방지하는 로직은 굉장히 무겁고 복잡함
    - HTTP connections
        - TCP를 통해 HTTP connection을 할 때의 두가지 방법이 존재.
        - non-persistent HTTP (유지X)
            - at most one object sent over TCP connection
                - 하나의 connection에 하나의 object만. 만약 다른 object가 필요한 경우 새로운 connection을 또 만들어야 함.
                - connection then closed
            - downloading multiple objects required multiple connections
        - persistent HTTP
            - multiple objects can be sent over single TCP connection between client, server
            - 여러개의 object를 single TCP connection으로 가능
            - connection을 만드는 데에 시간이 걸리기 때문에 조금 더 효율적.
    
    - **Non-persistent HTTP**
        - HTTP connection 요청, 수락(accepts), connection, HTTP request, HTTP response, connection close
        - 이후 jpg 10개가 있다면 위의 과정을 10번 반복해야함.
        - **Response Time**
            - **RTT (Round Trip Time)**
                - time for a small packet to travel from client to server and back
            - HTTP response time
                - one RTT to initiate TCP connection
                - one RTT for HTTP request and first few bytes of HTTP response to return
                - file transmission time
                - ***non-persistent HTTP response time = 2RTT + file transmission time***
                
                
    - Persistent HTTP
        - non-persistent HTTP issues
            - requires 2 RTTs per object + transmission time
            - OS overhead for each TCP connection
                - connection을 위한 OS의 overhead
            - browsers often open parallel TCP connections to fetch referenced objects
                - 브라우저는 보통 persistent HTTP를 할 경우 병렬적으로 여러개의 connections를 열어 진행. 이 또한 네트워크가 무거워지는 문제
        - **Persistent HTTP**
            - several leaves connection **open** after sending response (not closing)
            - subsequent HTTP messages between same client/server sent over open connection
                - 닫히지 않고 계속 열려 있는 connection을 통해 HTTP를 지속적으로 여러개 주고 받는 것.
            - client sends requests as soon as it encounters a referenced object
            - as little as one RTT for all the referenced objects
                - 하나의 object에 대해 one RTT 필요
    - **HTTP request message**
        - connection이 생성된 후 HTTP request message를 통해 통신
        - two types of HTTP message: request, response
        - **HTTP request message**
            - Format → ASCII (사람이 읽을 수 있는 요청 코드만)
            
            
        - Uploading form input
            - POST method
                - web page often includes form input
                    - form data or file data
                    - 파일과 같은 데이터들은 entity body에 들어가게 됨.
                - input is uploaded to server in entity body
            - URL method
                - uses GET method
                - input is uploaded in URL field of request line
                    - URL Method - 검색과 같은 단순 input 들은 GET 요청s + URL 안에 보내는 경우도 있음.
                    - 보내는 데이터가 URL에 들어가게 됨.
        - **Method types**
            - HTTP/1.0
                - GET POST HEAD
                    - HEAD는 GET과 비슷하지만 콘텐츠 유형, 마지막 수정 날짜 및 크기와 같은 리소스를 설명하는 HTTP 헤더만 반환함. body에 어떤 데이터가 담겨 있든 무시하고 HEAD에 대한 응답만 가져옴.
            - HTTP/1.1
                - GET POST HEAD
                - PUT
                    - File을 특정 위치 URL 에 집어 넣는 것.
                - DELETE
    - HTTP response message
    
    
    - HTTP response status codes를 통해 응답 상태 파악.

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
