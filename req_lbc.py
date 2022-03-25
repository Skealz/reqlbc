import urllib.request
import urllib.parse
import json
import gzip

url = "https://dd.leboncoin.fr/js"
hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': '*/*',
        'Host': 'dd.leboncoin.fr',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.leboncoin.fr/',

        'Content-Type': 'application/x-www-form-urlencoded',

        'Origin': 'https://www.leboncoin.fr',

        'Dnt': '1',

        'Sec-Fetch-Dest': 'empty',

        'Sec-Fetch-Mode': 'cors',

        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        'Sec-Gpc': '1'
        }


data_enc = b"""jsData=%7B%22plg%22%3A0%2C%22plgod%22%3Afalse%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22br_h%22%3A440%2C%22br_w%22%3A1920%2C%22br_oh%22%3A1028%2C%22br_ow%22%3A1920%2C%22jsf%22%3Afalse%2C%22cvs%22%3Atrue%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22sln%22%3Anull%2C%22lo%22%3Afalse%2C%22lb%22%3Afalse%2C%22mp_cx%22%3A465%2C%22mp_cy%22%3A133%2C%22mp_mx%22%3A0%2C%22mp_my%22%3A0%2C%22mp_sx%22%3A465%2C%22mp_sy%22%3A299%2C%22mp_tr%22%3Atrue%2C%22mm_md%22%3A76%2C%22hc%22%3A4%2C%22rs_h%22%3A1080%2C%22rs_w%22%3A1920%2C%22rs_cd%22%3A24%2C%22ua%22%3A%22Mozilla%2F5.0%20(X11%3B%20Linux%20x86_64%3B%20rv%3A91.0)%20Gecko%2F20100101%20Firefox%2F91.0%22%2C%22lg%22%3A%22en-US%22%2C%22pr%22%3A1%2C%22ars_h%22%3A1080%2C%22ars_w%22%3A1920%2C%22tz%22%3A-60%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22abk%22%3Anull%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wo%22%3Anull%2C%22sz%22%3Anull%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdif%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdw%22%3Atrue%2C%22prm%22%3Atrue%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22usb%22%3A%22NA%22%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22eva%22%3A37%2C%22med%22%3A%22defined%22%2C%22ocpt%22%3Afalse%2C%22aco%22%3A%22probably%22%2C%22acmp%22%3A%22maybe%22%2C%22acw%22%3A%22probably%22%2C%22acma%22%3A%22maybe%22%2C%22acaa%22%3A%22maybe%22%2C%22ac3%22%3A%22%22%2C%22acf%22%3A%22maybe%22%2C%22acmp4%22%3A%22maybe%22%2C%22acmp3%22%3A%22maybe%22%2C%22acwm%22%3A%22maybe%22%2C%22acots%22%3Afalse%2C%22acmpts%22%3Afalse%2C%22acwts%22%3Afalse%2C%22acmats%22%3Afalse%2C%22acaats%22%3Afalse%2C%22ac3ts%22%3Afalse%2C%22acfts%22%3Afalse%2C%22acmp4ts%22%3Atrue%2C%22acmp3ts%22%3Afalse%2C%22acwmts%22%3Atrue%2C%22vco%22%3A%22probably%22%2C%22vch%22%3A%22probably%22%2C%22vcw%22%3A%22probably%22%2C%22vc3%22%3A%22%22%2C%22vcmp%22%3A%22%22%2C%22vcq%22%3A%22maybe%22%2C%22vc1%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vchts%22%3Atrue%2C%22vcwts%22%3Atrue%2C%22vc3ts%22%3Afalse%2C%22vcmpts%22%3Afalse%2C%22vcqts%22%3Afalse%2C%22vc1ts%22%3Afalse%2C%22glrd%22%3A%22llvmpipe%22%2C%22glvd%22%3A%22Mesa%2FX.org%22%2C%22cfpp%22%3Anull%2C%22cfcpw%22%3Anull%2C%22cffpw%22%3Anull%2C%22cffrb%22%3Anull%2C%22cfpfe%22%3Anull%2C%22cfse%22%3Anull%2C%22stcfp%22%3Anull%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Atrue%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22xr%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22svde%22%3Afalse%2C%22slat%22%3Anull%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22ttst%22%3A499%2C%22ewsi%22%3Anull%2C%22wwsi%22%3Anull%2C%22slmk%22%3Anull%2C%22dbov%22%3Afalse%2C%22ifov%22%3Afalse%2C%22hcovdr%22%3Afalse%2C%22plovdr%22%3Afalse%2C%22ftsovdr%22%3Afalse%2C%22hcovdr2%22%3Afalse%2C%22plovdr2%22%3Afalse%2C%22ftsovdr2%22%3Afalse%2C%22cokys%22%3Anull%2C%22tagpu%22%3A75%2C%22tbce%22%3Anull%2C%22ecpc%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22nddc%22%3A1%2C%22nclad%22%3Anull%2C%22haent%22%3Anull%2C%22psn%22%3Afalse%2C%22edp%22%3Afalse%2C%22addt%22%3Afalse%2C%22wsdc%22%3Afalse%2C%22ccsr%22%3Atrue%2C%22nuad%22%3Afalse%2C%22npmtm%22%3A%22NA%22%2C%22ucdv%22%3Afalse%7D&events=%5B%5D&eventCounters=%5B%5D&jsType=ch&cid=0For~X_FsTuI4YM_Cf78FPzo.P.VLx9C3jAoXAnSWrydSGPXQv.I6EyLqwkCBA~G75Wk3tfAa0cGVFMq5WscJu5HTwGWKzVgQspTGdpLwVI5DKDCnmVMtXrkF6iZme2&ddk=05B30BD9055986BD2EE8F5A199D973&Referer=https%253A%252F%252Fwww.leboncoin.fr%252F&request=%252F&responsePage=origin&ddv=4.2.10"""

req = urllib.request.Request(url, headers=hdr, data=data_enc)
response = urllib.request.urlopen(req)

resp = response.read().decode('utf-8')
print(resp)
d = json.loads(resp)

cookie = d['cookie']
print(cookie)

url = "https://api.leboncoin.fr/finder/search"
hdr = {
       'Host': 'api.leboncoin.fr',

       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',

        'Accept': '*/*',

        'Accept-Language': 'en-US,en;q=0.5',

         'Accept-Encoding': 'gzip, deflate, br',

         'Referer': 'https://www.leboncoin.fr/',

         'Api_key': 'ba0c2dad52b3ec',

         'Content-Type': 'application/json',

          'Origin': 'https://www.leboncoin.fr',

          'Dnt': '1',

          'Cookie': cookie + '; utag_main=_st:1648151365624$v_id:017fbd5e72ba005272a3c812e4e400044001900900bd0$_sn:1$_ss:1$_pn:1%3Bexp-session$ses_id:1648149557946%3Bexp-session; __Secure-InstanceId=e6f84352-df87-4cc3-8cd5-0f93410a3373;include_in_experiment=false',

          'Sec-Fetch-Dest': 'empty',

          'Sec-Fetch-Mode': 'cors',

          'Sec-Fetch-Site': 'same-site',

          'Sec-Gpc': '1' 
        }

data = b'{"owner_type":"all","limit":35,"limit_alu":3,"sort_by":"relevance","sort_order":"desc","filters":{"enums":{"ad_type":["offer"]},"keywords":{"text":"ya"}},"listing_source":"direct-search","offset":0}'

req = urllib.request.Request(url, headers=hdr, data=data)
response = urllib.request.urlopen(req)

resp = response.read()
resp = gzip.decompress(resp)
#print(resp)
#resp = resp.decode(response.headers.get_content_charset())
print(str(resp))
