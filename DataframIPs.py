import pandas as pd
import ipaddress
from itertools import chain


def getExcelData(ExcelFile):
    ips={}
    dataf = pd.read_excel(ExcelFile)
    for value in dataf["Dst"]:
        
        
        if(isinstance(value,str)):
            ipaddr=[]
            for ip in ipaddress.ip_network(value):
                ipaddr.append(str(ip))
                print(ip)
            ips[value]=ipaddr

    #print(ips)       
    dataf["IPs"] = dataf["Dst"].map(ips)
		#df = pd.DataFrame({
    		#'A' : df['A'].values.repeat(lens),
    		#'C' : list(chain.from_iterable(s.values.tolist()))
		#	})
    dataf.to_excel("temp.xlsx")
		
def getIPs(ipSubnet):
	ipAdds=ipaddress.ip_network(ipSubnet)
	for ip in ipAdds:
		print(ip)


		
def getIPFromSubnetAndTransform(ExcelFile):
    ips={}
    dataf = pd.read_excel(ExcelFile)
    for value in dataf["Dst"]:
        
        
        if(isinstance(value,str)):
            ipaddr=[]
            for ip in ipaddress.ip_network(value):
                ipaddr.append(str(ip))
                print(ip)
            ips[value]=ipaddr

    df1 = pd.DataFrame([(k, y) for k, v in ips.items() for y in v], columns=['Dst','IPs'])
    #print(ips)  
    dataf = dataf.merge(df1, on='Dst', how='left')     
    
		#df = pd.DataFrame({
    		#'A' : df['A'].values.repeat(lens),
    		#'C' : list(chain.from_iterable(s.values.tolist()))
		#	})
    dataf.to_excel("temp.xlsx")
