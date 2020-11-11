# Maclookup

Clone the repository by running 
```
git clone https://github.com/surajtk7/maclookup.git
```
Move into the directory 
```
cd maclookup
```
Docker is used to build the application and run it correspondingly. The application is written in Python.  


Build the container 
```
docker build -t maclookup .
```
Run with -h for help
```
docker run maclookup -h
```
# Example :

 For obtaining the company name to which the MAC address belongs, Run the following command where **"-a"** refers to the **"API Key"** and **"-m"** refers to the **"MAC address"**.  (**Dummy API Key is used here**)
```
docker run maclookup -a=at_PElKcjAqk1mdWnBA6Lwi48PDYizlP -m=44:38:39:ff:ef:57
```
