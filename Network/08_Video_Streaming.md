# 08_Video_Streaming

- Video Streaming and CDNs: context
    - video traffic
        - major consumer of Internet bandwidth
        - Youtube user 10억명, Netflix 75M
        - different users have different capabilities (different bandwidth)
        - 10억명의 요청을 어떻게 처리하는가?
        - Solution: distributed, application-level infrastructure
- Multimedia: video
    - video: sequence of images displayed at constant rate
        - 24 images/sec
    - digital image: array of pixels
        - each pixel represented by bits
    - 이미지의 bit가 많을수록  부담
    - coding: use redundancy within and between images to decrease # bits used to encode image
        - 이미지들 내부 혹은 이미지들 사이의 중복을 활용하는 것. 이를 통해 encode bit를 줄일 수 있음.
            
            
        - spatial (within image) (공간적인 중복 한 image 속 중복을 코딩)
        - temporal (from one image to next) (시간적인 중복 다음 image와의 중복을 코딩)
    - Encoding의 두 종류
    - **CBR (Constant bit rate)**
        - video encoding rate fixed
        - 고정된 bit rate로 encoding 하는 방식
    - **VBR (Variable bit rate)**
        - video encoding rate changes as amount of spatial, temporal coding changes
        - 사람이 많이 움직이는 경우에는 redundancy 사용이 어렵기에 bit rate가 높아져야함. 이에 맞춰 변형하는 방법.
        - Ex)
            - MPEG 1 (CD - ROM) 1.5Mbps
            - MPEG2 (DVD) 3-6 Mbps
            - MPEG4 (often used in Internet, <1Mbps)
            
- Streaming multimedia: Dash
    
    
    - **DASH: Dynamic, Adaptive, Streaming over HTTP**
    - server
        - divides video file into multiple chunks (보통 2초 정도)
        - each chunk stored, encoded at different rates
        - **manifest file**: provides URLs for different chunks
            - 어떤 chunk가 어느 Server의 URL에 있는지를 표시. 모든 chunk의 위치를 저장
    - client
        - periodically measures server-to-client bandwidth
            - 주기적으로 bandwidth를 측정하여 bandwidth에 맞는 chunk를 요청하는 것
            - 즉 같은 영상 2초짜리는 rate별로 다른 화질 별로 존재하는 것.
        - consulting manifest, requests one chunk at a time
            - server에게서 manifest file을 받음
            - chooses maximum coding rate sustainable given current bandwidth
            - can choose different coding rates at different points in time (depending on available bandwidth at time)
    - “**intelligence**” at client : client determines
        - 무엇을 받아야 할지 client가 판단하기에 intelligence
        - when to request chunk (so that buffer starvation, or overflow does not occur)
            - 언제 chunk를 요청할지. 미리 받아놓을지. buffer memory 등 고려하여 결정해야함.
        - waht encoding rate to request (higher quality when more bandwidth available)
            - 어떤 rate를 가진 chunk를 요청할지
        - where to request chunk (can request from URL server that is “close” to client or has high available bandwidth)
            - 어느 서버에 있는 chunk를 요청할지
        - DASH의 좋은 점 → client의 Intelligence를 잘 응용하기에 서버가 모든 client의 상황을 파악하지 않아도 됨. server는 manifest 파일만 보내주면 되는 것.
    
    - Content distribution networks (서버 입장)
        - challenge
            - how to stream content (selected from millions of videos) to hundreds of thousands of simultaneous users?
            - option 1: single, large “mega-server”
                - 하나의 굉장히 큰 서버 하나에서 모든 것을 설치하는 방법.
                - Centralized DNS server를 쓸 때와 마찬가지의 문제점.
                - single point of failure (얘가 죽으면 아무도 서비스를 못받음)
                - point of network congestion (Traffic이 모두 몰림)
                - long path to distant clients (물리적 거리가 멀면 propagation delay가 늘어남)
                - multiple copies of video sent over outgoing link (같은 copy가 수도 없이 많이 전송됨)
            - **this solution doesn’t scale 확장가능성 X**
            - option2: store/serve multiple copies of videos at multiple geographically distributed sites (**CDN**)
                - 지리적으로 분산된 지역의 서버에 copy를 쭉 뿌려 저장하는 것. 많이 뿌리는 것 enter deep, 적게 bring home
                - enter deep: push CDN servers deep into many access networks
                    - close to users
                    - used by Akamai, 1700 locations
                - bring home: smaller number (10개 정도) of larger clusters in POPs near (but not within) access networks
                    - used by Limelight
