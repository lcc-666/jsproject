#化妆品信息许可
import json
import requests


if __name__ == '__main__':
    id_list = []
    all_data_list = []
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do'
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    params={
        'method': 'getXkzsList'
    }

    for page in range(1,6):
        page=str(page)
        data={'on': 'true',
              'page': page,
              'pageSize': '15',
              'productName': '',
              'conditionType': '1',
              'applyname': '',
              'applysn': ''}
        dict_data=requests.post(url=url,data=data,params=params,headers=headers).json()
        for dic in dict_data['list']:
            id_list.append(dic['ID'])
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do'
    params = {
        'method': 'getXkzsById'
    }
    for id in id_list:
        data={
            'id':id
        }
        detail_json=requests.post(url=url,params=params,data=data,headers=headers).json()
        all_data_list.append(detail_json)
    fp=open('./hz.json','w')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')
