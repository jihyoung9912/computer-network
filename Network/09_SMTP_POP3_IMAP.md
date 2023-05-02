# 09_SMTP_POP3,IMAP

- Electronic mail 동작
    
    
    - Three major components
        - user agents
        - **mail servers**
            - mailbox contains incoming messages for user
            - message queue of outgoing (to be sent) mail messages
            - SMTP protocol between mail servers to send email messages
                - 해당 작업에는 주고 받는 단 두개의 mail server만 관여함.
                - client: sending mail server
                - server: receiving mail server
        - simple mail transfer protocol: SMTP
            - mail server 사이 사용하는 protocol
    - User Agent
        - “mail reader”
        - composing, editing, reading mail messages
        - Outlook, Thunderbird, iPhone mail client
        - outgoing, incoming messages stored on server
            - 각각의 사용자가 가입한 이메일에 해당되는 mail server가 있음.
    - SMTP
        - uses TCP to reliably transfer email message from client to server, port 25
            - 메일이 중간에 유실되거나 해서는 안되기 때문에 reliable data transfer가 필요하기에 TCP
        - direct transfer: sending server to receiving server
            - 중간에 다른 서버를 거치거나 하지 않고 무조건 direct
        - three phases of transfer 세 개의 단계
            - handshaking (HTTP와 다른 점. HTTP는 req, res 두개지만, handshaking message, closure 통신을 종료하는 메세지 등 여러가지 command가 추가적으로 필요함)
            - transfer of messages
            - closure
        - command/response interaction (like HTTP)
            - commands : ASCII text (HTTP와 비슷한 맥락이지만 더욱 많은 command)
            - response: status code and phrase
        - message must be in 7-bit ASCII
            - 이미지와 같은 데이터들은 base 64 등을 이용해 binary를 ASCII 7-bit로 encoding하여 사용
    - Scenario
    
    
    - 보통 2번 4번에서 SMTP 사용
    
    
    - 일반적인 SMTP 사용시 암호화가 전혀 되어 있지 않기에 보안의 위험.
    - SMTP uses persistent connections
        - connection이 유지된 상태에서 req, res가 계속 오고 감. non-persistent connection일 경우 req-res 1회 이후 connection closure
    - SMTP requires messages (header & body) to be in 7-bit ASCII
    - SMTP server uses CRLF.CRLF to determine end of message
    - **comparison with HTTP**
        - HTTP: pull
            - Client가 Server에 접속해서 Server에 데이터를 달라.
        - SMTP: push
            - Client가 상대방 Server에 접속해서 나의 데이터를 보내는 것.
        - both have ASCII command, response interaction, status codes
        - HTTP: each object encapsulated in its own response message
            - 하나의 메세지 각각의 object 하나씩
        - SMTP: multiple objects sent in multipart message
            - 하나의 메세지에 여러개의 object 합쳐서 여러개씩
    - Mail message format
        - SMTP → email messages의 주고 받음에 관한 protocol
        - RFC 822 → 주고 받는 messages의 format에 관한 standard
        - Header
            - To, From, Subject
            - different from SMTP Mail From, RCPT To: commands
                - 여기 Header에서 적는 값이 실제로 보내지는 값. SMTP와 다르게 작성할 수도 있으며, 만약 같더라도 한번 더 써줘야만 함.
        - Body
            - the Message (ASCII Only)
    - User가 메일을 보내면 SMTP를 통해 sender’s mail server의 mail queue에 들어가고, 이후 receiver’s mail server의 mail box에 들어가게 됨. 이때 receiver는 해당 mail을 어떻게 접근하는가?
    - **Mail access protocols**
        - POP (Post Office Protocol)
        
        
        - IMAP (Internet Mail Access Protocol)
            - POP은 retr 1을 했을 때 dele 1을 함께 보내 mail server box에 있던 1 content가 사라지지만 POP3부터 keep option을 지원하는 것.
            - IMAP도 모든 메세지를 서버에 저장하고 user가 directory를 만들어 관리할 수 있음.
        - HTTP
