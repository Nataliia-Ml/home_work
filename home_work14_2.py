import json


def some_func(*args, **kwargs):
    args_list = list(args)
    kwargs_list = list(kwargs)
    chunk_size = int(len(args_list)/len(kwargs_list))
    new_args_list = [args_list[i:i + chunk_size]for i in range(0, len(args_list), chunk_size)]
    return dict(zip(kwargs_list, new_args_list))


def load_dict(some_dict: dict, json_path):
    with open(json_path, "w") as file:
        json.dump(some_dict, file)


def main():
    result_some_func = some_func(
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
        one="first", two="second", three="third", four="fourth", five="fifth"
        )
    load_dict(result_some_func, "new_json_file.json")


if __name__ == '__main__':
    main()

