SEPARATOR = ","

#read values function
def readValues(filename) -> str:
    values = ""
    with open(filename, "r", encoding="UTF-8") as source:
        for line in source:
            value = line.strip()
            if value == "":
                continue
            if values == "":
                values = value
            else:
                values += SEPARATOR + value
        return values

#analysing values function
def analyseValues(values) -> str:
    numbers = values.split(SEPARATOR) if values != "" else []
    count = 0
    sum = 0
    greater = 0
    for number in numbers:
        value = int(number)
        count += 1
        sum += value
        if value > greater:
            greater = value
    average = sum / count if count > 0 else 0

    result = "Count;Sum;Greatest;Average\n"
    result += f"{count};{sum};{greater};{average:.2f}\n"
    return result

#displaying function
def displayingValues(filename, result):
    print("#### Number analysis - START ####")
    print(f'File {filename} results:')
    print(result)
    print()
    print("#### Number analysis - END ####")
    return None

#main function
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    result = analyseValues(values)
    displayingValues(filename, result)
    print("Program ending.")

if __name__ == "__main__":
    main()