import json
import chardet
import locale


def load_file_json(file_path: str):
    with open(file_path, "rb") as f:
        default_encoding = "utf-8"
        os_locale = locale.getlocale()
        match os_locale:
            case (_, "936"):
                default_encoding = "gbk"
            case (_, "1252"):
                default_encoding = "windows-1252"
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"] or default_encoding
    data = json.loads(raw_data.decode(encoding))
    return data


if __name__ == "__main__":
    import os

    if not os.path.exists("config.json"):
        exit
    config = load_file_json("config.json")
    print("Config data type: " + str(type(config)))
    print("Config data content: " + str(config))
