# draw target catchment area in Japan

## purpose

- 対象領域図の作成
- 図に使用するデータの収集
- 収集したデータの加工

## Usage

draw target catchment area

```bash
python src/draw_target_area.py
```

## target area

![catchment area](https://github.com/harukimine/readme-image-source/blob/main/research-target-area/omaru-catchment.png?raw=true)

## data source (base_data)

- [都道府県別](https://github.com/dataofjapan/land)：japan.geojson
- [流域界](https://nlftp.mlit.go.jp/ksj/gmlold/datalist/gmlold_KsjTmplt-W12.html
)：WatershedBoundary
- [dam point](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-W01.html)：W01-14-g_Dam.geojson

## virtual env

windows

```bash
python -m venv .venv
./.venv/Scripts/activate
```

mac

```bash
python3 -m venv .venv
. .venv/bin/activate
```

pip

```bash
pip install --upgrade pip
pip install -r requirement.txt
```

## figure setting

- [color code](https://www.colordic.org/)
- [plt.rcParams](https://qiita.com/aurueps/items/d04a3bb127e2d6e6c21b
)
