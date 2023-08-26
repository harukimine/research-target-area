import geopandas as gpd
from geopandas import GeoDataFrame as GDF
import matplotlib.pyplot as plt
from shapely.ops import unary_union

from common.figure_setting import FigureSetting
from common.figure_setting import PltConfig
from common.figure_setting import PltPlotParameter
from common.geo_setting import PrefectureArea


INPUT_DIR = "base_data"
WATERSHED_DIR = f"{INPUT_DIR}/WatershedBoundary"

PREFECTURE_AREA_LIST = PrefectureArea.dict["九州地方"]
TARGET_PREFECTURE_LIST = ["宮崎県"]

WATERSHED_PATH = f"{WATERSHED_DIR}/W12-52A_45_WatershedBoundary.geojson"
WATERSHED_LIST = ["89108"]

CATCHMENT_PATH = f"{WATERSHED_DIR}/clipped_watershed.geojson"
CATCHMENT_LIST = []

LONGITUDE_RANGE = [129.2, 132.2]
LATITUDE_RANGE = [31, 34]


def main():
    gdf = gpd.read_file(f"{INPUT_DIR}/japan.geojson")
    whole_area = narrow_down_area(gdf, PREFECTURE_AREA_LIST)
    prefecture = narrow_down_area(gdf, TARGET_PREFECTURE_LIST)
    watershed = get_watershed_gdf(WATERSHED_PATH, WATERSHED_LIST)
    catchment = get_watershed_gdf(CATCHMENT_PATH, CATCHMENT_LIST)

    plt.rcParams.update(PltConfig.rc_config)
    fig, ax = plt.subplots()
    whole_area.plot(ax=ax, **PltPlotParameter.whole_area)
    prefecture.plot(ax=ax, **PltPlotParameter.scope_area)
    watershed.plot(ax=ax, **PltPlotParameter.watershed)
    catchment.plot(ax=ax, **PltPlotParameter.catchment)

    plt.xlim(LONGITUDE_RANGE)
    plt.ylim(LATITUDE_RANGE)
    plt.savefig("target-area.png", **FigureSetting.png)


def narrow_down_area(gdf: GDF, target_list: list[str]) -> GDF:
    return gdf[gdf["nam_ja"].isin(target_list)]


def get_watershed_gdf(path: str, watershed_list: list[str] = None) -> GDF:
    gdf = gpd.read_file(path)
    if watershed_list:
        gdf = narrow_down_watershed(gdf, watershed_list)
    gdf = merge_boundary(gdf)
    return gdf


def narrow_down_watershed(gdf: GDF, watershed_list: list[str]) -> GDF:
    return gdf[gdf["W12_002"].isin(watershed_list)]


def merge_boundary(gdf: GDF) -> gpd.GeoSeries:
    return gpd.GeoSeries(unary_union(gdf.geometry))


if __name__ == "__main__":
    main()
