import sys


def get_inversions_in_list(enumed_data):
    res = 0
    for i in range(0, len(enumed_data) - 1):

        for j in range(i + 1, len(enumed_data)):

            if enumed_data[i] > enumed_data[j]:
                res += 1
    return res


all_data = {}
active_user = {}
for line in sys.stdin:
    name, pref = line.split(":")
    if not active_user:
        active_user[name] = pref.split(",")
    else:
        all_data[name] = pref.split(",")

active_user_prefs = {}
i = 0
for p in active_user.values():
    active_user_prefs[p] = i
    i += 1

inversion_dict = {}

for k, v in all_data.items():
    enumed = []
    for i in v:
        enumed.append(active_user_prefs[i])

    res = get_inversions_in_list(enumed)
    inversion_dict[k] = res

final_res = [v[0] for v in sorted(inversion_dict.items(), key=lambda kv: (kv[1], kv[0]))]

print(final_res)
