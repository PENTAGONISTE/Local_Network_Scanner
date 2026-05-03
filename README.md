# MAC Lookup — Local Network Scanner

A Python tool that scans your local network using ARP requests, collects the IP and MAC address of every active device, and looks up the hardware vendor for each one using the [MAC Vendors API](https://macvendors.com/).

Results are printed to the terminal and saved to a `scan_results.json` file.

## Example Output

```json
{
    "a4:c3:f0:xx:xx:xx": {
        "IP": "192.168.1.1",
        "vendor": "Raspberry Pi Trading Ltd"
    },
    "dc:a6:32:xx:xx:xx": {
        "IP": "192.168.1.5",
        "vendor": "Apple, Inc."
    }
}
```

## Requirements

- Python 3
- [Scapy](https://scapy.net/)
- [Requests](https://docs.python-requests.org/)

Install dependencies:
```bash
pip install scapy requests
```

## Usage

> **Note:** Scapy requires root/admin privileges to send raw packets.

```bash
sudo python mac_lookup.py
```

The script will:
1. Detect your local network range automatically
2. Send ARP broadcast packets to discover active devices
3. Look up the vendor for each MAC address
4. Save results to `scan_results.json`

## Notes

- The MAC Vendors API is rate-limited, so the script waits 2 seconds between lookups.
- Tested on Linux. May require additional setup on Windows/macOS for Scapy.
