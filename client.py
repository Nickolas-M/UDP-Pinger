from socket import *
from datetime import datetime
import time

def main():

    serverName = '127.0.0.1'
    serverPort = 12001
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1) 
    
    rtt_list = [] # Holds the Round Trip Time of each packet sent
    successful_packets = 0 
    
    
    for x in range(1, 11):
        
        date_time = datetime.now()
        format_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
        message = f"PING {x} {format_date_time}"
        
        packet_time_start = time.perf_counter()

        clientSocket.sendto(message.encode(),(serverName, serverPort))
        
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        
            packet_time_end = time.perf_counter()
            rtt = (packet_time_end - packet_time_start) * 1000
        
            print(modifiedMessage.decode())
            print(f"RTT: {rtt:.2f} ")
            
            rtt_list.append(rtt)
            successful_packets += 1
            
        except timeout:
            print("Request Timed Out")
            
    clientSocket.close()
    
    # Ping Summary
    min_calc = min(rtt_list)
    max_calc = max(rtt_list)
    avg_calc = sum(rtt_list) / len(rtt_list)
    
    percent_lost = (10 - successful_packets) / 10 * 100
    

    print(f"Min RTT: {min_calc:.2f}")
    print(f"Max RTT: {max_calc:.2f}")
    print(f"Ave RTT: {avg_calc:.2f}")
    print(f"Percent Lost: {percent_lost}%")

if __name__ == '__main__': 
    main()