# 04_Network_Security&History

- **Network Security**
    - Hacker → put malware into hosts via internet
    - Malware
        - Virus → 자가복제 감염 (다운 받은 후 실행해야 감염)
        - Worm → 스스로 실행 (다운 받자마자 실행)
    - Spyware
        - keystroke 저장
        - 웹 방문 기록 저장 (광고 등에 이용됨)
    - host가 감염되어 Botnet에 올라간다면, 디도스의 위험.
    - **DDos (Distribute Denial of service)**
        - Attackers make resources (server, bandwidth) unavailable to legitimate traffic by overwhelming resource with bogus traffic
        - Attacker가 어떤 서버가 갖고 있는 resource를 모두 사용하게 만들어버림
            - 정상적인 Traffic이 해당 resource를 사용하지 못함
        - Target을 선정하고 Botnet에 속한 모든 컴퓨터가 해당 타겟 서버에 메세지를 보냄. 서버는 메세지가 왔으니 처리를 해야만 하고, 많은 Resource를 사용하기에 정상적인 Message, Packet이 거부됨.
            
            
    
    - **Packet Sniffing**
        
        
        - promiscuius network interface reads/records all packets passing by.
        - B가 A에게 링크를 보낼 때 해당 Link가 shared link인 경우 C가 해당 link를 볼 수 있음
            - Network Interface를 promiscuous로 변경할 경우 본인에게 오는 packet이 아님에도 볼 수 있음
        - broadcast media (shared Ethernet, wireless)
        - wireshark
            - 모든 packet을 볼 수 있음 (화이트 해커쪽)
    
    - **IP spoofing**
        
        
        - send packet with false source address
        - C가 A에게 B가 보내는 것처럼 만들어 보냄.
            - 이를 통해 B가 보낸 줄 알고 어떤 resource를 처리하게 됨.
        
- Internet History
    - 1961 Kleinrock → Packet Switching 등장
        - 기존 Circuit Switching만 있었으며, 소련이 이를 공격하여 통신망을 마비 시켜도 통신 가능하게 하기 위해 발명
    - 1972 - 1980 새로운 Internetworking이 생기기 시작
    - 1974 Cerf and Kahn → interconnecting에 대한 설계 고안 오늘 날의 인터넷 Architecture에 기반이 되는 상호 연결의 기반을 만들어냄.
    - early 1990s Web이 생기며 Berners-Lee의 HTML
