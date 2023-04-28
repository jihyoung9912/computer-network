# 09_DNS

- People
    - many identifiers : SSN, name, passports…
- Internet hosts, routers
    - IP address 32bit used for addressing datagrams → 사람이 외우기엔 쉽지 않기에 name
    - name → [www.google.com](http://www.google.com) used by humans
    - Q) IP address와 name 간의 mapping처리는 어떻게 되는가?
- **Domain Name System**
    - distributed database
        - 분산 데이터베이스
        - 중앙 데이터베이스에 모든 매핑을 저장하는 것이 아니라 분산해서 저장.
    - application-layer protocol
        - hosts와 name servers의 communicate를 통해 IP address에 대한 도메인 name을 달라 등 조정
            - core-function이지만 application-layer에 있는 이유는 network의 complexity는 모두 edge에 존재해야 하는 철학을 따른 것, 쉬운 것들은 core.
        
- DNS services
    - hostname to IP address translation
    - host aliasing
        - 같은 Host라도 여러 개의 name을 가질 수 있음.
            - 하나를 canonical, 다른 하나를 alias name
    - mail server aliasing
    - load distribution
        - 웹 서비스의 요청이 왔을 때 DNS를 통해 load 분산
        - 어떤 요청이 DNS로 왔을 때, 현재 서버들 중 가장 부하가 (load) 적은 물리적인 컴퓨터의 IP address를 return. 즉 부하를 분산시키는 것.
    - why not centralize DNS? 중앙 집중 안하는 이유?
        - single point of failure
            - DNS 서버가 죽는다면 어느 누구도 DNS를 사용할 수 없는 위험.
        - traffic volume
        - distant centralized database
            - 미국과 우리 나라 사이의 propagation delay
        - maintenance
            - 계속적으로 변화하는 IP address에 높은 유지력
    
