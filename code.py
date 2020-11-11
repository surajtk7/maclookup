import requests 
import argparse
import json 


  
print("MAC Lookup") 
 
# Function to get the apiKey and MAC address 
def get_args(): 
    
    parser = argparse.ArgumentParser() 
      
    # Get apiKey and the MAC address from the command line
    parser.add_argument("-m", "--macaddress", 
                        dest="mac_address", 
                        help="MAC Address of the device. "
                        )

    parser.add_argument("-a", "--apiKey", 
                        dest="apiKey", 
                        help="API key to be used"
                        )                    
                                            
    inputs = parser.parse_args() 
      
    # Check if address and apiKey were entered 
    if inputs.mac_address and inputs.apiKey: 
        return inputs 
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
        raise Exception("Invalid MAC Address or API Key") 
    return response.text
  
# Main 
if __name__ == "__main__": 
    
    inputs = get_args()
    mac_address=inputs.mac_address
    apiKey=inputs.apiKey 

    print("Fetching Details...") 
   
    try: 
        #Converting the response to dictionary for parsing
        vendor_name =json.loads(get_vendor_details(mac_address,apiKey))
        print("Device vendor with MAC address: "+mac_address+" is "+vendor_name["vendorDetails"]["companyName"])    
     
    except:  
        
         # If something goes wrong 
        print("An error occurred") 