import requests
from bs4 import BeautifulSoup
import csv
import json


url = "https://vehicle.bihr.net/api/v1/public/criteria/types"

querystring = {"companyId":"1"}

headers = {
    'internal': "MTIyLjE3Ny4xNTQuMjA3",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'sec-ch-ua-mobile': "?0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'cache-control': "no-cache",
    'postman-token': "a103ae9a-6878-0f91-2e16-e8e912d7aa34"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

companies = json.loads(response.text)

for company in companies:
    company_name = company['name']
    company_id = company['id']

    if company_id == 2:


        print (company_name)

        url_1 = "https://vehicle.bihr.net/api/v1/public/criteria/manufacturers"

        querystring = {"typeId": str(company_id)}

        headers = {
            'internal': "MTIyLjE3Ny4xNTQuMjA3",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'sec-ch-ua-mobile': "?0",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'cache-control': "no-cache",
            'postman-token': "51b28194-058c-ff5d-0345-f0ac072c3ae9"
        }

        response1 = requests.request("GET", url_1, headers=headers, params=querystring)

        manufacturers = json.loads(response1.text)

        for manufacturer in manufacturers:
            manufacturer_name = manufacturer['name']
            manufacturer_id = manufacturer['id']

            done = ['BETA','HONDA','KAWASAKI','KYMCO','MBK','PEUGEOT','PIAGGIO','SUZUKI','SYM','YAMAHA','APRILIA','BENELLI','CAGIVA',
                    'CPI','DAELIM','DERBI','GILERA','HYOSUNG','ITALJET','KEEWAY','MALAGUTI','PGO','RIEJU','TGB','VESPA']

            if manufacturer_name not in done:

                print (manufacturer_name)

                url_2 = "https://vehicle.bihr.net/api/v1/public/criteria/manufacturer/years"

                querystring = {"typeId": str(company_id), "manufacturerId": str(manufacturer_id)}

                headers = {
                    'internal': "MTIyLjE3Ny4xNTQuMjA3",
                    'accept': "application/json, text/javascript, */*; q=0.01",
                    'sec-ch-ua-mobile': "?0",
                    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
                    'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
                    'sec-fetch-site': "cross-site",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-dest': "empty",
                    'cache-control': "no-cache",
                    'postman-token': "351922d8-8b50-dab2-77ae-c87ce7aec8e2"
                }

                response_2 = requests.request("GET", url_2, headers=headers, params=querystring)

                years = json.loads(response_2.text)

                for year in years:

                    print (year)
                    url_3 = "https://vehicle.bihr.net/api/v1/public/criteria/manufacturer/year/versions"

                    querystring = {"typeId": str(company_id), "manufacturerId": str(manufacturer_id), "year": str(year)}

                    headers = {
                        'internal': "MTIyLjE3Ny4xNTQuMjA3",
                        'accept': "application/json, text/javascript, */*; q=0.01",
                        'sec-ch-ua-mobile': "?0",
                        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
                        'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
                        'sec-fetch-site': "cross-site",
                        'sec-fetch-mode': "cors",
                        'sec-fetch-dest': "empty",
                        'cache-control': "no-cache",
                        'postman-token': "627e8d83-91e7-93f7-6e1d-495398e7e0b5"
                    }

                    response_3 = requests.request("GET", url_3, headers=headers, params=querystring)



                    versions = json.loads(response_3.text)


                    for version in versions:
                        models = version['versions']
                        for model in models:
                            vehicle_id = model['vehicleId']

                            url_final = "https://www.bihr.eu/fr/nl/product/search"

                            querystring = {"page": "1", "sort": "0", "vehicle": str(vehicle_id)}

                            headers = {
                                'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
                                'sec-ch-ua-mobile': "?0",
                                'upgrade-insecure-requests': "1",
                                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
                                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                'sec-fetch-site': "same-origin",
                                'sec-fetch-mode': "navigate",
                                'sec-fetch-dest': "document",
                                'cache-control': "no-cache",
                                'postman-token': "e0648f7b-dc3e-1cc8-57d8-400d257ed891"
                            }

                            responsefinal = requests.request("GET", url_final, headers=headers, params=querystring)

                            html = BeautifulSoup(responsefinal.content, 'html.parser')

                            try:
                                model = html.find('p', {'class': 'model'})

                                model_name = model.text.strip()

                                print (model_name)

                                arr = []
                                temp = []
                                temp.append(company_name)
                                temp.append(manufacturer_name)
                                temp.append(year)
                                temp.append(model_name)

                                arr.append(temp)

                                with open('sydney2.csv', 'a+') as csvfile:
                                    csvwriter = csv.writer(csvfile)
                                    csvwriter.writerows(arr)

                            except:
                                print ("Error")






