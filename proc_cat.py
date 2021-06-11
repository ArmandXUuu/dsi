import csv

class Cat:
    def __init__(self):
        self.id = 0
        self.nom_1 = ""
        self.nom_2 = ""
        self.nom_3 = ""

def read_from_csv(input_file = "input.csv"):
    with open(input_file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
    return rows

def process(input_file = "cat.csv"):
    rows = read_from_csv(input_file)
    cats = []

    for row in rows:
        cat_tmp = Cat()
        cat_tmp.id = row[0]
        cat_tmp.nom_1 = row[1]
        cat_tmp.nom_2 = row[2]
        cat_tmp.nom_3 = row[3]
        cats.append(cat_tmp)

    return cats
    

def output_txt(cats):
    f = open("/home/ziyixu/Downloads/cat/Label1.txt",'a')
    for cat in cats:
        f.write("categories.seo.label."+str(cat.id)+"="+cat.nom_1)
        f.write('\n')
    f.close()

    f = open("/home/ziyixu/Downloads/cat/Label2.txt",'a')
    for cat in cats:
        f.write("categories.seo.label."+str(cat.id)+"="+cat.nom_2)
        f.write('\n')
    f.close()

    f = open("/home/ziyixu/Downloads/cat/Label3.txt",'a')
    for cat in cats:
        f.write("categories.seo.label."+str(cat.id)+"="+cat.nom_3)
        f.write('\n')
    f.close()



def main():
    
    output_txt(process("/home/ziyixu/Downloads/cat/cat.csv"))
    print("Thank you for using, processing complete.")

if __name__ == '__main__':
    main()