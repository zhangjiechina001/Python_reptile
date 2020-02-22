from bs4 import BeautifulSoup
import re
def getInfo():
    file=open('city_code.html','rb')
    html=file.read()
    bs=BeautifulSoup(html,'html.parser')
    provinces=bs.find_all('province')
    citys=bs.find_all('county')
    city_infos={}
    for city in citys:
        attr=city.attrs
        city_infos[attr['name']]=attr['weathercode']
    return city_infos

def get_data():
    file=open('city_code.html','rb')
    html=file.read()
    bs=BeautifulSoup(html,'html.parser')
    #获得所有省的信息
    provinces=bs.find_all('province')
    ret_info={}
    for province in provinces:
        province_name=province.attrs['name']
        province_val={}
        citys=province.find_all('city')
        for city in citys:
            city_name=city.attrs['name']
            city_val={}
            countrys=city.find_all('county')
            for country in countrys:
                country_name=country.attrs['name']
                country_val=country.attrs['weathercode']
                city_val[country_name]=country_val
            province_val[city_name]=city_val

        ret_info[province_name]=province_val
    return ret_info

if __name__=='__main__':
     data=get_data()



