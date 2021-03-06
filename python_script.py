# importing libraries 
import os 

arch = (os.uname())[4]

#installing dependencies
os.system('yum install docker curl -y')
if arch == 'x86_64' or arch == 'amd64':
    os.system('curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-latest.x86_64.rpm')
    os.system('rpm -ivh minikube-latest.x86_64.rpm')
elif arch == 'arm64' or arch == 'aarch64':
    os.system( 'curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-latest.aarch64.rpm')
    os.system('rpm -ivh minikube-latest.aarch64.rpm')





