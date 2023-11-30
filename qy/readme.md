# RUC Movie
## Installation
- all in RUCMovie_V2
- packages added in `requirements.txt`
- enter powershell then:
```bash
D:\app\anaconda\python.exe -m venv env
.\env\Scripts\activate.bat
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r ./requirements.txt
flask run
```
## changes
- add new table to `movie.db`, with `SQLite_Create.ipynb` in `/jupyter`
- add '豆瓣' to navbar in tempalte `base.html`
- add new route to `/douban` directories

## refer to
- [china GeoJson](https://github.com/yezongyang/china-geojson)
- [https://plotly.com/python/scattermapbox/](https://plotly.com/python/scattermapbox/)

