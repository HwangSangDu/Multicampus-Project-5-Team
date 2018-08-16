## 영화 목록
# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e\&openStartDt\=2014\&openEndDt\=2014\&itemPerPage\=99999 &> 201411.json

# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e\&openStartDt\=2015\&openEndDt\=2015\&itemPerPage\=99999 &> 201511.json

# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e\&openStartDt\=2016\&openEndDt\=2016\&itemPerPage\=99999 &> 201611.json

# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e\&openStartDt\=2017\&openEndDt\=2017\&itemPerPage\=99999 &> 201711.json

# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e\&openStartDt\=2018\&openEndDt\=2018\&itemPerPage\=99999 &> 201811.json




## 영화인 목록
echo "영화인 목록"
# curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key=430156241533f1d058c603178cc3ca0e\&itemPerPage=9999999 &> 영화인목록.json
## 영화인 상세 정보
echo "영화인 상세 정보"
curl -X GET http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json?key=430156241533f1d058c603178cc3ca0e &> 영화인상세정보.json

## 영화사 목록
echo "영화사 목록"
curl -X GET http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key=430156241533f1d058c603178cc3ca0e\&itemPerPage=99999999 &> 영화사목록.json

## 영화사 상세정보
echo "영화사 상세정보"
curl -X GET http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json?key=430156241533f1d058c603178cc3ca0e &> 영화사상세정보.json

# 20188621