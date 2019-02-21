# 빅데이터를 활용한 영화 흥행 예측

```
기존 영화 예측 모델에 새로운 변수를 추가
```

## 기존 변수

```
배우, 감독, 장르, 배급사, 평점, 국적, 관람등급, 배우, 흥행요인 등등 

```

## 새로운 변수

```
영화 포스터 [인물 수, 색감 등]
개봉 후 날씨 및 기온
연휴 수
개봉 전 후 일주일 간의 경쟁작
```

## 모델링

```
1. Random forest

2. Random forest CV [과적합 방지]

3. Boosting CV

4. XGBoost CV
```

## 모델 적용 결과

![](http://cfile7.uf.tistory.com/image/99C93C495C6EBB010D9AA8)

![](http://cfile5.uf.tistory.com/image/992ABA3E5C6EBB1D16935E)

# 사용 Tool

-   데이터 크롤링 \[Selenium\] \[[github link](https://github.com/SeleniumHQ/selenium)\]
    
    ```
    pip install selenium
    ```
    
-   R Script

### 참조 링크

-   [TED](https://www.ted.com/talks/stacy_smith_the_data_behind_hollywood_s_sexism/transcript?language=ko)
    
-   [영화 흥행성 요인 \[학술 논문 검색\]](http://www.riss.kr/search/Search.do?queryText=znSubject,%ED%9D%A5%ED%96%89%EC%98%81%ED%99%94&searchGubun=true&colName=bib_t&detailSearch=true#redirect)
    
-   [멀티캠퍼스 2017년 프로젝트](https://m.blog.naver.com/PostView.nhn?blogId=mcgyber1&logNo=221093798669&rvid=9002B7F9B72BD1879F6357AA820458275CD7&proxyReferer=https%3A%2F%2Fm.search.naver.com%2Fsearch.naver%3Fquery%3D%25EA%25B2%25BD%25EA%25B8%25B0%2B%25EB%25B9%2585%25EB%258D%25B0%25EC%259D%25B4%25ED%2584%25B0%2B%25EC%258B%259C%25EC%2583%2581%26sm%3Dmtb_hty.top%26where%3Dm_video%26oquery%3D%25EA%25B2%25BD%25EA%25B8%25B0%2B%25EB%25B9%2585%25EB%258D%25B0%25EC%259D%25B4%25ED%2584%25B0%26tqi%3DT0khgspVuplssucdGECssssstdd-432281)
    

### 영화 진흥 위원회

1.  [영화진흥위원회](http://www.kofic.or.kr/kofic/business/main/main.do)
    
2.  [영화 DB 검색](http://www.kofic.or.kr/kofic/business/infm/introData.do)
    
3.  [영화 연도별 월별 공식 통계](http://www.kobis.or.kr/kobis/business/stat/offc/searchOfficHitTotList.do?searchMode=year)
    
4.  [박스오피스 월간 순위](http://www.kobis.or.kr/kobis/business/stat/boxs/onlinefindMonthlyBoxOfficeList.do?loadEnd=0&searchType=search&sSearchYearFrom=2018&sSearchMonthFrom=4&sMultiMovieYn=)
    
5.  [IPTV, VOD 순위 \[월별\]](http://www.kofic.or.kr/kofic/business/board/selectBoardList.do?boardNumber=2)
    

### 참조 기사

-   [인공지능, 몰랐던 ‘영화 속 배역 성차별’도 콕 찍어낸다 : IT : 경제 : 뉴스 : 한겨레](http://www.hani.co.kr/arti/economy/it/787272.html)
    
-   [배우 지나 데이비스, 할리우드 성차별 'GD 지수' 공개](http://www.koreaherald.com/view.php?ud=20160925000039&kr=1)
