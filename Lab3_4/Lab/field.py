def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
    else:
        for item in items:
            filtered_item = {key: item[key] for key in args if item.get(key) is not None}
            if filtered_item:
                yield filtered_item
