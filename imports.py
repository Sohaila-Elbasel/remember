def read_file(file='list.txt'):
    list = []
    try:
        with open(file, 'r') as f:
            content = f.readlines()
            content = [x.replace('\n', "") for x in content]
            content = [x.replace('\r', "") for x in content]
            content = [x.split(',') for x in content]
        for line in content:
            show = {}
            show['name'] = line[0]
            show['type'] = line[1]
            show['season'] = line[2]
            show['last_ep'] = line[3]
            list.append(show)

        return list
    except:
        raise('The file is empty')

def write_file(show, file='list.txt'):
    with open(file, 'a') as f:
        f.write(f'{show}\n')
