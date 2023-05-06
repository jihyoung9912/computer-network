# 07_HTTP_Protocols

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

