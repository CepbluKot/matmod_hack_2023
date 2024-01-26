import datetime


def columns_to_dict(self):
    dict_ = {}
    for key in self.__mapper__.c.keys():

        dict_[key] = getattr(self, key)
    return dict_


def groupData(data):
    data = [columns_to_dict(x) for x in data]

    grouped_data = {}

    for row in data:
        aircraft_id = row['aircraft_id']

        if aircraft_id not in grouped_data:
            grouped_data[aircraft_id] = []

        grouped_data[aircraft_id].append(row)

    for row in grouped_data:
        aircraft_data = {}

        for x in grouped_data[row]:
            engine_id = x['engine_id']

            if engine_id not in aircraft_data:
                aircraft_data[engine_id] = []

            aircraft_data[engine_id].append(x)

        grouped_data[row] = aircraft_data

    for aircraft_id in grouped_data:
        for key, value in grouped_data[aircraft_id].items():
            value.sort(key=lambda x: x['flight_datetime'], reverse=False)

    return grouped_data
