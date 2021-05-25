import ged_lib as gl

class working_class(object):
    def __init__(self, tag=None, id_type=None, id=None, text=None):
        self.tag = tag
        self.id_type = id_type
        self.id = id
        self.text = text

working = []

column_heading = ["Tag", "ID Type", "ID", "Text"]

def write_ged_file():
#    print('Writing New GED File')
    gl.read_individuals()
    gl.read_families()
    load_working()
    tag_working()
    write_working()
    write_new_ged_file()
    
def write_new_ged_file():   
    file = open('new.ged','w')
    for i in range(0,len(working)):
        if working[i].tag == 'Y':
            file.write(working[i].text + '\n')
    file.close()

def read_working():
    file = open('working.txt','r')
    working.clear()
    s = file.readline()
    i = 0
    while True:
        s = file.readline()
        s = s.strip()
        if s == '':
            break
        x = s.split("~")
        add_working(x[0], x[1], int(x[2]), x[3])
        i = i + 1

#    print("Read " + str(len(working)) + " Working GED file records")

def add_working(f0, f1, f2, f3):
    working.append(working_class(f0, f1, f2, f3))
 
def write_working():
    file = open('working.txt','w')
    line = ""
    for i in range(len(column_heading)):
        line = line + column_heading[i]  + '~'
    line = line[0:len(line)-1]        
    file.write(line + '\n')

    for i in range(0,len(working)):
        line = working[i].tag + "~"
        line = line + working[i].id_type + "~"
        line = line + str(working[i].id) + "~"
        line = line + working[i].text
        file.write(line + '\n')

    file.close()

#    print("Written " + str(len(working)-1) + " Working GED File records")

def load_working():
#    print("Loading Working GED File")
    gl.get_params()
    
    working.clear()
    gfile = open(gl.ged_file_name, "r")

    tag = ""
    while True:
        line = gfile.readline()
        s = line.strip()
        if s == "": break
    
        c1 = s[:1]
        if c1 == "0":
            id_type = ""
            id = 0
            record_type = s[-4:]
            if record_type == "INDI":
                individual = s[4:]
                individual = individual[0:individual.find("@")]
                id_type = "I"
                id = int(individual)
            if record_type == " FAM":
                family = s[4:]
                family = family[0:family.find("@")]
                id_type = "F"
                id = int(family)
        text = s
        add_working(tag, id_type, id, text)
        
    gfile.close()

def tag_working():
    for i in range(0,len(working)):
        if working[i].id_type == "":
            working[i].tag = 'Y'
        if working[i].id_type == "I":
            id = working[i].id
            working[i].tag = gl.individuals[id].tag
        if working[i].id_type == "F":
            id = working[i].id
            working[i].tag = gl.families[id].tag
                
write_ged_file()

