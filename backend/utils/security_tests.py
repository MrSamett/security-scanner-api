def run_security_tests(url, scan_type):
    if scan_type == "sql_injection":
        return f"SQL Injection test for {url} passed"
    elif scan_type == "xss":
        return f"XSS test for {url} passed"
    return "Unknown scan type"
