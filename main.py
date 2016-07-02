# coding: utf-8


def read_json():
    """Returns a dict with project name and list of dates with corresponding
    work durations in hours."""

    import datetime
    import json

    def get_project_name(project_id):
        # TODO, read from json data
        return "My Project"

    def mybreak(item):
        """Include a small break, to round up the 25 minute slots to 30
        minutes."""
        # TODO
        return 300

    def get_project_ids():
        # TODO, currently hardcoded
        return [6]

    json_data = open('backup.json').read()
    data = json.loads(json_data)
    work = data['workUnits']

    work = [{
        "date": datetime.datetime.fromtimestamp(x['_t']).date(),
        "duration": x['_d'],
        "project_id": x['_p']
        } for x in work]

    results = {}

    for project_id in get_project_ids():
        project_name = get_project_name(project_id)
        items = [x for x in work if x['project_id'] == project_id]
        project_results = []
        first_date = items[0]['date']
        last_date = items[-1]['date']
        date_list = [last_date - datetime.timedelta(days=x) for x in range(0,
                     (last_date - first_date).days)]
        for date in date_list[::-1]:
            seconds = sum((x['duration']+mybreak(x) for x in items
                           if x['date'] == date))
            project_results.append({"date": date, "hours": seconds / 60 / 60})
        results[project_name] = project_results

    return results


def write_output(results):
    import xlsxwriter

    workbook = xlsxwriter.Workbook('output.xlsx')
    date_format = workbook.add_format({'num_format': 'd mmm yyyy'})
    hour_format = workbook.add_format({'num_format': '[hh]:mm'})

    for project_name, items in results.items():
        worksheet = workbook.add_worksheet(project_name.strip())
        worksheet.set_column('A:A', 25)  # widen column A for extra visibility
        for i, item in enumerate(items):
            date = item['date']
            hours = item['hours']
            worksheet.write(i, 0, date, date_format)
            if hours:
                worksheet.write(i, 1, hours / 24, hour_format)

    workbook.close()

results = read_json()
write_output(results)