- DNS → distributed, hierarchical database
    
    
    - 각각의 서버들이 본인만의 DB를 가지고 있음.
    - client가 [www.amazon.com](http://www.amazon.com) 에 대한 IP를 찾으려고 한다면,
        1. Root server가 .com DNS server를 찾아 알려줌
        2. .com DNS server가 [amazon.com](http://amazon.com) DNS server를 알려줌
        3. [amazon.com](http://amazon.com) DNS server가 www.amazon.com의 IP 주소를 물어봄.
    
- DNS **root name servers**
    - contracted by local name server that can not resolve name
        - local name server가 name을 해석하지 못할 때 DNS 접근
    - root name server
        - contacts authoritative name server if name mapping not known
            - 만약 name maaping이 안되면 authoritative name server (최종적으로 실제 IP address mapping 값을 가진 것)에 연결. 다른 서버의 값들은 전부 copy
        - gets mapping
        - returns mapping to local name server
- **TLD, authoritative servers (Root name server 밑에 존재)**
    - top-level domain servers
        - responsible for com, org, net, edu, aero, jobs, museums, and all top-level country domains
        - Network Solutions maintains servers for .com TLD
        - Educause for .edu TLD
    - authoritative DNS servers
        - organization’s own DNS server, providing authoritative hostname to IP mappings for organization’s named hosts
            - 어떤 기관의 DNS 서버를 소유하여 권위있는 host name IP를 mapping
            - 권위라는 것은 진짜라는 의미. 다른 것들은 복사 본이며, 진짜 데이터를 의미함.
            - 즉 어떤 주소의 진짜 IP Address는 Authoritative server에 있음.
        - can be maintained by organization or service provider
- Local DNS name Server
    - does not strictly belong to hierarchy
    - each ISP (residential ISP, company, university) has one
        - also called default name server
    - when host makes DNS query, query is sent to its local DNS server
        - has local cache of recent name-to-address translation paris
        - acts as proxy, forwards **query** into hierarchy
    - hierarchy에 속하는 것은 아니지만, ISP에서 하나씩 가지고 있음.
    - 일반적인 host에서 모든 mapping을 저장하지 못하기에 name server에게 요청하는 것.
    - 요청을 보낼 때 Local name server로 보낸다고 생각하면 됨.
    - 해당 기관에 속하는 다양한 host에서 오는 요청들에 관하여 mapping에 대한 정보를 찾고, caching을 해놓음.
    - 같은 query가 온다면 해당 정보를 바로 보내주면 됨.

- DNS name resolution example 두가지
    - host at [cis.poly.edu](http://cis.poly.edu) wants IP address for gaia.cs.umass.edu
    - iterated query (하나씩 순서대로 접근)
        
        
        - contacted server replies with name of server to contact
        - local server가 있으면 local이, 없으면 해당 server에.
    - recursive query
        
        
        - local server의 부담을 줄이는 과정이지만, 타 서버들의 부하가 너무 큼
        - 보안 관점에서 취약하기에 DNS들이 지원하지 않는 추세
- DNS: caching, updating records
    - once name server learns mapping, it caches mapping
        - name server들은 매핑 즉 정보를 얻으면 캐싱을 해놓게 됨.
        - cache entries timeout (disappear) after some time (TTL)
            - 무한정 하는 것이 아님. 정보가 수정이 되었다면 가져올 수 없기에, timeout value가 존재함. (TTL)동안 유지 → 잘못된 정보가 TTL만큼 존재할 수도 있다.
        - TLD servers typically cached in local name servers
            - TLD 주소는 잘 바뀌지 않기에 local에서 그치지, TLD server까지 잘 가지 않음.
    - Cached entries may be out-of-date
        - if name host changes IP address, may not be known Internet-wide until all TTLs expire
        - 만약 시간이 지나지 않았는데 데이터가 바뀌는 것은 어쩔 수 없다. 바뀌어도 Internet은 이를 감지할 수 없음.
- DNS records (DNS의 reocods를 cache에 저장 즉 mapping 하는 것)
    - DNS: distributed database storing **resource records** (RR)
        - **RR format (name, value, type, ttl)**
        - type에 따라 name과 value가 달라진다.
        - type = A
            - name is hostname (www.foo.com)
            - value is IP address
        - type = NS
            - name is domain (foo.com)
            - value is hostname of authoritative name server for this domain (IP address가 아니라 도메인을 담당하는 authoritative name의 hostname)
        - type = CNAME
            - name is alias name for some canonical name
            - [www.ibm.com](http://www.ibm.com) is really, [servereast.backup2.ibm.com](http://servereast.backup2.ibm.com) is alias name
            - value is canonical name
        - type = MX
            - value is name of mailserver associated with name
- DNS protocol, messages
    - DNS의 메세지 타입 두 가지 : query, reply (both with same message format)
    
    - query를 보낼 때 임의의 값을 id로 설정하여 보내고, reply 받을 때 해당 임의의 값과 같은 값으로 보낸다. 이를 통해 query에 대한 맞는 reply를 매칭하며 구분할 수 있음. local DNS는 무수히 많은 query를 받고 reply를 보낸다. 이때, query의 reply를 비동기적으로 실행하기 위해 id를 통해 식별하는 것.
    - questions
        - name, type fields for a query (원하는게 IP address인지 domain name인지 등)
    - answers
        - RRs in response to query (query에 대한 응답)
    - authority
        - records for authoritative servers
    - additional info
        - additional helpful info that may be used
- Inserting records into DNS example
    - register name [networkuptopia.com](http://networkuptopia.com) at DNS registrar
        - provide names, IP addresses of authoritative name server (primary secondary → 서버가 죽을 수도 있기에 두개)
        - registrar inserts two RRs into .com TLD server
            - NS Type, networkutopia.com, [dns1.networkutopia.com](http://dns1.networkutopia.com), TTL 으로 저장
            - A Type, dns1.networkutopia.com, 212.212.212.1, TTL 으로도 저장 → IP address를 알아야 접속할 수 있기에.
        - create authoritative server type A record for www.networkuptopia.com
        - type MX record for networkuptopia.com
        
- Attacking DNS
    - DDos attacks
        - bombard (폭격) root servers with traffic
            - not successful to date
            - traffic filtering
            - local DNS servers cache IPs of TLD servers, allowing root server bypass
        - bombard TLD servers
            - potentially more dangerous
    - redirect attacks
        - main-in-the-middle
            - Intercept queries
                - local DNS server가 TLD server에게 보내는 query는 UDP (암호화 X) intercept 후, header의 id를 가져와 다른 요청을 보낼 수 있음.
        - DNS poisoning
            - send bogus replies to DNS server, which caches
    - exploit(악용) DNS for DDOS
        - send queries with **spoofed** **source** address : target IP
        - DNS서버에세 query를 보낼 때, 내가 공격하려는 IP 주소를 source IP address로 쓴다. 요청을 받은 DNS 서버는 reply를 해야하고, reply는 해당 타겟의 IP address로 간다. target에게 엄청나게 많은 reply를 줌으로 DDOS Attack이 가능하다.
