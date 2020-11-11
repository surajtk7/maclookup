import requests 
import argparse
import json 


  
print("MAC Lookup") 
 
# Function to get the apiKey and MAC address 
def get_args(): 
    
    parser = argparse.ArgumentParser() 
      
    # We need the apiKey and the MAC address
    parser.add_argument("-m", "--macaddress", 
                        dest="mac_address", 
                        help="MAC Address of the device. "
                        )

    parser.add_argument("-a", "--apiKey", 
                        dest="apiKey", 
                        help="API key to be used"
                        )                    
                                            
    values = parser.parse_args() 
      
    # Check if address and apiKey were entered 
    if values.mac_address and values.apiKey: 
        return values 
    else: 
        parser.error("Invalid Syntax. "
                     "Use --help for more details.")  
                     
  
  
def get_vendor_details(mac_address,apiKey): 
      
   
    url = "https://api.macaddress.io/v1"
    output="json"
       
    # API to get the vendor details 
    API= url+"?"+"apiKey="+apiKey+"&"+"output="+output+"&"+"search="+mac_address
    
    # Fetching the vendor details using GET method
    response = requests.get(API) 
    if response.status_code != 200: 
        raise Exception("Invalid MAC Address!") 
    return response.text
  
# Main 
if __name__ == "__main__": 
    
    values = get_args()
    mac_address=values.mac_address
    apiKey=values.apiKey 

    print("Fetching Details...") 
   
    try: 
        #Converting the response to dictionary for parsing
        vendor_name =json.loads(get_vendor_details(mac_address,apiKey))
        print("Device vendor with MAC address: "+mac_address+" is "+vendor_name["vendorDetails"]["companyName"])    
     
    except:  
        
         # If something goes wrong 
        print("An error occurred. Check "
              "your Internet connection.") 