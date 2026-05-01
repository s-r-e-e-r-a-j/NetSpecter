# NetSpecter

**NetSpecter** is a lightweight yet powerful asynchronous OSINT and reconnaissance engine built in Python.  

It combines multi-source intelligence gathering (DNS, WHOIS, Web, Geo, Reverse DNS) with Shodan-powered security intelligence and full raw data access, providing a complete target profile and risk assessment.

---

## Features

### Reconnaissance Engine
- DNS enumeration (A, MX, NS, TXT)
- WHOIS lookup
- Reverse DNS resolution
- Web probing (status, server, title extraction)
- Geo/IP intelligence

---

### Intelligence Engine (`--full`)
- Shodan host intelligence via official SDK
- Open port and service discovery
- Banner and version extraction
- OS, ASN, ISP, and organization detection
- Vulnerability detection (CVE presence)

---

### Raw Intelligence Access
- Includes full raw Shodan API response
- Enables advanced analysis and custom parsing
- Preserves original data without filtering or loss

---

### Security Analysis
- Detects exposed services:
  - SSH (22)
  - RDP (3389)
  - MySQL (3306)
- Identifies vulnerability presence
- Provides OS fingerprint insights

---

### Risk Scoring System
- Classification:
  - LOW
  - MEDIUM
  - HIGH
  - CRITICAL
- Based on exposed services and vulnerabilities
