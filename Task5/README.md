# Wireshark Network Traffic Analysis

## 1. Objective

The objective of this activity was to capture and analyze live network
traffic using Wireshark and identify basic protocols, packet types, IP
addresses, ports, and notable network events.

## 2. Capture Information

-   **Capture file:** `wireshark result .pcapng`
-   **Capture interface:** `eth0`
-   **Interface link type:** Ethernet
-   **Capture size:** 6,084 bytes
-   **Packets in the supplied capture:** **52**
-   **Captured traffic:** IPv4, IPv6, ARP, TCP, UDP/DNS, and ICMP

> **Important:** The supplied `.pcapng` file contains 52 packets. If the
> original Wireshark window showed approximately 13,000 packets, this
> uploaded file appears to be a smaller/filtered capture rather than the
> full original capture.

## 3. Protocol Summary

  Protocol / Traffic     Packets Evidence
  -------------------- --------- -----------------------------------------------
  TCP                         25 IPv4 TCP traffic, mainly destination port 443
  UDP                         19 DNS queries/responses
  ICMP                         2 ICMP Destination Unreachable
  ARP                          2 ARP traffic
  IPv6                         4 IPv6 Ethernet frames
  IPv4                        46 IPv4 Ethernet frames

The capture therefore contains more than the required three protocols.

## 4. Local Host

The main captured host is:

**10.0.2.15**

This is the source address of the Kali machine in the capture.

The DNS server observed is:

**10.0.2.3**

## 5. DNS Analysis

DNS traffic was carried using UDP port **53** between `10.0.2.15` and
`10.0.2.3`.

### Observed DNS queries

  Domain                    Query Type               Observed Requests
  ------------------------- ---------------------- -------------------
  `chatgpt.com`             A (IPv4)                                 2
  `chatgpt.com`             AAAA (IPv6)                              1
  `chatgpt.com`             HTTPS/SVCB (type 65)                     1
  `zws5.web.telegram.org`   A (IPv4)                                 6
  `zws5.web.telegram.org`   AAAA (IPv6)                              3
  `httpforever.com`         A (IPv4)                                 4
  `httpforever.com`         AAAA (IPv6)                              1
  `httpforever.com`         HTTPS/SVCB (type 65)                     1

### DNS examples

A DNS request for:

`chatgpt.com`

was sent from:

`10.0.2.15 → 10.0.2.3`

using UDP destination port `53`.

A DNS request for:

`zws5.web.telegram.org`

was also sent to `10.0.2.3:53`.

The capture includes both DNS requests and DNS responses.

## 6. TCP / HTTPS Traffic

There are **25 TCP packets** in the supplied capture.

The TCP traffic is primarily directed to destination port **443**, which
is normally used for HTTPS.

Observed destination IP addresses include:

-   `172.64.155.209:443`
-   `104.18.32.47:443`
-   `149.154.170.200:443`

Examples of TCP connections initiated by the local host include:

  Source              Destination             Protocol
  ------------------- ----------------------- ----------
  `10.0.2.15:50674`   `172.64.155.209:443`    TCP
  `10.0.2.15:41980`   `104.18.32.47:443`      TCP
  `10.0.2.15:56346`   `149.154.170.200:443`   TCP
  `10.0.2.15:45730`   `149.154.170.200:443`   TCP

The TCP packets visible in this supplied capture are SYN packets (`SYN`
flag set). Multiple repeated SYN packets are present, indicating
repeated connection attempts/retransmissions.

### Important observation

Although TCP port 443 is present, the supplied capture does **not**
contain enough visible application-layer information to claim that HTTP
payloads were captured. Port 443 normally indicates HTTPS/TLS traffic,
but the exact application protocol should be confirmed with Wireshark's
protocol dissection.

## 7. ICMP Analysis

Two ICMP packets were captured.

Both packets were:

`10.0.2.15 → 10.0.2.3`

The ICMP type/code bytes identify them as:

**Destination Unreachable --- Port Unreachable**

This is a notable result because it indicates that the destination host
reported that a UDP destination port was unreachable.

## 8. ARP Analysis

Two ARP packets were captured.

The Ethernet addresses show communication between the Kali VM and the
VirtualBox-style network gateway/local network device.

ARP is used to resolve an IPv4 address to a MAC address on the local
Ethernet network.

## 9. IPv6 Traffic

Four Ethernet frames use EtherType `0x86DD`, which identifies IPv6.

These frames demonstrate that IPv6 traffic was also present on the
interface during the capture.

The supplied packet data does not provide enough decoded IPv6
information to make a reliable application-level identification, so no
further protocol claim is made here.

## 10. Useful Wireshark Filters

The following filters can be used to reproduce the analysis:

### DNS

``` text
dns
```

### DNS queries only

``` text
dns.flags.response == 0
```

### TCP

``` text
tcp
```

### TCP port 443

``` text
tcp.port == 443
```

### TCP SYN packets

``` text
tcp.flags.syn == 1
```

### TCP initial SYN packets

``` text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

### ICMP

``` text
icmp
```

### ARP

``` text
arp
```

### IPv6

``` text
ipv6
```

### Combined useful filter

``` text
dns or tcp.port == 443 or icmp or arp
```

## 11. Key Findings

1.  The supplied capture contains **52 packets**.
2.  The local Kali host is **10.0.2.15**.
3.  The DNS server observed is **10.0.2.3**.
4.  DNS traffic used UDP port **53**.
5.  DNS queries were observed for `chatgpt.com`,
    `zws5.web.telegram.org`, and `httpforever.com`.
6.  **25 TCP packets** were observed, primarily targeting TCP port
    **443**.
7.  The capture contains **2 ICMP Destination Unreachable / Port
    Unreachable packets**.
8.  **2 ARP packets** and **4 IPv6 frames** were also observed.
9.  Several repeated TCP SYN packets indicate repeated connection
    attempts/retransmissions.
10. The capture demonstrates multiple layers of network communication:
    Ethernet, ARP, IPv4/IPv6, TCP, UDP/DNS, and ICMP.

## 12. Conclusion

The Wireshark capture demonstrates normal network activity from the Kali
Linux host. DNS was used for domain-name resolution, TCP connections
were initiated toward HTTPS port 443, ARP handled local address
resolution, IPv6 frames were present, and ICMP reported
destination-port-unreachable events.

The analysis shows how Wireshark can be used to move from a large packet
capture to a small set of meaningful observations by filtering traffic
according to protocol, port, and packet characteristics.
