import subprocess
import datetime

def chcek_ip(ip_address):
    cmd=["ping","-c","1",ip_address]
    result=subprocess.run(cmd,text=True,capture_output=True)
    time=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    if result.returncode==0:
        return True
    else:
        return False

if __name__=="__main__":
 server_up=0
 server_down=0
 print("getting data ...")
 try:
    with open("server.txt","r") as file:
       print("opened succesfully")
       for ip in file:
          ip=ip.strip()
          

          if not ip:
           continue
          print("pinging ip")
          is_up=chcek_ip(ip)
          if is_up==True:
             log_messgae=f"the server {ip}is up..."
             server_up=server_up+1
          else:
             log_messgae=f"the server{ip} is down..."
             server_down=server_down+1
          print(log_messgae.strip())

          with open("up_timeaudit.log","a") as Nile:
             Nile.write(log_messgae)
 except FileNotFoundError:
   print("the file doesnt exits")
print("getting data ....")
print(f"the number of server up is {server_up}")
print(f"the number of server down is {server_down}")
print("over and out")