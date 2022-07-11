import requests         # import librares
from pyfiglet import Figlet
import folium
from colorama import Fore
from colorama import init
init()


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()      # information about ip adres
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }       # need's information
        
        for k, v in data.items():
            print(Fore.GREEN + f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')   #        create html file 
        
    except requests.exceptions.ConnectionError:
        print(Fore.GREEN + '[!] Please check your connection!')     # except erorr
        
        
def main():
    preview_text = Figlet(font='slant')
    print(Fore.GREEN + preview_text.renderText('IP INFO'))
    ip = input(Fore.GREEN + 'Please enter a target IP: ')       # ip quetion
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()

input('Type "Enter" to end')
