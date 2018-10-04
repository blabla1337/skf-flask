from skf.database import db
from skf.api.security import log, val_num, val_float, val_alpha_num
from skf.database.checklists_kb import checklists_kb
from skf.database.checklist_types import checklist_types


def get_checklist_item(checklist_id, checklist_type):
    log("User requested specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
    val_num(checklist_type)
    result = checklists_kb.query.filter((checklists_kb.checklistID == checklist_id) & (checklists_kb.checklist_type == checklist_type)).one()
    return result


def get_checklist_item_types():
    log("User requested list checklist types", "LOW", "PASS")
    result = checklist_types.query.paginate(1, 500, False)
    return result


def create_checklist_type(data):
    log("User requested create a new checklist type", "LOW", "PASS")
    checklist_name = data.get('checklist_name')
    checklist_description = data.get('checklist_description')
    val_alpha_num(checklist_name)
    val_alpha_num(checklist_description)
    types = checklist_types(checklist_name, checklist_description)
    db.session.add(types)
    db.session.commit()
    return {'message': 'Checklist type successfully created'} 


def update_checklist_type(id, data):
    log("User requested update checklist type", "LOW", "PASS")
    checklist_name = data.get('checklist_name')
    checklist_description = data.get('checklist_description')
    val_alpha_num(checklist_name)
    val_alpha_num(checklist_description)
    val_num(id)
    result_checklist_types = checklist_types.query.filter(checklist_types.checklist_type == id).one()
    result_checklist_types.checklist_name = checklist_name
    db.session.add(result_checklist_types, checklist_description)
    db.session.commit()
    return {'message': 'Checklist item successfully updated'} 


def delete_checklist_type(checklist_type_id):
    log("User deleted checklist type", "MEDIUM", "PASS")
    val_num(checklist_type_id)
    result_checklist_types = checklist_types.query.filter(checklist_types.checklist_type == checklist_type_id).one()
    db.session.delete(result_checklist_types)
    db.session.commit()
    return {'message': 'Checklist type successfully deleted'}


def create_checklist_item(checklistID, checklist_type, data):
    log("User requested create a new checklist item", "LOW", "PASS")
    checklist_content = data.get('content')
    include_always = data.get('include_always')
    include_first = data.get('include_first')
    question_sprint_ID = data.get('question_sprint_ID')
    question_pre_ID = data.get('question_pre_ID')
    checklist_kbID = data.get('kbID')
    val_num(checklist_kbID)
    val_num(checklist_type)
    checklist_item = checklists_kb(checklistID, checklist_content, checklist_kbID, checklist_type, include_always, include_first, question_sprint_ID, question_pre_ID)
    db.session.add(checklist_item)
    db.session.commit()
    return {'message': 'Checklist item successfully created'} 


def update_checklist_item(checklist_id, checklist_type, data):
    log("User requested update a specific checklist item", "LOW", "PASS")
    val_float(checklist_id)
    val_num(checklist_type)
    if data.get('kbID') == "":
        kbID = 0
    else:
        kbID = data.get('kbID')
    val_num(kbID)
    result_checklist_kb = checklists_kb.query.filter((checklists_kb.checklistID == checklist_id) & (checklists_kb.checklist_type == checklist_type)).one()
    result_checklist_kb.title = data.get('title')
    result_checklist_kb.content = data.get('content')
    result_checklist_kb.include_always = data.get('include_always')
    result_checklist_kb.include_first = data.get('include_first')
    result_checklist_kb.question_sprint_ID = data.get('question_sprint_ID')
    result_checklist_kb.question_pre_ID = data.get('question_pre_ID')
    result_checklist_kb.kbID = kbID
    result_checklist_kb.checklistID = checklist_id
    result_checklist_kb.checklist_type = checklist_type
    db.session.add(result_checklist_kb)
    db.session.commit()
    return {'message': 'Checklist item successfully updated'} 


def get_checklist_items(checklist_type):
    log("User requested list of checklist items", "LOW", "PASS")
    val_num(checklist_type)
    result = checklists_kb.query.filter(checklists_kb.checklist_type == checklist_type).paginate(1, 1500, False)
    return result
    

def order_checklist_items(checklist_items, get_checklist_items_lvl, lvl, checklist_type):
    ordered_checklist_items = []
    for item in checklist_items.items:
        numbers = item.checklistID.split('.')
        category = int(numbers[0])
        category_requirement = int(numbers[1])
        if (len(ordered_checklist_items) == 0):
            ordered_checklist_items.append(item)
        else:
            y = 0
            while y < len(ordered_checklist_items):
                numbers_ordered = ordered_checklist_items[y].checklistID.split('.')
                category_ordered = int(numbers_ordered[0])
                category_requirement_ordered = int(numbers_ordered[1])
                if (category < category_ordered):
                    ordered_checklist_items.insert(y, item)
                    break
                else:
                    if (category == category_ordered):
                        if (category_requirement < category_requirement_ordered):
                            ordered_checklist_items.insert(y, item)
                            break
                y = y + 1
            if (y == len(ordered_checklist_items)):
                ordered_checklist_items.insert(y, item)

    if (get_checklist_items_lvl):
        if (not (checklist_type == 1)):
            i = 0
            previousItemLevel = -1
            orderedWithEmpties = []
            for item in ordered_checklist_items:
                if ((item.checklist_items.level == 0 and previousItemLevel == 0) or (item.checklist_items.content == "Resiliency Against Reverse Engineering Requirements" and not (lvl == 3))):
                    if (item.checklist_items.content == "Resiliency Against Reverse Engineering Requirements"):
                        orderedWithEmpties.append(item)
                        previousItemLevel = item.checklist_items.level
                        checklist_empty = checklists("0.0", "Requirements of Reverse Engineering can be added to form a level " + str(lvl-3) + "+R.", -1, 0)
                        checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
                        orderedWithEmpties.append(checklists_kb_empty)
                    else:
                        checklist_empty = checklists("0.0", "No items for this category in this checklist level", -1, 0)
                        checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
                        orderedWithEmpties.append(checklists_kb_empty)
                        orderedWithEmpties.append(item)
                        previousItemLevel = item.checklist_items.level
                else:
                    orderedWithEmpties.append(item)
                    previousItemLevel = item.checklist_items.level
                i = i + 1
            checklist_items.items = orderedWithEmpties
        else:
            orderedWithR6 = []
            checklist_empty = checklists("0.0", "Using Requirements of Reverse Engineering you can form the levels L1+R or L2+R.", -1, 0)
            checklists_kb_empty = checklists_kb("0.0", checklist_empty, 0, None)
            orderedWithR6.append(checklists_kb_empty)
            for item in ordered_checklist_items:
                if (item.checklist_items.level == 3):
                    checklist_modified = checklists(item.checklistID, item.checklist_items.content, 3, item.checklist_items.kbID)
                    modifiedItem = checklists_kb(item.checklistID, checklist_modified, item.kbID, item.kb_items)
                    orderedWithR6.append(modifiedItem)
                else:
                    orderedWithR6.append(item)
            checklist_items.items = orderedWithR6
    return checklist_items