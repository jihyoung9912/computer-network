# 09_CDNS

- Content Distribution Networks
- CDN: stores copies of content at CDN nodes
    - eg: Netflix stores copies of MadMen
- subscriber requests content from CDN
    - directed to nearby copy, retrieves content
    - may choose different copy if network path congested
        - client가 where to request chunk 를 발휘하는 것
    - 여러 군데에다 copy를 해놓고 client가 요청한다면 가장 효율적인 server에서 manifest를 다운받음.
- **Over the Top**
    - 위의 서비스 방식을 의미. top 은 setup box를 의미
- OTT Challenges: coping with a congested Internet (혼잡이 발생했을 때의 문제
    - from which CDN node to retrieve content?
    - viewer behavior in presence of congestion?
    - what content to palce in which CDN node?
        - 지역별로 유명한 컨텐트를 해당 지역 가까운 CDN node에 미리 분배
- CDN content access: a closer look
    
    
    1. Bob gets URL for video (http://netcinema.com/6Y7B23V)
        1. 최초로 요청하는 과정.
    2. resolve [http://netcinema.com/6Y7B23V](http://netcinema.com/6Y7B23V) in Bob’s local DNS
    3. netcinema’s DNS returns URL http://KingCDN.com/NetC6y&b23V
        1. netcinema가 가까운 즉 Bob이 가장 효율적으로 요청해야할 CDN 을 알려줌
    4. Resolove [http://KingCDN.com/NetC6y&b23V](http://KingCDN.com/NetC6y&b23V), returns IP address of KingCDN server with video
    5. local DNS가 Bob의 Server에 해당 정보를 알려줌
    6. request video from KingCDN
        1. http를 통해 file들의 chunk를 다운로드 받게 되는 것.
            
            
    - 3-4 번에서 받은 manifest file을 통해 어떤 CDN server에 어떤 chunk가 있는지를 알 수 있고, 어느 서버에 DASH를 요청해야할지 파악하고, 해당 서버에 요청을 보내게 됨.
