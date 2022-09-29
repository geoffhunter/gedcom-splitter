import ged_lib as gl

def tag_ancestors_families():
#    print("Tagging Ancestor's Families")
    gl.read_individuals()
    gl.read_families()
    gl.read_children()
    
    gl.get_params()
    family_id = int(gl.initial_family)
    tree_walk(family_id)

    for i in gl.families:
        if gl.families[i].tag == 'Y':
            tag_family(gl.families[i].family_id, 0)

    additional = 1    
    while additional > 0:
        additional = tag_additional_families()
        
    gl.write_individuals()
    gl.write_families()

def tree_walk(family_id):
    if family_id > 0:
        gl.families[family_id].tag = 'Y'   
        if gl.families[family_id].husband_id != 0:
            husband_id = gl.families[family_id].husband_id
            family_where_child = gl.get_family_where_child(husband_id)
            if family_where_child != 0:
                tree_walk(family_where_child)

        if gl.families[family_id].wife_id != 0:
            wife_id = gl.families[family_id].wife_id
            family_where_child = gl.get_family_where_child(wife_id)
            if family_where_child != 0:
                tree_walk(family_where_child)

def tag_family(family_id, tag_count):
    husband_id = gl.families[family_id].husband_id
    if husband_id != 0:
        if gl.individuals[husband_id].tag == "N":
            gl.individuals[husband_id].tag = 'Y'
            tag_count = tag_count + 1
            
    wife_id = gl.families[family_id].wife_id
    if wife_id != 0:
        if gl.individuals[wife_id].tag == "N":
            gl.individuals[wife_id].tag = 'Y'
            tag_count = tag_count + 1
        
    for i in gl.children:
        child_family_id = gl.children[i].family_id
        if child_family_id != 0:
            if child_family_id > family_id: break
            if family_id == child_family_id:
                child_id = gl.children[i].child_id
                if gl.individuals[child_id].tag == "N":
                    gl.individuals[child_id].tag = 'Y'
                    tag_count = tag_count + 1
    return(tag_count)

def tag_additional_families():
    tag_count = 0
    for i in gl.individuals:
        if gl.individuals[i].tag == 'Y':
            id = gl.individuals[i].individual_id
            for f in gl.families:
                if gl.families[f].husband_id == id or gl.families[f].wife_id == id:
                    family_id = gl.families[f].family_id
                    gl.families[family_id].tag = 'Y'   
                    tag_count = tag_family(family_id, tag_count)

    return(tag_count)

#tag_ancestors_families()
