import csv


class Alert:
    def __init__(self):
        self.id = 0
        self.mail = ""
        self.query = ""
        self.active = False


def read_from_csv(input_file="/home/ziyixu/Downloads/basic_alert.csv"):
    with open(input_file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        alerts_do = []
        alerts_drouot = []
        for row in reader:
            if row[10] == "1" and row[9] == "drouotonline":
                alert_tmp = Alert()
                alert_tmp.id = row[0]
                alert_tmp.mail = row[5]
                alert_tmp.query = row[8]
                alert_tmp.active = True
                alerts_do.append(alert_tmp)
            if row[10] == "1" and row[9] == "drouot":
                alert_tmp = Alert()
                alert_tmp.id = row[0]
                alert_tmp.mail = row[5]
                alert_tmp.query = row[8]
                alert_tmp.active = True
                alerts_drouot.append(alert_tmp)
        return alerts_do, alerts_drouot


# 0 id, 5 mail, 8 query, 9 site, 10 active
# '2975630;0;0;"2021-08-24 11:25:37";"2021-08-24 11:25:37";"user_email@gmail.com";0;0;"Chantal thomass";"site_à_supprimer";"0";pass_id'

if __name__ == '__main__':
    alerts_do, alerts_drouot = read_from_csv()

    alerts_drouot_map = dict()

    for alert in alerts_drouot:  # generate a dict where key = user_email, value = a list of key_words
        if alerts_drouot_map.__contains__(alert.mail):
            alerts_drouot_map[alert.mail].append(alert.query)
        else:
            alerts_drouot_map[alert.mail] = [alert.query]

    count = 0
    doublon_ids = []
    for alert in alerts_do:
        if alerts_drouot_map.__contains__(alert.mail):
            for query in alerts_drouot_map[alert.mail]:
                if alert.query == query:
                    doublon_ids.append(alert.id)
                    count += 1

    print("Found " + str(count) + " doublons côté DO, where active = 1 and the query can be found in d.com with exact the same email")
    print("use this list in sql query :")

    print(",".join(doublon_ids))
    ''' this out put can be used in sql command : 
        UPDATE `schema`.`alert_table`
        SET
            `active` = 'false'
        WHERE
            (`id` IN  (OUT_PUT));
        - exact command with correct table_name etc, see in sql_log
    '''
