import params as pa
import individuals as ind
import families as fam
import children as chi

def tag_ancestors_families():
#    print("Tagging Ancestor's Families")
    ind.read_individuals()
    fam.read_families()
    chi.read_children()
    
    pa.get_params()
    family_id = int(pa.initial_family)
    tree_walk(family_id)

    for i in range(0,len(fam.families)):
        if fam.families[i].tag == 'Y':
            tag_family(fam.families[i].family_id, 0)

    additional = 1    
    while additional > 0:
        additional = tag_additional_families()
        
    ind.write_individuals()
    fam.write_families()
    chi.write_children()

def tree_walk(family_id):
    if family_id > 0:
        fam.families[family_id].tag = 'Y'   
        if fam.families[family_id].husband_id != 0:
            husband_id = fam.families[family_id].husband_id
            family_where_child = ind.get_family_where_child(husband_id)
            if family_where_child != 0:
                tree_walk(family_where_child)

        if fam.families[family_id].wife_id != 0:
            wife_id = fam.families[family_id].wife_id
            family_where_child = ind.get_family_where_child(wife_id)
            if family_where_child != 0:
                tree_walk(family_where_child)

def tag_family(family_id, tag_count):
    husband_id = fam.families[family_id].husband_id
    if husband_id != 0:
        if ind.individuals[husband_id].tag == "N":
            ind.individuals[husband_id].tag = 'Y'
            tag_count = tag_count + 1
            
    wife_id = fam.families[family_id].wife_id
    if wife_id != 0:
        if ind.individuals[wife_id].tag == "N":
            ind.individuals[wife_id].tag = 'Y'
            tag_count = tag_count + 1
        
    for i in range(1,len(chi.children)):
        child_family_id = chi.children[i].family_id
        if child_family_id != 0:
            if child_family_id > family_id: break
            if family_id == child_family_id:
                child_id = chi.children[i].child_id
                if ind.individuals[child_id].tag == "N":
                    ind.individuals[child_id].tag = 'Y'
                    tag_count = tag_count + 1
    return(tag_count)

def tag_additional_families():
    tag_count = 0
    for i in range(0,len(ind.individuals)):
        if ind.individuals[i].tag == 'Y':
            id = ind.individuals[i].individual_id
            for f in range(0,len(fam.families)):
                if fam.families[f].husband_id == id or fam.families[f].wife_id == id:
                    family_id = fam.families[f].family_id
                    fam.families[family_id].tag = 'Y'   
                    tag_count = tag_family(family_id, tag_count)

    return(tag_count)

#tag_ancestors_families()
