import json
import pathlib
import typing as tp

import final_solution


PATH_TO_TEST_DATA = pathlib.Path("data") / "test_texts.json"
PATH_TO_OUTPUT_DATA = pathlib.Path("results") / "output_scores.json"


def load_data(path: pathlib.PosixPath = PATH_TO_TEST_DATA) -> tp.List[str]:
    """load data"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def save_data(data, path: pathlib.PosixPath = PATH_TO_OUTPUT_DATA):
    """save data"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)


def main():
    """main solution"""
    texts = load_data()
    scores = final_solution.solution.score_texts(texts)
    save_data(scores)


if __name__ == "__main__":
    main()
