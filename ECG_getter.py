import json


raw_dataset_path="C:\\Users\\User\\Desktop\\ecg_data_200.json" #файл с датасетом

def healthy(diagnos):
    is_heathy =True
    axis_ok = False
    rythm_ok = False
    for key in diagnos.keys():
        if key == 'electric_axis_normal':
            if diagnos[key] == True:
                axis_ok = True
                continue
        if key == 'regular_normosystole':
            if diagnos[key] == True:
                rythm_ok = True
                continue
        if diagnos[key] == True:
            is_heathy = False
            break
    return axis_ok and rythm_ok and is_heathy

def get_signal():
    lead_name = 'i'
    with open(raw_dataset_path, 'r') as f:
        data = json.load(f)

        for case_id in data.keys():
            leads = data[case_id]['Leads']
            diag = data[case_id]['StructuredDiagnosisDoc']
            if healthy(diag):
                new_entry = leads[lead_name]['Signal']
                return new_entry
    return None


print(get_signal())