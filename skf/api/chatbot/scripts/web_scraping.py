import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build
from skf import settings

def replace_all(text):
    rep={"<b>":"",'\n':"","</b>":"","<br>":"","&nbsp;...":"."}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return text


def remove_duplicates(string):
    final_list=[]
    for q in string:
        if q not in final_list:
            final_list.append(q)
    return final_list 


def web_scraper(entity):
    search = "\"Security\" "+entity
    results=google_search(search,settings.API_KEY, settings.CSE_ID)
    for i in range(0,len(results)):
        query_string = urllib.parse.urlencode({"search_query" : search})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        final_search=remove_duplicates(search_results)
        youtube_links="http://www.youtube.com/watch?v="+final_search[0]+"and"+final_search[1]

        if 'owasp' in results['items'][i]['link']:    
            Title="Title "+ results['items'][i]['title'] + " Link "+ results['items'][i]['link']
            snippet=results['items'][0]['snippet'].replace('\n',"")
            html_snippet=replace_all(results['items'][0]['htmlSnippet'])
            Description=snippet+html_snippet
            return Title +"\n"+ Description +"\n"+ "Youtube Links: "+ youtube_links

        if 'wikipedia' in results['items'][i]['link']: 
            Title="Title "+ results['items'][i]['title'] + "Link "+ results['items'][i]['link']
            snippet=results['items'][0]['snippet'].replace('\n',"")
            html_snippet=replace_all(results['items'][0]['htmlSnippet'])
            Description=snippet+html_snippet
            return Title +"\n"+ Description +"\n"+ "Youtube Links: "+ youtube_links

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

#print(web_scraper('"Security" what are injections?'))
