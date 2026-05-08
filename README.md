# NetSpecter

**NetSpecter** is a lightweight yet powerful asynchronous OSINT and reconnaissance engine built in Python.  

It combines multi-source intelligence gathering (DNS, WHOIS, Web, TLS, HTTP, Geo, Reverse DNS) with Shodan-powered security intelligence and full raw data access, providing a complete target profile and risk assessment.

---

## Disclaimer

NetSpecter is developed for **educational use** and **authorized security research** only.

This tool performs reconnaissance and gathers publicly accessible intelligence from multiple sources.  
Any use of NetSpecter against systems, networks, or domains **without explicit permission from the owner is strictly prohibited**.

The author assumes **no liability and is not responsible** for any misuse, damage, or legal consequences resulting from the use of this tool.

By using NetSpecter, you agree to:
- Use it only on systems you own or are authorized to assess
- Comply with all applicable local, national, and international laws
- Take full responsibility for your actions

If you are unsure about the legality of your actions, **do not use this tool**.

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

### TLS Intelligence
- Extracts certificate subject and issuer details
- Analyzes certificate validity period
- Collects Subject Alternative Names (SAN)
- Identifies certificate authority (CA)
- Provides signals for infrastructure relationship analysis

---

### HTTP Fingerprinting
- Extracts server and backend technology indicators
- Analyzes HTTP status and redirect behavior
- Collects security headers (HSTS, CSP, X-Frame-Options, etc.)
- Identifies session and cookie behavior signals
- Extracts page title information
- Infers framework hints from response headers

---

### Security Analysis
- Detects exposed services:
  - SSH (22)
  - RDP (3389)
  - MySQL (3306)
- Identifies vulnerability presence
- Includes OS information (from Shodan intelligence)

---

### Risk Scoring System
- Classification:
  - LOW
  - MEDIUM
  - HIGH
  - CRITICAL
- Based on exposed services and vulnerabilities


---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/s-r-e-e-r-a-j/NetSpecter.git
```
### 2. Navigate to the NetSpecter directory 
```bash
cd NetSpecter
```

### 3. Create a Virtual Environment
```bash
python3 -m venv venv
```
*Activate it:*

**Linux / macOS**
```bash
source venv/bin/activate
```
**Windows**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip3 install -r requirements.txt
```
### 5. Configure Shodan API Key

Edit the configuration file:

```ini
netspecter.cfg
```
**Add your API key:**
```ini
[SHODAN]
api_key=YOUR_API_KEY
```
**Important:**
- Do NOT use single quotes `' '` or double quotes `" "` around the API key
- Add the key directly as plain text

*Correct:*
```ini
api_key=abc123xyz456
```
*Incorrect:*
```ini
api_key="abc123xyz456"
```
```ini
api_key='abc123xyz456'
```

--- 

## Command Line Usage

NetSpecter provides a simple CLI interface.

### Basic Syntax

```bash
python3 -m netspecter <command> [options]
```

### Recon Command
Run reconnaissance on a target:
```bash
python3 -m netspecter recon <target>
```

### Options

| Option      | Description                                      |
|-------------|--------------------------------------------------|
| `--full`    | Enable full intelligence scan (Shodan integration) |
| `--timeout` | Set HTTP request timeout (default: 5 seconds)     |
| `--json`    | Output results in JSON format                     |

### Notes

- `<target>` can be a domain (e.g., `example.com`) or an IP address  
- When `--full` is used, NetSpecter attempts to resolve the domain to an IP address for Shodan lookup  
- If Shodan intelligence is not available for a domain, try using:
  - the direct IP address, or  
  - the resolved IP of the domain  
- `--full` requires a valid Shodan API key  
- Without `--full`, only basic reconnaissance modules are executed


### Examples
**Basic recon:**
```bash
python3 -m netspecter recon example.com
```
**Full scan with Shodan intelligence:**
```bash
python3 -m netspecter recon scanme.org --full
```
> Shodan operates on IP addresses. If a domain does not return results, use its resolved IP address for better accuracy

**Custom timeout:**
```bash
python3 -m netspecter recon example.com --timeout 10
```

**JSON output:**
```bash
python3 -m netspecter recon example.com --full --json
```

**Save JSON output to a file:**
```bash
python3 -m netspecter recon example.com --full --json > result.json
```
> Output will be saved as valid JSON in `result.json`

---

## Output

NetSpecter supports multiple output formats:

- **Default:** Pretty-printed structured output (human-readable)
- **JSON (`--json`):**
  - Colored JSON in terminal
  - Clean JSON when redirected to a file

Example:

```bash
python3 -m netspecter recon example.com --json > result.json
```

## License
This project is licensed under the MIT License.

