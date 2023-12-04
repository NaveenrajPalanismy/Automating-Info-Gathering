import nmap
import sys

nm_scan=nmap.PortScanner()
nm_scanner=nm_scan.scan("http://172.16.99.200/",'80',arguments='-O')