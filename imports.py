file='list.txt'
def make_dict(line):
    show = {}
    show['name'] = line[0]
    show['type'] = line[1]
    show['season'] = line[2]
    show['last_ep'] = line[3]
    return show


def read_file(file = file):
    list = []
    try:
        with open(file, 'r') as f:
            content = f.readlines()
            content = [x.replace('\n', "") for x in content]
            content = [x.replace('\r', "") for x in content]
            content = [x.split(',') for x in content]
        for line in content:
            list.append(make_dict(line))

        return list
    except:
        raise('The file is empty')

def write_file(show, file = file):
    with open(file, 'a') as f:
        f.write(f'{show}\n')

def search(name, file = file):
    with open(file, 'r') as f:
        content = f.readlines()
        content = [x.replace('\n', "") for x in content]
        content = [x.replace('\r', "") for x in content]
        content = [x.split(',') for x in content]
    for line in content:
        if name in line:
            return make_dict(line)

def delete(name, file = file):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            if name not in line.split(',')[0]:
                f.write(line)
