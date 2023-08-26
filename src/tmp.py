import pandas as pd
import common.util as util


path = "base_file/river-code.csv"
df = pd.read_csv(path)

code_col = "code"
name_col = "river"

max_len_code = max([len(str(i)) for i in df[code_col].values.tolist()])
watershed_dict = {}
for index in df.index:
    code = str(df.at[index, code_col])
    code = "0" * (max_len_code - len(code)) + code
    name = df.at[index, name_col]
    watershed_dict[name] = code

util.save_json(watershed_dict, path.replace("csv", "json"))
