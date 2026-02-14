# tcpdump Network Analysis - Hands-On Exercises

**Source Material**: https://www.youtube.com/watch?v=pdUL8iZnghA  
**Generated**: February 10, 2026  
**Estimated Total Time**: 60-70 minutes

---

## Setup Instructions

Before starting the exercises, run the setup script to create the necessary files and directories:

```bash
bash setup_tcpdump_exercises.sh
```

This will create an `exercises/` directory with all required files, sample data, and network scenarios.

---

## Exercise 1: Verify Network Connectivity with ICMP Capture

**Estimated Time**: 8 minutes  
**Difficulty**: Beginner  
**Concepts**: Interface selection, ICMP filtering, basic packet capture

### Objective

You will capture and analyze ICMP (ping) traffic to verify network connectivity and understand how packets flow between your system and a remote host.

### Context

Your team reports intermittent connectivity issues when accessing Google's DNS server (8.8.8.8). Before escalating to the network team, you need to verify whether ICMP packets are being sent and received correctly. This is a fundamental troubleshooting step for diagnosing network problems.

### Tasks

1. List all available network interfaces on your system to identify which interface to monitor
2. Start a continuous ping to 8.8.8.8 in one terminal
3. In another terminal, capture only ICMP traffic from any interface, limiting the capture to 20 packets
4. Observe the captured packets and identify the ICMP request (echo request) and reply (echo reply) packet types
5. Stop the ping process and analyze whether all requests received replies

### Reference

This exercise builds on the example from the video where `tcpdump -i any -n icmp` is used to filter ICMP traffic, and `tcpdump -D` lists available interfaces.

### Validation

You'll know you've succeeded when:
- You can see both ICMP echo request and echo reply packets in the output
- The packet count shows pairs of requests and replies (indicating successful connectivity)
- You understand the difference between request and reply packet types

### Hints

<details>
<summary>Click to reveal hints</summary>

- Remember to use `sudo` when running tcpdump to avoid permission errors
- The `-n` flag prevents hostname resolution, making output cleaner
- The `-c` flag limits the number of packets captured
- Look for "echo request" and "echo reply" in the packet descriptions

</details>

---

## Exercise 2: Analyze HTTP Traffic to Diagnose Slow Website

**Estimated Time**: 12 minutes  
**Difficulty**: Beginner  
**Concepts**: Port filtering, ASCII packet content, HTTP analysis

### Objective

You will capture HTTP traffic and inspect the actual content of HTTP requests and responses to understand how web communication works and identify potential performance issues.

### Context

Users are complaining that accessing http://example.com is slow. You need to capture the HTTP traffic to see if the request is being sent properly and how long it takes to receive a response. By viewing the actual HTTP headers, you can identify issues like redirects, error codes, or missing resources.

### Tasks

1. Start capturing traffic on port 80 (HTTP) with ASCII output enabled to view packet content
2. In another terminal, use `curl http://example.com` to make an HTTP request
3. Observe the captured packets and identify the HTTP GET request headers
4. Find the HTTP response status code (200, 404, etc.) in the captured traffic
5. Stop the capture and analyze the request/response pattern

### Reference

This exercise builds on the video example where `tcpdump -A port 80` is used to view ASCII content of HTTP packets on port 80.

### Validation

You'll know you've succeeded when:
- You can see the HTTP GET request with headers like "Host:", "User-Agent:", etc.
- You can identify the HTTP response status code (e.g., "HTTP/1.1 200 OK")
- You understand the basic structure of HTTP communication

### Hints

<details>
<summary>Click to reveal hints</summary>

- The `-A` flag displays packet content in ASCII format
- HTTP headers are human-readable text
- The first line of an HTTP request shows the method (GET, POST, etc.) and path
- The first line of an HTTP response shows the status code (200, 404, 500, etc.)
- You may need to scroll through output to find the relevant packets

</details>

---

## Exercise 3: Investigate Suspicious Network Activity

**Estimated Time**: 15 minutes  
**Difficulty**: Intermediate  
**Concepts**: Host filtering, saving captures, security monitoring

### Context

Your security monitoring system has flagged unusual traffic to an external IP address (1.1.1.1) from your server. You need to capture and save this traffic for later analysis to determine if it's legitimate application traffic or a potential security incident.

### Objective

You will use host-based filtering to isolate traffic to a specific IP address, save the capture to a file, and perform basic analysis to understand the nature of the communication.

### Tasks

1. Navigate to the `exercises/03_suspicious_activity/` directory
2. Start capturing all traffic to and from host 1.1.1.1, saving it to a file named `suspicious_traffic.pcap`
3. In another terminal, generate some test traffic by pinging 1.1.1.1 (5 packets) and using `curl` to access http://1.1.1.1
4. Stop the capture after 30 seconds
5. Read the saved capture file and count how many packets were captured
6. Analyze the output to identify what protocols were used (ICMP, HTTP, etc.)

### Reference

This exercise combines the host filtering example (`tcpdump host 8.8.8.8`) and the file saving example (`tcpdump -w pakiety.pcap`) from the video.

### Validation

You'll know you've succeeded when:
- You have a `.pcap` file containing the captured traffic
- You can read the file using `tcpdump -r` and see the packets you generated
- You can identify both ICMP and TCP packets in the capture
- You understand how to save traffic for offline analysis

### Hints

<details>
<summary>Click to reveal hints</summary>

- Use the `-w` flag to write packets to a file
- Use the `-r` flag to read packets from a file
- The `host` filter captures both incoming and outgoing traffic for that IP
- You can use `Ctrl+C` to stop the capture
- Count packets by looking at the summary tcpdump displays when you stop the capture

