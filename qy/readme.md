# RUC Movie
## Installation
- packages added in `requirements.txt`
- enter powershell then:
```bash
D:\app\anaconda\python.exe -m venv env
.\env\Scripts\activate.bat
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r ./requirements.txt
```
## changes
- add new table to `movie.db`, with `SQLite_Create.ipynb` in `/jupyter`
- add '豆瓣电影' to navbar in tempalte `base.html`
- add new route to `/douban` in `app.py`

