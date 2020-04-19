def devices_to_json(path):
    #path = './devices'
    device_info = {}

    with open(path) as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        line = lines[i].split("|")
        if ("NAME" in line[0]):
            device_info[line[1]] = [None]*2
        elif("IP" in line[0]):
            name = lines[i-1].split("|")
            device_info[name[1]][0] = line[1]
        elif("MAC" in line[0]):
            name = lines[i-2].split("|")
            device_info[name[1]][1] = line[1]
    return(device_info)