</details>

---

## Exercise 4: Debug Application Communication Issues

**Estimated Time**: 15 minutes  
**Difficulty**: Intermediate  
**Concepts**: Port filtering, multiple captures, application debugging

### Context

Your web application is failing to connect to a database server that should be listening on port 3306 (MySQL). The application logs show "connection refused" errors. You need to capture traffic on port 3306 to determine if connection attempts are being made and whether the database is responding.

### Objective

You will capture traffic on a specific port to diagnose application connectivity issues, save the capture for documentation, and analyze whether the problem is with the client (application) or server (database).

### Tasks

1. Navigate to the `exercises/04_app_debugging/` directory
2. Start capturing traffic on port 3306, saving to `db_traffic.pcap`
3. In another terminal, attempt to connect to localhost:3306 using the provided test script: `bash simulate_db_connection.sh`
4. Let the capture run for 20 seconds to capture multiple connection attempts
5. Stop the capture and read the saved file
6. Analyze the output to determine if SYN packets (connection attempts) are being sent
7. Check if you see any RST (reset) or SYN-ACK packets that indicate the server's response

### Reference

This exercise extends the port filtering concept (`tcpdump port 80`) and file saving workflow (`tcpdump -w` and `tcpdump -r`) shown in the video, applying them to a real debugging scenario.

### Validation

You'll know you've succeeded when:
- You can identify TCP SYN packets indicating connection attempts
- You can determine whether the server is responding (SYN-ACK) or refusing (RST)
- You understand how tcpdump helps diagnose application-level connectivity issues
- You have documented evidence of the connection attempts in a pcap file

### Hints

<details>
<summary>Click to reveal hints</summary>

- TCP connection establishment uses a three-way handshake: SYN, SYN-ACK, ACK
- Look for "Flags [S]" for SYN packets (connection attempts)
- Look for "Flags [R]" for RST packets (connection refused)
- The port filter captures traffic on both source and destination ports
- If you see only SYN packets with no response, the server may not be running

</details>

---

## Exercise 5: Create Network Traffic Report for Security Audit

**Estimated Time**: 20 minutes  
**Difficulty**: Advanced  
**Concepts**: Multiple filters, capture analysis, reporting, synthesis

### Context

Your organization is undergoing a security audit, and you've been asked to document all network traffic from your server over a 5-minute period. The auditors specifically want to know about HTTP traffic (port 80), HTTPS traffic (port 443), DNS queries (port 53), and any ICMP traffic. You need to capture each type separately and provide a summary report.

### Objective

You will perform multiple targeted captures using different filters, save each to separate files, analyze the results, and create a summary report documenting the network activity patterns.

### Tasks

1. Navigate to the `exercises/05_security_audit/` directory
2. Run the provided traffic simulation script in the background: `bash generate_traffic.sh &`
3. Capture the following traffic types simultaneously (use multiple terminals or background processes):
   - HTTP traffic (port 80) → save to `http_traffic.pcap`
   - HTTPS traffic (port 443) → save to `https_traffic.pcap`
   - DNS traffic (port 53) → save to `dns_traffic.pcap`
   - ICMP traffic → save to `icmp_traffic.pcap`
4. Let all captures run for 60 seconds, then stop them
5. Read each capture file and count the number of packets in each category
6. Create a summary report file `traffic_report.txt` with the following information:
   - Total packets captured per protocol
   - Most active protocol (highest packet count)
   - Any unusual patterns or observations
   - Recommendations for security team

### Reference

This exercise synthesizes multiple concepts from the video: port filtering (`port 80`), protocol filtering (`icmp`), and the save/read workflow (`-w` and `-r` flags).

### Validation

You'll know you've succeeded when:
- You have four separate `.pcap` files, one for each traffic type
- You can read each file and see relevant packets
- Your report accurately reflects the packet counts from each capture
- You understand how to use tcpdump for comprehensive network monitoring
- You can explain why separating traffic types is useful for analysis

### Hints

<details>
<summary>Click to reveal hints</summary>

- You can run tcpdump in the background by adding `&` at the end of the command
- Use `jobs` to see background processes and `fg` to bring them to foreground
- To stop a background tcpdump, use `sudo pkill tcpdump` or bring it to foreground with `fg` and press Ctrl+C
- You can combine filters with `or`: `tcpdump 'port 80 or port 443'` (but for this exercise, keep them separate)
- Use `wc -l` to count lines if you redirect tcpdump output to a text file
- The packet count is shown when tcpdump exits

</details>

---

## Cleanup

After completing all exercises, you can clean up the created files:

```bash
bash cleanup_tcpdump_exercises.sh
```

**Warning**: This will delete all files in the `exercises/` directory. Make sure to save any work you want to keep!

---

## Notes

- All exercises are independent and can be completed in any order
- Refer back to the source material if you get stuck
- Try to solve exercises without looking at hints first
- The goal is to understand *when* and *why* to use these techniques, not just *how*
- Remember that tcpdump requires root privileges (use `sudo`)
- Practice on a test system or VM to avoid capturing sensitive production traffic

---

## Common Troubleshooting Tips

Based on the video, here are common mistakes to avoid:

1. **Permission Denied Error**: Always use `sudo` when running tcpdump
2. **No Packets Captured**: Check that you're using the correct interface with `-i`
3. **Too Many Packets**: Use `-c` to limit packet count or apply more specific filters
4. **Can't Read Saved File**: Make sure you're using `-r` (read) not `-w` (write)
5. **Filter Not Working**: Check filter syntax - protocol names don't need quotes, but complex expressions do
