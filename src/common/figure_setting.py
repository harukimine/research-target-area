class FigureSetting:
    default = {
        "dpi": 300,
        "bbox_inches": "tight",
        "pad_inches": 0,
    }
    png = {
        **default,
        "format": "png",
    }
    tiff = {
        **default,
        "format": "tiff",
    }
    gif = {
        **default,
        "format": "gif",
        "save_all": True,
    }
    monochrome = {
        "bbox_inches": "tight",
        "pad_inches": 0,
    }
    monochrome_png = {
        **monochrome,
        "format": "png",
    }
    monochrome_tiff = {
        **monochrome,
        "format": "tiff",
    }


class PltPlotParameter:
    # area
    default = {
        "figsize": (8, 8),
        "edgecolor": "black",
        "linewidth": 0.7,
    }
    whole_area = {
        **default,
        "facecolor": "white",
    }
    scope_area = {
        **default,
        "linewidth": 0.3,
        "facecolor": "HoneyDew",
    }
    watershed = {
        **scope_area,
        "edgecolor": "blue",
    }
    catchment = {
        **watershed,
        "facecolor": "blue",
    }


class PltConfig:
    rc_config = {
        "font.family": "Times New Roman",
        "font.size": 16,
        "figure.autolayout": True,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "xtick.major.width": 1,
        "ytick.major.width": 1,
        "axes.linewidth": 1,
    }
