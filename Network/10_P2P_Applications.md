# 10_P2P_Applications

- Pure P2P Architecture
    - no always-on server (peer들 사이 통신)
    - arbitrary end systems directly communicate
        - 임의의 엔드 시스템간의 직접 소통
    - peers are intermittently connected and change IP addresses
        - ex) file distribution (Torrent), Streaming, VoIP
- File distribution: client-server vs P2P
    
    
    - client-server
    - **server transmission**
        - must sequentially send (upload) N file copies: 서버가 파일을 업로드하는 시간
            - time to send one copy : F / u second
            - time to send N copies: NF / u second
    - client
        - each client must download file copy: 클라이언트가 파일을 다운로드 하는 시간
            - dmin = min client download rate (최소)
            - min client download time: F / dmin
            
            
            - 파일 전송 전체의 시간은 적어도 server upload or client down 중 더 큰 시간보다는 크다
            - 위 식에서 F/dmin 은 크게 차이가 없지만, NF/us 에서 큰 차이. N이 많으면 많을수록 서버가 보내줘야 하는 양이 많아 시간이 길어짐.
    - **P2P**
    - server-transmission
        - must upload at least one copy (최초 1회는 보내야 클라이언트간 P2P 구조가 가능함)
            - time to send one copy: F/us
    - client
        - each client must download file copy
            - min client download time: F/dmin
    - clients
        - as aggregate must donwload NF bits
            - 어쨋든 N개의 클라이언트가 다운로드를 받는다는 것은 N개의 copy가 업로드 되어야 함을 의미
                
                
            - max upload rate → 최초 1회 서버의 업로드 us, 유저들의 업로드 시그마 ui → NF bits 업로드. ui 의 개수는 N-1일 것임.
            - N이 늘어나는 경우에도 분자인 NF의 값이 늘어나지만, N이 늘면 시그마 ui 즉 분모도 늘어나기에 효율적인 방안이라고 볼 수 있음.
                
                
                - Client-Server는 Node가 증가할수록 linear하게 증가하지만, P2P에선 N이 늘어나도 시간이 크게 증가하지 않음.
- P2P file distrbutuin: **BitTorrent**
    - file divided into 256Kb chunks
    - peers in torrent send/receive file chunks
        
        
    - 기생충 영화를 공유한다면, 영화가 하나의 torrent가 되는 것.
    - torrent에 어떤 peer가 있는지를 관리하는 것 → tracker
        - peer들의 요청은 tracker에게 간 후 조정을 통해 다운로드 받게 되는 것.
    - 과정
    - peer joining torrent:
        - has no chunks, but will accumulate them over time from other peers
        - registers with tracker to get list of peers, connects to subset of peers (neighbors)
        - 최초에는 아무런 chunk가 없지만, 시간이 지나며 축적됨. tracker에게 요청하여 다른 peer들의 정보를 받고, 필요한 chunk를 받기 위한 만큼의 peer들과 연결됨 → neighbors
        - 이렇게 다운받으며 본인에게도 chunk가 쌓이기에, 본인의 Chunk를 업로드 하기도 함.
    - while downloading, peer uploads chunks to other peers
    - peer may change peers with whom it exchanges chunks
    - churn: peers may come and go
    - once peer has entire file, it may (selfishly) leave or (altruistically) remain in torrent
    
- BitTorrent: requesting, sending file chunks
    - **requesting chunks**
        - at any given time, different peers have different subsets of file chunks
            - 최초 어떤 peer가 어떤 chunk의 subset을 가지고 있는지 모름 (A: 1,3,5 B:2,4)
        - periodically, Alice asks each peer for list of chunks that they have
            - Alice는 주기적으로 peer들에게 어떤 chunk의 subset을 가지고 있는지 물어봐야함
        - Alice requests missing chunks from peers, **rarest first**
            - 본인이 없는 chunk를 갖고 있는 peer에게 요청.
            - 1000개가 부족하다고 1000개를 모두 요청할 수 없으니 rarest first 방식 사용.
                - 3번은 10명의 peer, 5번은 3명, 7번은 1명의 peer가 chunk를 갖고 있다면, 가장 적은 peer들에게 존재하는 chunk를 먼저 요청, 즉 7번부터 요청
    - **sending chunks: tit-for-tat**
        - 100명의 peer들에게 요청을 받아도 모두 줄 수 없음. 골라서 보내야 하는데, 이때 tit-for-tat 정책
        - 나한테 chunk를 준 적이 있다면 그 사람부터 줌.
        - Alice sends chunks to those four peers currently sending her chunks at highest rate
            - 여러 peers의 요청이 온다면, 가장 최근 나에게 가장 빠른 속도로 chunks를 주고 있는 4명의 peers 선정
            - other peers are chocked by Alice (do not receive chunks from her)
            - re-evaluate top 4 every 10 secs (매 10초마다 선정)
        - every 30 secs: randomly select another peer, starts sending chunks
            - 최초에 들어간 유저는 아무것도 못받을 가능성이 높기에.
            - optimistically unchoke. this peer
            - newly chosen peer may join top 4
            - top 4는 계속적으로 변하고, 새로운 유저도 optimistically unchoke 기능으로 받을 수 있음.
