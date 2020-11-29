import pandas as pd


def load_scores(file="data/dougscore.csv"):
    column_titles = ["Vehicle Year", "Make", "Model", "Styling", "Acceleration", "Handling", "Fun", "Cool", "Weekend",
                     "Features", "Comfort", "Quality", "Practicality", "Value", "Daily", "Total",
                     "Runtime", "Film City", "Film State", "Manufacturer Country"]
    doug_frame = pd.read_csv(file, names=column_titles)

    return doug_frame


def find_dominated_cars(initial_car, frame, columns=None):
    if columns is None:
        columns = [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]

    dominated_cars = pd.DataFrame([initial_car])

    for car in frame.iloc:
        if not car.equals(initial_car):
            one_greater = False
            i = 0
            while not one_greater and i < len(columns):
                if initial_car[columns[i]] < car[columns[i]]:
                    one_greater = True
                i += 1
            if not one_greater:
                dominated_cars = dominated_cars.append([car])

    return dominated_cars


def find_superior_cars(initial_car, frame, columns=None):
    if columns is None:
        columns = [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]

    result = pd.DataFrame([initial_car])

    dominated = True
    for second_car in frame.iloc:
        if not initial_car.equals(second_car):
            dominated = True
            i = 0
            while i < len(columns):
                if initial_car[columns[i]] > second_car[columns[i]]:
                    dominated = False
                i += 1
            if dominated:
                result = result.append([second_car])

    return result


def frames_to_excel(frames, names, file_name):
    with pd.ExcelWriter(file_name) as writer:
        for i in range(len(frames)):
            frames[i].to_excel(writer, sheet_name=names[i])
    return 1


if __name__ == '__main__':
    df = load_scores()

    idc = find_superior_cars(df.iloc[13], df, [3, 4, 5, 6, 7, 9])
    # idc = find_dominated_cars(df.iloc[222], df)

    for x in idc.iloc:
        print(x[:3])
        print()
