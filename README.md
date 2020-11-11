# Maclookup

Clone the repository by running 
```
git clone https://github.com/surajtk7/maclookup.git
```
Move into the directory 
```
cd maclookup
```
Docker is used to build the application and run it correspondingly. The application is written in Python as it is versatile, easy to use and fast to develop.  


Build the container 
```
docker build -t maclookup .
```
Run with -h for help
```
docker run maclookup -h
```

# Security :

Security isn't an afterthought. It has to be an integral part of any development project and also for REST APIs. There are multiple ways to secure a RESTful API e.g. basic auth, OAuth etc. but one thing is sure that RESTful APIs should be stateless- so request authentication/authorization should not depend on cookies or sessions. Instead, each API request should come with some sort authentication credentials which must be validated on the server for every request and this case is no different.


# Example :

For obtaining the company name to which the MAC address belongs, Run the following command where **"-a"** refers to the **"API Key"** and **"-m"** refers to the **"MAC address"**.  (**Dummy API Key is used here**)
```
docker run maclookup -a=at_PElKcjAqk1mdWnBA6Lwi48PDYizlP -m=44:38:39:ff:ef:57
```
