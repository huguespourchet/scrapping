import csv

class Toolkit:

    def fileReader(file):
        result = []
        with open(file, 'r', encoding="UTF8", newline="") as f:
            reader = csv.DictReader(f)
            for line in reader:
                result.append(line) 
        return result

    def fileWriter(file, fieldnames, data):
        with open(file, 'w', encoding="UTF8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            
    def triTaillesDispos(objects):
        for object in objects:
            if 'disabled' in object.get('class'):
                object.extract()
        return objects
    
    def getCategories(string):
        second_dash_index = string.find("-", string.find("-") + 1)
        return string[second_dash_index+1:]