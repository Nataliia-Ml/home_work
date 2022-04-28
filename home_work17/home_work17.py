FILE_NAME = "settings.cfg"


def creator_settings_dict(file_name: str):
    with open(file_name, 'r') as file:
        settings_list = file.readlines()
        orig_settings = {el.split(": ")[0]: el.split(": ")[1].replace('\n', '') for el in settings_list}
    return orig_settings


def creator_new_settings_dict(orig_settings: dict, new_settings: dict):
    for k1, v1 in orig_settings.items():
        for k2, v2 in new_settings.items():
            if k1 == k2:
                orig_settings[k1] = v2
    return orig_settings


def creator_new_settings_list(orig_settings: dict):
    new_settings_list = []
    for k, v in orig_settings.items():
        new_settings_list.append(f"{k}: {v}\n")
    return new_settings_list


def file_rewriting(file_name: str, new_settings_list: list):
    with open(file_name, 'w') as file:
        file.writelines(new_settings_list)


def change_settings(file_name: str, new_settings: dict):
    orig_settings_dict = creator_settings_dict(file_name)
    new_settings = creator_new_settings_dict(orig_settings_dict, new_settings)
    new_list = creator_new_settings_list(new_settings)
    file_rewriting(file_name, new_list)


settings = [
    {"ip_address": "127.0.0.1", "port": "8080", "use_ssl": False, "is_admin": True},
    {"ip_address": "127.77.0.1", "port": "8080"},
    {"ip_address": "192.0.0.1", "debug_mode": False}
    ]


if __name__ == '__main__':
    for setting in settings:
        change_settings(FILE_NAME, setting)
