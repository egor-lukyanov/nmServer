from typing import List, Tuple, Union

from storage import all_metrics


def handle_packet(data: dict):
    agg = process(data.get('data', []))
    for key, value in agg.items():
        update_dict(all_metrics, (key, value))
    return all_metrics


def update_dict(target: dict, data: Tuple[str, Union[float, list]]):
    key, value = data
    if key in target:
        target[key] = (target[key] + value) if isinstance(value, list) else (target[key] + [value])
    else:
        target[key] = value if isinstance(value, list) else [value]


def process(data: List[dict]) -> dict:
    result = {}
    for item in data:
        metrics = item.get('data', {})
        for key, value in metrics.items():
            update_dict(result, (key, value))
    return result
