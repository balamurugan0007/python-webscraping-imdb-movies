

from bs4 import BeautifulSoup

import requests

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://www.googleapis.com/auth/spreadsheets' ,'https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('crud.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = client.open("webscraping").worksheet("logs")




try:
   
    response=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup=BeautifulSoup(response.text,"html.parser")
   
    print(soup)
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    print(movies)

    for movie in movies:
        
        #print(movie)
        
        movie_name=movie.find("td",class_="titleColumn").a.text
  
        ratings=movie.find("td",class_="ratingColumn").strong.text
      
        year=movie.find("td",class_="titleColumn").span.text.replace("(","").replace(")","")
  
        rank=movie.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
        imges=movie.find("td",class_="posterColumn").a.img['src']
        print(imges)
        
        print("Name:"+ movie_name,"Ratings:"+ ratings ,"Year:"+year,"Rank:"+rank)

        col=sheet.col_values(movie_name(1))
        print(col)
        break


    tamil=requests.get("https://www.imdb.com/india/top-rated-tamil-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=57b6cfe5-784a-4764-bb68-72ed85c2961e&pf_rd_r=6G42EJ9AZE538KKP1P6Q&pf_rd_s=center-2&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_ta_hd")
    tamil_soup=BeautifulSoup(tamil.text,"html.parser")
    tamil_movie=tamil_soup.find('tbody',class_="lister-list").find_all('tr')
    #print(tamil_movie)
   



   

    for tamil in tamil_movie:
        
        #print(movie)
        
        movie_name=tamil.find("td",class_="titleColumn").a.text
  
        ratings=tamil.find("td",class_="ratingColumn").strong.text
      
        year=tamil.find("td",class_="titleColumn").span.text.replace("(","").replace(")","")
  
        rank=tamil.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
        imges=tamil.find("td",class_="posterColumn").a.img['src']
        print(imges)
        print("Name:"+ movie_name,"Ratings:"+ ratings ,"Year:"+year,"Rank:"+rank)
        break



    #TV movies
    tv=requests.get("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv")
    tv_soup=BeautifulSoup(tv.text,"html.parser")
    tv_movie=tv_soup.find('tbody',class_="lister-list").find_all('tr')
    print(tv_movie)

    for tv_ in tv_movie:
        
        #print(movie)
        
        movie_name=tv_.find("td",class_="titleColumn").a.text
  
        ratings=tv_.find("td",class_="ratingColumn").strong.text
      
        year=tv_.find("td",class_="titleColumn").span.text.replace("(","").replace(")","")
  
        rank=tv_.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
        imges=tv_.find("td",class_="posterColumn").a.img['src']
        print(imges)
        print("Name:"+ movie_name,"Ratings:"+ ratings ,"Year:"+year,"Rank:"+rank)
        break




   #most popular
    pop=requests.get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
    pop_s=BeautifulSoup(pop.text,"html.parser")
    pop_movie=pop_s.find('tbody',class_="lister-list").find_all('tr')
    print(pop_movie)
   

    for poplar in pop_movie:
        
        #print(movie)
        
        movie_name=poplar.find("td",class_="titleColumn").a.text
  
        ratings=poplar.find("td",class_="ratingColumn").strong.text
      
        year=poplar.find("td",class_="titleColumn").span.text.replace("(","").replace(")","")
  
        rank=poplar.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
        imges=poplar.find("td",class_="posterColumn").a.img['src']
        print(imges)
        print("Name:"+ movie_name,"Ratings:"+ ratings ,"Year:"+year,"Rank:"+rank)
        break


    
except Exception as e:
    print(e)